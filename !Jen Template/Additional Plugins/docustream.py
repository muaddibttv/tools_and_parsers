"""

    Copyright (C) 2018 MuadDib

    ----------------------------------------------------------------------------
    "THE BEER-WARE LICENSE" (Revision 42):
    @tantrumdev wrote this file.  As long as you retain this notice you can do 
    whatever you want with this stuff. Just Ask first when not released through
    the tools and parser GIT. If we meet some day, and you think this stuff is
    worth it, you can buy him a beer in return. - Muad'Dib
    ----------------------------------------------------------------------------


    Overview:

        Drop this PY in the plugins folder. See examples below on use.

    Version:
        2018.7.2:
            - Added Clear Cache function
            - Minor update on fetch cache returns

        2018.6.29:
            - Added caching to primary menus (Cache time is 3 hours)

        2018.5.31
            - Initial Release


    XML Explanations:
        Tags: 
            <docus></docus> - Displays the entry as category's contents


    Usage Examples:

        <dir>
            <title>911</title>
            <docus>dscategory/911</docus>
        </dir>

        <dir>
            <title>Activist</title>
            <docus>dscategory/activist</docus>
        </dir>

        <dir>
            <title>Archaeology</title>
            <docus>dscategory/archaeology</docus>
        </dir>

        <dir>
            <title>Art and Artists</title>
            <docus>dscategory/art-and-artists</docus>
        </dir>

        <dir>
            <title>Atheism</title>
            <docus>dscategory/atheism</docus>
        </dir>

        <dir>
            <title>Biographies</title>
            <docus>dscategory/biographies</docus>
        </dir>

        <dir>
            <title>Business</title>
            <docus>dscategory/business</docus>
        </dir>

        <dir>
            <title>Celebrity</title>
            <docus>dscategory/celebrity</docus>
        </dir>

        <dir>
            <title>Crime</title>
            <docus>dscategory/crime</docus>
        </dir>

        <dir>
            <title>Conference</title>
            <docus>dscategory/conference</docus>
        </dir>

        <dir>
            <title>Conspiracy</title>
            <docus>dscategory/conspiracy</docus>
        </dir>

        <dir>
            <title>Countries</title>
            <docus>dscategory/countries</docus>
        </dir>

        <dir>
            <title>Drugs</title>
            <docus>dscategory/drugs</docus>
        </dir>

        <dir>
            <title>Economics</title>
            <docus>dscategory/economics</docus>
        </dir>

        <dir>
            <title>Educational</title>
            <docus>dscategory/educational</docus>
        </dir>

        <dir>
            <title>Environment</title>
            <docus>dscategory/environment</docus>
        </dir>

        <dir>
            <title>Evolution</title>
            <docus>dscategory/evolution</docus>
        </dir>

        <dir>
            <title>Gangs</title>
            <docus>dscategory/gangs</docus>
        </dir>

        <dir>
            <title>Health</title>
            <docus>dscategory/health</docus>
        </dir>

        <dir>
            <title>History</title>
            <docus>dscategory/history</docus>
        </dir>

        <dir>
            <title>Human Rights</title>
            <docus>dscategory/human-rights</docus>
        </dir>

        <dir>
            <title>Lifestyle</title>
            <docus>dscategory/lifestyle</docus>
        </dir>

        <dir>
            <title>Movies</title>
            <docus>dscategory/movies</docus>
        </dir>

        <dir>
            <title>Music</title>
            <docus>dscategory/music</docus>
        </dir>

        <dir>
            <title>Mystery</title>
            <docus>dscategory/mystery</docus>
        </dir>

        <dir>
            <title>Nature</title>
            <docus>dscategory/nature</docus>
        </dir>

        <dir>
            <title>News and Politics</title>
            <docus>dscategory/news-politics</docus>
        </dir>

        <dir>
            <title>Performing Arts</title>
            <docus>dscategory/performing-arts</docus>
        </dir>

        <dir>
            <title>Philosophy</title>
            <docus>dscategory/philosophy</docus>
        </dir>

        <dir>
            <title>Preview Only</title>
            <docus>dscategory/preview-only</docus>
        </dir>

        <dir>
            <title>Psychology</title>
            <docus>dscategory/psychology</docus>
        </dir>

        <dir>
            <title>Religion</title>
            <docus>dscategory/religion</docus>
        </dir>

        <dir>
            <title>Science</title>
            <docus>dscategory/science</docus>
        </dir>

        <dir>
            <title>Society</title>
            <docus>dscategory/society</docus>
        </dir>

        <dir>
            <title>Space</title>
            <docus>dscategory/space</docus>
        </dir>

        <dir>
            <title>Spiritual</title>
            <docus>dscategory/spiritual</docus>
        </dir>

        <dir>
            <title>Sport and Adventure</title>
            <docus>dscategory/sportadventure</docus>
        </dir>

        <dir>
            <title>Technology</title>
            <docus>dscategory/technology</docus>
        </dir>

        <dir>
            <title>War</title>
            <docus>dscategory/war</docus>
        </dir>



"""

