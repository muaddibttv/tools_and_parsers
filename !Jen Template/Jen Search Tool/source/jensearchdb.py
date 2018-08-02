import requests,re,traceback
try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+
import os
import json
from sqlite3 import dbapi2 as database
from ConfigParser import SafeConfigParser
import xml.etree.ElementTree as ET

identifiers = set()


def jen_get_tag_content(collection, tag, default):
    try:
        result = re.findall('<%s>(.+?)</%s>' % (tag, tag), collection)[0]
        return result
    except:
        return default


def jen_list(content):
    content = str(content)
    if content.strip().startswith('#EXTM3U') and '#EXTINF' in content:
        content = re.compile('#EXTINF:.+?\,(.+?)\n(.+?)\n', re.MULTILINE | re.DOTALL).findall(content)
        content = ['<item><title>%s</title><link>%s</link></item>' % (i[0], i[1]) for i in content]
        content = ''.join(content)

    info = content.split('<item>')[0].split('<dir>')[0]
    vip = jen_get_tag_content(info, 'poster', '0')
    image = jen_get_tag_content(info, 'thumbnail', '0')
    fanart = jen_get_tag_content(info, 'fanart', '0')

    items = re.compile(
        '((?:<item>.+?</item>|<dir>.+?</dir>|<plugin>.+?</plugin>|<info>.+?</info>|'
        '<title>[^<]+</title><link>[^<]+</link><thumbnail>[^<]+</thumbnail><mode>[^<]+</mode>|'
        '<name>[^<]+</name><link>[^<]+</link><thumbnail>[^<]+</thumbnail><date>[^<]+</date>))',
        re.MULTILINE | re.DOTALL).findall(content)

    results = []
    for item in items:
        try:
            regex = re.compile('(<regex>.+?</regex>)', re.MULTILINE | re.DOTALL).findall(item)
            regex = ''.join(regex)
            regex = quote(regex)

            item = item.replace('\r', '').replace('\n', '').replace('\t', '').replace('&nbsp;', '')
            item = re.sub('<link></link>|<sublink></sublink>', '', item)

            name = item.split('<meta>')[0].split('<regex>')[0]
            try:
                name = re.findall('<title>(.+?)</title>', name)[0]
            except:
                name = re.findall('<name>(.+?)</name>', name)[0]
            if '<meta>' in name:
                raise Exception()

            date = jen_get_tag_content(item, 'date', '')
            if re.search(r'\d+', date):
                name += ' [COLOR red] Updated %s[/COLOR]' % date
            meta = jen_get_tag_content(item, 'meta', '0')
            url = jen_get_tag_content(item, 'link', '0')

            url = url.replace('>search<', '><preset>search</preset>%s<' % meta)
            url = '<preset>search</preset>%s' % meta if url == 'search' else url
            url = url.replace('>searchsd<', '><preset>searchsd</preset>%s<' % meta)
            url = '<preset>searchsd</preset>%s' % meta if url == 'searchsd' else url
            url = url.replace('<sublink></sublink>', '')
            url += regex

            if item.startswith('<item>'):
                action = 'play'
            elif item.startswith('<plugin>'):
                action = 'plugin'
            elif item.startswith('<info>') or url == '0':
                action = '0'
            else:
                action = 'directory'

            if action in ['directory', 'plugin']:
                folder = True
            elif not regex == '':
                folder = True
            else:
                folder = False

            image2 = jen_get_tag_content(item, 'thumbnail', image)
            if not str(image2).lower().startswith('http'):
                image2 = '0'

            fanart2 = jen_get_tag_content(item, 'fanart', fanart)
            if not str(fanart2).lower().startswith('http'):
                fanart2 = '0'

            content = jen_get_tag_content(meta, 'content', '0')

            if content in ['episode', 'season']:
                continue

            imdb = jen_get_tag_content(meta, 'imdb', '0')
            tvdb = jen_get_tag_content(meta, 'tvdb', '0')
            tvshowtitle = jen_get_tag_content(meta, 'tvshowtitle', '0')
            title = jen_get_tag_content(meta, 'title', '0')
            if title == '0' and not tvshowtitle == '0':
                title = tvshowtitle

            year = jen_get_tag_content(meta, 'year', '0')
            premiered = jen_get_tag_content(meta, 'premiered', '0')
            season = jen_get_tag_content(meta, 'season', '0')
            episode = jen_get_tag_content(meta, 'episode', '0')

            results.append({'name': name, 'vip': vip, 'url': url, 'action': action, 'folder': folder,
                            'poster': image2,
                            'banner': '0', 'fanart': fanart2, 'content': content, 'imdb': imdb, 'tvdb': tvdb,
                            'tmdb': '0',
                            'title': title, 'originaltitle': title, 'tvshowtitle': tvshowtitle, 'year': year,
                            'premiered': premiered, 'season': season, 'episode': episode})
        except:
            failure = traceback.format_exc()
            print('Exception: \n' + str(failure))
            pass
    return results


