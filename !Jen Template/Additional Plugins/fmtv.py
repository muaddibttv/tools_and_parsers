"""

    Copyright (C) 2018 MuadDib

    ----------------------------------------------------------------------------
    "THE BEER-WARE LICENSE" (Revision 42):
    @tantrumdev wrote this file.  As long as you retain this notice you can do 
    whatever you want with this stuff. Just Ask first when not released through
    the tools and parser GIT. If we meet some day, and you think this stuff is
    worth it, you can buy him a beer in return. - Muad'Dib
    ----------------------------------------------------------------------------



    Examples:
        <dir>
            <title>[COLOR yellow][ FM ][/COLOR] WWE Archive</title>
            <fullmatch>wwe_replay/1</fullmatch>
        </dir>

        <dir>
            <title>[COLOR yellow][ FM ][/COLOR] Archive</title>
            <fullmatch>nfl_replay/1</fullmatch>
        </dir>

        <dir>
            <title>[COLOR yellow][ FM ][/COLOR] Archive</title>
            <fullmatch>nba_replay/1</fullmatch>
        </dir>

        <dir>
            <title>[COLOR yellow][ FM ][/COLOR] Archive</title>
            <fullmatch>motor_replay/1</fullmatch>
        </dir>

        <dir>
            <title>[COLOR yellow][ FM ][/COLOR] Archive</title>
            <fullmatch>mlb_replay/1</fullmatch>
        </dir>

        <dir>
            <title>[COLOR yellow][ FM ][/COLOR] Archive</title>
            <fullmatch>nhl_replay/1</fullmatch>
        </dir>

"""

import requests,re,json,os,traceback,urlparse
import koding
import __builtin__
import xbmc,xbmcaddon,xbmcgui
import time
from datetime import date, datetime, timedelta
from koding import route
from resources.lib.plugin import Plugin
from resources.lib.util import dom_parser
from resources.lib.util.context import get_context_items
from resources.lib.util.xml import JenItem, JenList, display_list
from unidecode import unidecode

CACHE_TIME = 3600  # change to wanted cache time in seconds

addon_id   = xbmcaddon.Addon().getAddonInfo('id')
this_addon   = xbmcaddon.Addon(id=addon_id)
addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
addon_icon   = xbmcaddon.Addon().getAddonInfo('icon')
headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'} 

nba_info   = { 'per_page':this_addon.getSetting('nba_replay'), 'category':'3' }
nfl_info   = { 'per_page':this_addon.getSetting('nfl_replay'), 'category':'4' }
nhl_info   = { 'per_page':this_addon.getSetting('nhl_replay'), 'category':'5' }
mlb_info   = { 'per_page':this_addon.getSetting('mlb_replay'), 'category':'6' }
motor_info = { 'per_page':this_addon.getSetting('motogp_replay'), 'category':'973' }
wwe_info   = { 'per_page':this_addon.getSetting('wwe_replay'), 'category':'989' }
nhl_tonight= this_addon.getSetting('nhl_tonight')

base_full_match = 'http://fullmatchtv.com/index.php/%s'
json_cat_url    = 'wp-json/wp/v2/posts/?per_page=%s&categories=%s&page=%s'