import __builtin__
import base64,time
import json,re,requests,os,traceback,urlparse
import koding
import xbmc,xbmcaddon,xbmcgui
from koding import route
from resources.lib.plugin import Plugin
from resources.lib.util import dom_parser
from resources.lib.util.context import get_context_items
from resources.lib.util.xml import JenItem, JenList, display_list
from unidecode import unidecode

CACHE_TIME = 10800  # change to wanted cache time in seconds

addon_id = xbmcaddon.Addon().getAddonInfo('id')
addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
addon_icon   = xbmcaddon.Addon().getAddonInfo('icon')
headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

docu_link = 'https://documentarystorm.com/'
docu_cat_list = 'https://documentarystorm.com/category/'

"""
Add strings to the reg_items for domains that are supported naturally by resolveurl
"""
reg_items = {'vimeo','dailymotion','pbs.org','rutube','vid.ag','vidzi.tv','rt.com'}
unreg_items = {'myspace','nfb.ca','thevideobee','dotsub','en.musicplayon.com','vkontakte.ru','veehd.com','snagfilms','liveleak.com','imdb.com','disclose.tv','videoweed.es','putlocker','vid.ag','vice.com'}
"""
Examples for unreg_items, to look into future support or if requested to fix by adding to/fixing in resolveurl



"""