def recurse_list(url, errors=[]):
    global identifiers
    print("working on: " + url)
    # content = requests.get(url).text
    content = get_xml(url)
    if not content:
        print("investigate url: " + url)
        content = requests.get(url).text
    list = jen_list(content)
    xml = ""
    for item in list:
        if item['folder'] and not item['url'].startswith('plugin'):
            if not item['content'] in ["tvshow"] and not "tnpb/TV" in url:
                result_xml, result_errors = recurse_list(
                    item['url'], errors)
                xml += result_xml
                if result_errors is not None:
                    if type(result_errors) == list:
                        errors.extend(result_errors)
                    else:
                        errors.append(result_errors)
            else:
                if item["content"] == "0" and "/tnpb/" in url:
                    continue
                if item["url"] in ["0", "#"]:
                    continue
                if not item["imdb"] == "0" or "None":
                    if item["imdb"] in identifiers:
                        continue
                    else:
                        identifiers.add(item["imdb"])
                if item['url'].endswith("xml"):
                    item_type = "dir"
                else:
                    item_type = "item"
                xml += "<%s>\n" \
                       "\t<title>%s</title>\n" \
                       "\t<meta>\n" \
                       "\t<content>%s</content>\n" \
                       "\t<imdb>%s</imdb>\n" \
                       "\t<title>%s</title>\n" \
                       "\t<year>%s</year>\n" \
                       "\t</meta>\n" \
                       "\t<link>%s</link>\n" \
                       "\t<thumbnail>%s</thumbnail>\n" \
                       "\t<fanart>%s</fanart>\n" \
                       "</%s>\n\n" % (
                           item_type, item['name'], item['content'], item['imdb'], item['title'], item['year'],
                           item['url'],
                           item['poster'], item['fanart'], item_type)
        elif not item['folder']:
            if item["url"] in ["0", "#", " "]:
                continue
            if not item["imdb"] in ["0", "None"]:
                if item["imdb"] in identifiers:
                    continue
                else:
                    identifiers.add(item["imdb"])
            if not item['content'] in ['episode', 'season']:
                if item["content"] == "0" and "/tnpb/" in url:
                    continue
                if item['url'].endswith("xml"):
                    item_type = "dir"
                else:
                    item_type = "item"
                xml += "<%s>\n" \
                       "\t<title>%s</title>\n" \
                       "\t<meta>\n" \
                       "\t<content>%s</content>\n" \
                       "\t<imdb>%s</imdb>\n" \
                       "\t<title>%s</title>\n" \
                       "\t<year>%s</year>\n" \
                       "\t</meta>\n" \
                       "\t<link>%s</link>\n" \
                       "\t<thumbnail>%s</thumbnail>\n" \
                       "\t<fanart>%s</fanart>\n" \
                       "</%s>\n\n" % (
                       item_type, item['name'], item['content'], item['imdb'], item['title'], item['year'], item['url'],
                       item['poster'], item['fanart'], item_type)
    return (xml, errors)