class FullMatch_Sports(Plugin):
    name = "fullmatch_sports"

    def process_item(self, item_xml):
        if "<fullmatch>" in item_xml:
            item = JenItem(item_xml)
            if "nba_replay/" in item.get("fullmatch", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "FullMatch_NBA_Replays",
                    'url': item.get("fullmatch", ""),
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
            elif "nfl_replay/" in item.get("fullmatch", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "FullMatch_NFL_Replays",
                    'url': item.get("fullmatch", ""),
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
            elif "nhl_replay/" in item.get("fullmatch", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "FullMatch_NHL_Replays",
                    'url': item.get("fullmatch", ""),
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
            elif "mlb_replay/" in item.get("fullmatch", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "FullMatch_MLB_Replays",
                    'url': item.get("fullmatch", ""),
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
            elif "motor_replay/" in item.get("fullmatch", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "FullMatch_MOTOR_Replays",
                    'url': item.get("fullmatch", ""),
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
            elif "wwe_replay/" in item.get("fullmatch", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "FullMatch_WWE_Replays",
                    'url': item.get("fullmatch", ""),
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
            result_item["properties"] = {
                'fanart_image': result_item["fanart"]
            }
            result_item['fanart_small'] = result_item["fanart"]
            return result_item


@route(mode='FullMatch_NBA_Replays', args=["url"])
def FullMatch_NBA_Replays(url):
    url = url.replace('nba_replay/', '')
    page_id = url
    url = base_full_match % ((json_cat_url % (nba_info['per_page'], nba_info['category'], page_id))) 

    try:
        xml = ""
        response = requests.get(url,headers).json()
        try:
            if 'invalid' in response['code']:
                return
        except:
            pass
        for post in response:
            title   = clean_titles(post['title']['rendered'])
            content = post['content']['rendered']
            description = decodeEntities(re.compile('<h2>(.+?)</h2>').findall(content)[0])

            try:
                icon_js = requests.get(post['_links']['wp:featuredmedia'][0]['href'].replace('\\', ''))
                icon_js = json.loads(icon_js.text)
                icon = str(icon_js['guid']['rendered'])
            except:
                icon = addon_icon

            sources = dom_parser.parseDOM(str(content), 'iframe', ret='src')
            if len(sources) > 0:
                xml += "<item>"\
                       "    <title>%s</title>"\
                       "    <meta>"\
                       "        <summary>%s</summary>"\
                       "    </meta>"\
                       "    <link>" % (title,description)

                for source in sources:
                    if not 'http' in source:
                        source = 'http:%s' % source
                    host = urlparse.urlparse(source).netloc.capitalize()
                    xml += "        <sublink>%s(%s)</sublink>" % (source,host)

                xml += "    </link>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "</item>" % (icon)
    except:
        pass

    try:
        xml += "<dir>"\
               "    <title>Next Page >></title>"\
               "    <fullmatch>nba_replay/%s</fullmatch>"\
               "</dir>" % (str(int(page_id)+1))
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='FullMatch_NFL_Replays', args=["url"])
def FullMatch_NFL_Replays(url):
    url = url.replace('nfl_replay/', '')
    page_id = url
    url = base_full_match % ((json_cat_url % (nfl_info['per_page'], nfl_info['category'], page_id))) 

    try:
        xml = ""
        response = requests.get(url,headers).json()
        try:
            if 'invalid' in response['code']:
                return
        except:
            pass
        for post in response:
            title   = clean_titles(post['title']['rendered'])
            content = post['content']['rendered']
            description = decodeEntities(re.compile('<h2>(.+?)</h2>').findall(content)[0])

            try:
                icon_js = requests.get(post['_links']['wp:featuredmedia'][0]['href'].replace('\\', ''))
                icon_js = json.loads(icon_js.text)
                icon = str(icon_js['guid']['rendered'])
            except:
                icon = addon_icon

            sources = dom_parser.parseDOM(str(content), 'iframe', ret='src')
            if len(sources) > 0:
                xml += "<item>"\
                       "    <title>%s</title>"\
                       "    <meta>"\
                       "        <summary>%s</summary>"\
                       "    </meta>"\
                       "    <link>" % (title,description)

                for source in sources:
                    if not 'http' in source:
                        source = 'http:%s' % source
                    host = urlparse.urlparse(source).netloc.capitalize()
                    xml += "        <sublink>%s(%s)</sublink>" % (source,host)

                xml += "    </link>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "</item>" % (icon)
    except:
        pass

    try:
        xml += "<dir>"\
               "    <title>Next Page >></title>"\
               "    <fullmatch>nfl_replay/%s</fullmatch>"\
               "</dir>" % (str(int(page_id)+1))
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='FullMatch_NHL_Replays', args=["url"])
def FullMatch_NHL_Replays(url):
    url = url.replace('nhl_replay/', '')
    page_id = url
    url = base_full_match % ((json_cat_url % (nhl_info['per_page'], nhl_info['category'], page_id))) 

    try:
        xml = ""
        response = requests.get(url,headers).json()
        try:
            if 'invalid' in response['code']:
                return
        except:
            pass
        for post in response:
            title   = clean_titles(post['title']['rendered'])
            if 'true' in nhl_tonight:
                pass
            else:
                if 'nhl tonight' in title.lower():
                    continue
            content = post['content']['rendered']
            description = decodeEntities(re.compile('<h2>(.+?)</h2>').findall(content)[0])

            try:
                icon_js = requests.get(post['_links']['wp:featuredmedia'][0]['href'].replace('\\', ''))
                icon_js = json.loads(icon_js.text)
                icon = str(icon_js['guid']['rendered'])
            except:
                icon = addon_icon

            sources = dom_parser.parseDOM(str(content), 'iframe', ret='src')
            if len(sources) > 0:
                xml += "<item>"\
                       "    <title>%s</title>"\
                       "    <meta>"\
                       "        <summary>%s</summary>"\
                       "    </meta>"\
                       "    <link>" % (title,description)

                for source in sources:
                    if not 'http' in source:
                        source = 'http:%s' % source
                    host = urlparse.urlparse(source).netloc.capitalize()
                    xml += "        <sublink>%s(%s)</sublink>" % (source,host)

                xml += "    </link>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "</item>" % (icon)
    except:
        pass

    try:
        xml += "<dir>"\
               "    <title>Next Page >></title>"\
               "    <fullmatch>nhl_replay/%s</fullmatch>"\
               "</dir>" % (str(int(page_id)+1))
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='FullMatch_MLB_Replays', args=["url"])
def FullMatch_MLB_Replays(url):
    url = url.replace('mlb_replay/', '')
    page_id = url
    url = base_full_match % ((json_cat_url % (mlb_info['per_page'], mlb_info['category'], page_id))) 

    try:
        xml = ""
        response = requests.get(url,headers).json()
        try:
            if 'invalid' in response['code']:
                return
        except:
            pass
        for post in response:
            title   = clean_titles(post['title']['rendered'])
            content = post['content']['rendered']
            description = decodeEntities(re.compile('<h2>(.+?)</h2>').findall(content)[0])

            try:
                icon_js = requests.get(post['_links']['wp:featuredmedia'][0]['href'].replace('\\', ''))
                icon_js = json.loads(icon_js.text)
                icon = str(icon_js['guid']['rendered'])
            except:
                icon = addon_icon

            sources = dom_parser.parseDOM(str(content), 'iframe', ret='src')
            if len(sources) > 0:
                xml += "<item>"\
                       "    <title>%s</title>"\
                       "    <meta>"\
                       "        <summary>%s</summary>"\
                       "    </meta>"\
                       "    <link>" % (title,description)

                for source in sources:
                    if not 'http' in source:
                        source = 'http:%s' % source
                    host = urlparse.urlparse(source).netloc.capitalize()
                    xml += "        <sublink>%s(%s)</sublink>" % (source,host)

                xml += "    </link>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "</item>" % (icon)
    except:
        pass

    try:
        xml += "<dir>"\
               "    <title>Next Page >></title>"\
               "    <fullmatch>mlb_replay/%s</fullmatch>"\
               "</dir>" % (str(int(page_id)+1))
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='FullMatch_MOTOR_Replays', args=["url"])
def FullMatch_MOTOR_Replays(url):
    url = url.replace('motor_replay/', '')
    page_id = url
    url = base_full_match % ((json_cat_url % (motor_info['per_page'], motor_info['category'], page_id))) 

    try:
        xml = ""
        response = requests.get(url,headers).json()
        try:
            if 'invalid' in response['code']:
                return
        except:
            pass
        for post in response:
            title   = clean_titles(post['title']['rendered'])
            content = post['content']['rendered']
            description = decodeEntities(re.compile('<h2>(.+?)</h2>').findall(content)[0])

            try:
                icon_js = requests.get(post['_links']['wp:featuredmedia'][0]['href'].replace('\\', ''))
                icon_js = json.loads(icon_js.text)
                icon = str(icon_js['guid']['rendered'])
            except:
                icon = addon_icon

            sources = dom_parser.parseDOM(str(content), 'iframe', ret='src')
            if len(sources) > 0:
                xml += "<item>"\
                       "    <title>%s</title>"\
                       "    <meta>"\
                       "        <summary>%s</summary>"\
                       "    </meta>"\
                       "    <link>" % (title,description)

                for source in sources:
                    if not 'http' in source:
                        source = 'http:%s' % source
                    host = urlparse.urlparse(source).netloc.capitalize()
                    xml += "        <sublink>%s(%s)</sublink>" % (source,host)

                xml += "    </link>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "</item>" % (icon)
    except:
        pass

    try:
        xml += "<dir>"\
               "    <title>Next Page >></title>"\
               "    <fullmatch>motor_replay/%s</fullmatch>"\
               "</dir>" % (str(int(page_id)+1))
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='FullMatch_WWE_Replays', args=["url"])
def FullMatch_WWE_Replays(url):
    url = url.replace('wwe_replay/', '')
    page_id = url
    url = base_full_match % ((json_cat_url % (wwe_info['per_page'], wwe_info['category'], page_id))) 

    try:
        xml = ""
        response = requests.get(url,headers).json()
        try:
            if 'invalid' in response['code']:
                return
        except:
            pass
        for post in response:
            title   = clean_titles(post['title']['rendered'])
            if not 'wwe' in title.lower():
                continue
            content = post['content']['rendered']
            description = decodeEntities(re.compile('<h2>(.+?)</h2>').findall(content)[0])

            try:
                icon_js = requests.get(post['_links']['wp:featuredmedia'][0]['href'].replace('\\', ''))
                icon_js = json.loads(icon_js.text)
                icon = str(icon_js['guid']['rendered'])
            except:
                icon = addon_icon

            sources = dom_parser.parseDOM(str(content), 'iframe', ret='src')
            if len(sources) > 0:
                xml += "<item>"\
                       "    <title>%s</title>"\
                       "    <meta>"\
                       "        <summary>%s</summary>"\
                       "    </meta>"\
                       "    <link>" % (title,description)

                for source in sources:
                    if not 'http' in source:
                        source = 'http:%s' % source
                    host = urlparse.urlparse(source).netloc.capitalize()
                    xml += "        <sublink>%s(%s)</sublink>" % (source,host)

                xml += "    </link>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "</item>" % (icon)
    except:
        pass

    try:
        xml += "<dir>"\
               "    <title>Next Page >></title>"\
               "    <fullmatch>wwe_replay/%s</fullmatch>"\
               "</dir>" % (str(int(page_id)+1))
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


def clean_titles(title):
    try:
        title = remove_non_ascii(title)
        title = title.replace('&#8211;','-').replace(' at ', ' vs ')
        tmp = title.split(' - ')
        tmp_d = time.strptime(str(tmp[-1]), '%b %d, %Y')
        tmp_d = str(time.strftime("%Y-%m-%d", tmp_d))
        title = '[COLOR yellow][%s][/COLOR] %s' % (tmp_d,tmp[0])
    except:
        pass
    return str(title)


from htmlentitydefs import name2codepoint
EntityPattern = re.compile('&(?:#(\d+)|(?:#x([\da-fA-F]+))|([a-zA-Z]+));')
def decodeEntities(s, encoding='utf-8'):
    def unescape(match):
        code = match.group(1)
        if code:
            return unichr(int(code, 10))
        else:
            code = match.group(2)
            if code:
                return unichr(int(code, 16))
            else:
                code = match.group(3)
                if code in name2codepoint:
                    return unichr(name2codepoint[code])
        return match.group(0)

    if isinstance(s, str):
        s = s.decode(encoding)
    return str(EntityPattern.sub(unescape, s).encode('utf-8'))


def replaceHTMLCodes(txt):
    txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
    try:
        import html.parser as html_parser
    except:
        import HTMLParser as html_parser
    txt = html_parser.HTMLParser().unescape(txt)
    txt = html_parser.HTMLParser().unescape(txt)
    txt = txt.replace("&quot;", "\"")
    txt = txt.replace("&amp;", "&")
    txt = txt.strip()
    return txt

def replaceEscapeCodes(txt):
    try:
        import html.parser as html_parser
    except:
        import HTMLParser as html_parser
    txt = html_parser.HTMLParser().unescape(txt)
    return txt

def remove_non_ascii(text):
    try:
        text = text.decode('utf-8').replace(u'\xc2', u'A').replace(u'\xc3', u'A').replace(u'\xc4', u'A')
    except:
        pass
    return unidecode(text)