class DocuStreams(Plugin):
    name = "docus"
    priority = 200

    def process_item(self, item_xml):
        if "<docus>" in item_xml:
            item = JenItem(item_xml)
            if "dscategory/" in item.get("docus", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "DSCats",
                    'url': item.get("docus", ""),
                    'folder': True,
                    'imdb': "0",
                    'content': "files",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
            result_item['fanart_small'] = result_item["fanart"]
            return result_item

    def clear_cache(self):
        dialog = xbmcgui.Dialog()
        if dialog.yesno(xbmcaddon.Addon().getAddonInfo('name'), "Clear Documentary Storm Plugin Cache?"):
            koding.Remove_Table("docustorm_com_plugin")

def get_category_id(category_name):
    json_url = 'https://documentarystorm.com/wp-json/wp/v2/categories?per_page=100&page=1&search=%s' % category_name
    json_html = requests.get(json_url,headers=headers).content
    lists = re.compile('"id":(.+?),"count":(.+?),"description".+?"name":"(.+?)","slug":"(.+?)"',re.DOTALL).findall(json_html)
    for id,total,title,slug in lists:
        if slug.lower() == category_name.lower():
            return str(id)


@route(mode='DSCats', args=["url"])
def get_DScats(url):
    url = url.replace('dscategory/', '') # Strip our category tag off.
    orig_cat = url.split("/")[0]
    try:
        npage =url.split("/")[2]
    except:
        npage = 1

    cat_id = get_category_id(orig_cat)
    json_url = 'https://documentarystorm.com/wp-json/wp/v2/posts?per_page=50&page=%s&order=asc&categories=%s' % (npage, cat_id)

    xml = fetch_from_db(json_url)
    if not xml:
        xml = ""
        try:
            html = requests.get(json_url,headers=headers).content
            doc_list = re.compile('"id":(.+?),"date".+?"link":"(.+?)","title".+?"rendered":"(.+?)"',re.DOTALL).findall(html)
            count = 0
            for post_id,docu_url,docu_title in doc_list:
                count += 1
                try:
                    docu_url = docu_url.replace('\\','')

                    docu_html = requests.get(docu_url,headers=headers).content
                    try:
                        docu_item = dom_parser.parseDOM(docu_html, 'meta', attrs={'itemprop':'embedUrl'}, ret='content')[0]
                    except:
                        docu_item = None

                    if docu_item == None:
                        try:
                            docu_item = dom_parser.parseDOM(docu_html, 'iframe', ret='src')[0]
                        except:
                            continue

                    if 'http:' not in docu_item and  'https:' not in docu_item:
                        docu_item = 'https:' + docu_item
                    docu_url = docu_item

                    replaceHTMLCodes(docu_title)

                    if 'rt.com' in docu_url:
                        res_html = requests.get(docu_url,headers=headers).content
                        pattern_file = r"""file: '(.*?)'"""
                        r = re.search(pattern_file, res_html)
                        if r:
                            file = r.group(1)
                            docu_url = file.replace('cdnv.rt.com', 'rtd.rt.com')

                    docu_summary = re.compile('meta name="description" content="(.+?)"',re.DOTALL).findall(docu_html)[0]
                    try:
                        docu_icon = re.compile('property="og:image" content="(.+?)"',re.DOTALL).findall(docu_html)[0]
                    except:
                        docu_icon = re.compile('itemprop="thumbnailUrl" content="(.+?)"',re.DOTALL).findall(docu_html)[0]

                    if 'youtube' in docu_url:
                        if 'videoseries' not in docu_url:
                            xml += "<item>"\
                                   "    <title>%s</title>"\
                                   "    <link>%s</link>"\
                                   "    <thumbnail>%s</thumbnail>"\
                                   "    <summary>%s</summary>"\
                                   "</item>" % (docu_title,docu_url,docu_icon,docu_summary)
                        else:
                            # videoseries stuff?
                            video_id = docu_url.split("=")[-1]
                            docu_url = 'plugin://plugin.video.youtube/playlist/%s/' % video_id
                            xml += "<item>"\
                                   "    <title>%s</title>"\
                                   "    <link>%s</link>"\
                                   "    <thumbnail>%s</thumbnail>"\
                                   "    <summary>%s</summary>"\
                                   "</item>" % (docu_title,docu_url,docu_icon,docu_summary)
                    elif 'archive.org/embed' in docu_url:
                        docu_html = requests.get(docu_url,headers=headers).content
                        video_element = dom_parser.parseDOM(docu_html, 'source', ret='src')[0]
                        docu_url = urlparse.urljoin('https://archive.org/', video_element)
                        xml += "<item>"\
                               "    <title>%s</title>"\
                               "    <link>%s</link>"\
                               "    <thumbnail>%s</thumbnail>"\
                               "    <summary>%s</summary>"\
                               "</item>" % (docu_title,docu_url,docu_icon,docu_summary)
                    elif any(x in docu_url for x in reg_items):
                        xml += "<item>"\
                               "    <title>%s</title>"\
                               "    <link>%s</link>"\
                               "    <thumbnail>%s</thumbnail>"\
                               "    <summary>%s</summary>"\
                               "</item>" % (docu_title,docu_url,docu_icon,docu_summary)
                    elif any(x in docu_url for x in unreg_items):
                        # most of these gone now so screw it lol, and no valid player know yet to work with nfb
                        continue
                    else:
                        xbmcgui.Dialog().ok('Unknown Host - ' + docu_title,str(docu_url)) 
                except:
                    continue

            try:
                if count == 50:
                    xml += "<dir>"\
                           "    <title>Next Page >></title>"\
                           "    <docus>dscategory/%s/page/%s</docus>"\
                           "</dir>" % (orig_cat,str((int(npage)+1)))
            except:
                pass
        except:
            pass

        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


def save_to_db(item, url):
    if not item or not url:
        return False
    try:
        koding.reset_db()
        koding.Remove_From_Table(
            "docustorm_com_plugin",
            {
                "url": url
            })

        koding.Add_To_Table("docustorm_com_plugin",
                            {
                                "url": url,
                                "item": base64.b64encode(item),
                                "created": time.time()
                            })
    except:
        return False


def fetch_from_db(url):
    koding.reset_db()
    docustorm_plugin_spec = {
        "columns": {
            "url": "TEXT",
            "item": "TEXT",
            "created": "TEXT"
        },
        "constraints": {
            "unique": "url"
        }
    }
    koding.Create_Table("docustorm_com_plugin", docustorm_plugin_spec)
    match = koding.Get_From_Table(
        "docustorm_com_plugin", {"url": url})
    if match:
        match = match[0]
        if not match["item"]:
            return None
        created_time = match["created"]
        if created_time and float(created_time) + CACHE_TIME >= time.time():
            match_item = match["item"]
            try:
                result = base64.b64decode(match_item)
            except:
                return None
            return result
        else:
            return None
    else:
        return None


def replaceHTMLCodes(txt):
    txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
    txt = txt.replace("&quot;", "\"").replace("&amp;", "&")
    txt = txt.replace('&#8216;','\'').replace('&#8217;','\'').replace('&#038;','&').replace('&#8230;','....')
    txt = txt.strip()
    return txt


def remove_non_ascii(text):
    try:
        text = text.decode('utf-8').replace(u'\xc2', u'A').replace(u'\xc3', u'A').replace(u'\xc4', u'A')
    except:
        pass
    return unidecode(text)