def get_xml(url):
    cache_location = os.path.join(".", 'url_cache.db')
    try:
        if not url.startswith('http'):
            tool_path = os.getcwd()
            xml_path = os.path.join(tool_path, url)
            xml_path = os.path.normpath(xml_path)
            xml_file = open(xml_path, 'r')
            request = xml_file.read()
            xml_file.close()
        else:
            request = requests.get(url, timeout=5)
    except:
        request = None
    try:
        last_modified = request.headers['Last-Modified']
    except:
        last_modified = ""
    dbcon = database.connect(cache_location)
    dbcur = dbcon.cursor()
    try:
        dbcur.execute("SELECT * FROM version")
        match = dbcur.fetchone()
    except:
        dbcur.execute("CREATE TABLE version (""version TEXT)")
        dbcur.execute("INSERT INTO version Values ('0.0.1')")
        dbcon.commit()
    dbcur.execute(
        "CREATE TABLE IF NOT EXISTS xml (url TEXT, xml TEXT, last_modified Text, UNIQUE(url, last_modified));")
    if last_modified:
        try:
            dbcur.execute(
                "SELECT * FROM xml WHERE last_modified = '%s' and url = '%s'" % (last_modified, url))
            match = dbcur.fetchone()
            if match:
                if match[2] == last_modified:
                    return match[1]
        except:
            pass
    else:
        try:
            dbcur.execute(
                "SELECT * FROM xml WHERE url = '%s'" % (url))
            match = dbcur.fetchone()
            if match:
                return match[1]
        except:
            pass
    if not last_modified:
        last_modified = 0
    if not url.startswith('http'):
        xml = request
    else:
        xml = request.text
    xml = xml.replace("\n", "").replace("##", "").replace('\t', "")
    try:
        dbcur.execute("DELETE FROM xml WHERE url = '%s'" % (url))
    except:
        print("error deleting")
        pass
    try:
        dbcur.execute("INSERT INTO xml Values (?, ?, ?)", (url, xml.encode("utf-8", "ignore"), last_modified))
    except:
        try:
            dbcur.execute("INSERT INTO xml Values (?, ?, ?)", (url, xml.decode("utf-8"), last_modified))
        except:
            pass
    dbcon.commit()
    return xml


def main():
    config = SafeConfigParser()
    config.read('config.ini')
    
    output_path = config.get('locations', 'output_path')
    sections_path = config.get('locations', 'section_xml')

    sxml = ET.parse(sections_path)
    container = sxml.find("search_container")
    def get_title(elem):
        txt = re.sub('\[.*?]','',str(elem.findtext("title").lower()))
        return txt
    container[:] = sorted(container, key=get_title)

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    else:
        os.remove('%s/search.db' % (output_path))
    dbcon = database.connect('%s/search.db' % (output_path))
    dbcur = dbcon.cursor()
    dbcur.execute("CREATE TABLE IF NOT EXISTS search (""item TEXT, ""poster TEXT);")

    for section in container:
        global identifiers
        identifiers = set()

        title = section.findtext('title')
        url = section.findtext('url')
        filename = section.findtext('file')

        print("\t\t" + title)
        print("#####################################")
        print(url)
        xml, errors = recurse_list(url)
        file = open('%s/' % (output_path) + filename + ".xml", "wb")
        xml = "<poster>%s</poster>\n" \
              "<cache>43200</cache>\n\n" % title + xml
        file.write(xml.encode('utf-8'))
        file.close()
        content = str(xml)
        items = re.compile(
            '((?:<item>.+?</item>|<dir>.+?</dir>|<plugin>.+?</plugin>|<info>.+?</info>|'
            '<title>[^<]+</title><link>[^<]+</link><thumbnail>[^<]+</thumbnail><mode>[^<]+</mode>|'
            '<name>[^<]+</name><link>[^<]+</link><thumbnail>[^<]+</thumbnail><date>[^<]+</date>))', re.MULTILINE | re.DOTALL).findall(content)
        for item in items:
            dbcur.execute("INSERT INTO search Values (?, ?)",
                          (item, title))

    dbcon.commit()
        # if errors:
        #    file = open("d:/test/" + section['name'] + "errors.xml", "wb")
        #    file.write(repr(errors).encode('utf-8'))
        #    file.close()
    print("done generating xmls")


if __name__ == '__main__':
    main()
