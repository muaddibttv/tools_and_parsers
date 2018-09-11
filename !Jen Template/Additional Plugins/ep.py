"""

    Copyright (C) 2018 MuadDib

    ----------------------------------------------------------------------------
    "THE BEER-WARE LICENSE" (Revision 42):
    @tantrumdev wrote this file.  As long as you retain this notice you can do 
    whatever you want with this stuff. Just Ask first when not released through
    the tools and parser GIT. If we meet some day, and you think this stuff is
    worth it, you can buy him a beer in return. - Muad'Dib
    ----------------------------------------------------------------------------

    Changelog:
        2018.7.2:
            - Added Clear Cache function
            - Minor update on fetch cache returns

        2018.6.29:
            - Added caching to primary menus (Cache time is 3 hours)


    Examples:
        <dir>
            <title>[COLOR red][B]EPorner Allows 30 Views a Day[/B][/COLOR]</title>
            <heading></heading>
        </dir>

        <dir>
            <title>4k Bitches</title>
            <eporner>category/4k-porn</eporner>
        </dir>

        <dir>
            <title>HD Videos</title>
            <eporner>category/hd-1080p</eporner>
        </dir>

        <dir>
            <title>Currently Watched</title>
            <eporner>currently</eporner>
        </dir>

        <dir>
            <title>Top Rated</title>
            <eporner>top-rated</eporner>
        </dir>

        <dir>
            <title>Pornstars</title>
            <eporner>pornstars</eporner>
        </dir>

        <dir>
            <title>Search</title>
            <eporner>search</eporner>
        </dir>

        <dir>
            <title>Anal</title>
            <eporner>category/anal</eporner>
            <thumbnail>https://static-ca-cdn.eporner.com/catimg/3.jpg</thumbnail>
        </dir>

        <dir>
            <title>60 FPS</title>
            <eporner>category/60fps</eporner>
            <thumbnail>https://static-ca-cdn.eporner.com/catimg/67.jpg</thumbnail>
        </dir>

        <dir>
            <title>Teen</title>
            <eporner>category/teens</eporner>
            <thumbnail>https://static-ca-cdn.eporner.com/catimg/0.jpg</thumbnail>
        </dir>

        <dir>
            <title>Big Tits</title>
            <eporner>category/big-tits</eporner>
            <thumbnail>https://static-ca-cdn.eporner.com/catimg/25.jpg</thumbnail>
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

addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
addon_icon = xbmcaddon.Addon().getAddonInfo('icon')
next_icon = os.path.join(xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path')), 'resources', 'media', 'next.png')

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'

class EPORNER(Plugin):
    name = "eporner"

    def process_item(self, item_xml):
        if "<eporner>" in item_xml:
            item = JenItem(item_xml)
            if "http" in item.get("eporner", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "PlayEporner",
                    'url': item.get("eporner", ""),
                    'folder': False,
                    'imdb': "0",
                    'content': "files",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
            elif "category/" in item.get("eporner", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "EPorner_Cat",
                    'url': item.get("eporner", ""),
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
            elif "currently" in item.get("eporner", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "EPorner_Cat",
                    'url': item.get("eporner", ""),
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
            elif "top-rated" in item.get("eporner", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "EPorner_Cat",
                    'url': item.get("eporner", ""),
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
            elif "pornstars" in item.get("eporner", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "EPorner_Stars",
                    'url': item.get("eporner", ""),
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
            elif "pornstar" in item.get("eporner", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "EPorner_Cat",
                    'url': item.get("eporner", ""),
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
            elif "search" in item.get("eporner", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "EPorner_Search",
                    'url': item.get("eporner", ""),
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
        if dialog.yesno(xbmcaddon.Addon().getAddonInfo('name'), "Clear EPorner Plugin Cache?"):
            koding.Remove_Table("eporner_com_plugin")

@route(mode='EPorner_Cat', args=["url"])
def category_eporner(url):
    url = urlparse.urljoin('https://www.eporner.com/', url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:
            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content
            
            hdy_vid_divs = dom_parser.parseDOM(html, 'div', attrs={'class':'mb hdy'})
            for vid_section in hdy_vid_divs:
                thumbnail = re.compile('src="(.+?)"',re.DOTALL).findall(str(vid_section))[0]
                vid_page_url, title = re.compile('href="(.+?)"+\stitle="(.+?)"',re.DOTALL).findall(str(vid_section))[0]
                vid_page_url = urlparse.urljoin('https://www.eporner.com/', vid_page_url)
                xml += "<item>"\
                       "    <title>%s</title>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "    <eporner>%s</eporner>"\
                       "    <summary>%s</summary>"\
                       "</item>" % (title,thumbnail,vid_page_url, title)

            vid_divs = dom_parser.parseDOM(html, 'div', attrs={'class':'mb'})
            for vid_section in vid_divs:
                thumbnail = re.compile('src="(.+?)"',re.DOTALL).findall(str(vid_section))[0]
                vid_page_url, title = re.compile('href="(.+?)"+\stitle="(.+?)"',re.DOTALL).findall(str(vid_section))[0]
                vid_page_url = urlparse.urljoin('https://www.eporner.com/', vid_page_url)
                xml += "<item>"\
                       "    <title>%s</title>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "    <eporner>%s</eporner>"\
                       "    <summary>%s</summary>"\
                       "</item>" % (title,thumbnail,vid_page_url, title)

            try:
                next_page = dom_parser.parseDOM(html, 'a', attrs={'title':'Next page'}, ret='href')[0]
                next_page = next_page.replace('/', '', 1)
                xml += "<dir>"\
                       "    <title>Next Page</title>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "    <eporner>%s</eporner>"\
                       "</dir>" % (next_icon,next_page)
            except:
                pass
        except:
            pass

        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='EPorner_Stars', args=["url"])
def pornstars_eporner(url):
    url = urlparse.urljoin('https://www.eporner.com/', url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:
            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content
            
            profile_divs = dom_parser.parseDOM(html, 'div', attrs={'class':'mbprofile'})
            for profile in profile_divs:
                thumbnail = re.compile('src="(.+?)"',re.DOTALL).findall(str(profile))[0]
                profile_url, title = re.compile('href="(.+?)"+\stitle="(.+?)"',re.DOTALL).findall(str(profile))[0]
                #profile_url = profile_url.replace('/', '', 1)
                xml += "<dir>"\
                       "    <title>%s</title>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "    <eporner>%s</eporner>"\
                       "    <summary>%s</summary>"\
                       "</dir>" % (title,thumbnail,profile_url, title)

            try:
                next_page = dom_parser.parseDOM(html, 'a', attrs={'title':'Next page'}, ret='href')[0]
                next_page = next_page.replace('/', '', 1)
                xml += "<dir>"\
                       "    <title>Next Page</title>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "    <eporner>%s</eporner>"\
                       "</dir>" % (next_icon,next_page)
            except:
                pass
        except:
            pass

        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='EPorner_Search', args=["url"])
def category_eporner(url):
    xml = ""
    try:
        if len(url) > 6:
            search = url.replace('search', '')
        else:
            keyboard = xbmc.Keyboard('', 'Search for')
            keyboard.doModal()
            if keyboard.isConfirmed() != None and keyboard.isConfirmed() != "":
                search = keyboard.getText()
            else:
                return

            if search == None or search == "":
                xml += "<item>"\
                       "    <title>Search Cancelled</title>"\
                       "    <heading></heading>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "</item>" % (addon_icon)
                jenlist = JenList(xml)
                display_list(jenlist.get_list(), jenlist.get_content_type())
                return

        total = 0

        try:
            search_url = 'https://www.eporner.com/search/%s' % search.replace(' ', '-')
            html = requests.get(search_url).content
            results = dom_parser.parseDOM(html, 'div', attrs={'class':'mb hdy'})

            for vid_section in results:
                thumbnail = re.compile('src="(.+?)"',re.DOTALL).findall(str(vid_section))[0]
                vid_page_url, title = re.compile('href="(.+?)"+\stitle="(.+?)"',re.DOTALL).findall(str(vid_section))[0]
                vid_page_url = urlparse.urljoin('https://www.eporner.com/', vid_page_url)
                xml += "<item>"\
                       "    <title>%s</title>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "    <eporner>%s</eporner>"\
                       "    <summary>%s</summary>"\
                       "</item>" % (title,thumbnail,vid_page_url, title)
            total += 1

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'mb'})
            for vid_section in results:
                thumbnail = re.compile('src="(.+?)"',re.DOTALL).findall(str(vid_section))[0]
                vid_page_url, title = re.compile('href="(.+?)"+\stitle="(.+?)"',re.DOTALL).findall(str(vid_section))[0]
                vid_page_url = urlparse.urljoin('https://www.eporner.com/', vid_page_url)
                xml += "<item>"\
                       "    <title>%s</title>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "    <eporner>%s</eporner>"\
                       "    <summary>%s</summary>"\
                       "</item>" % (title,thumbnail,vid_page_url, title)
                total += 1
        except:
            pass

        try:
            next_page = dom_parser.parseDOM(html, 'a', attrs={'title':'Next page'}, ret='href')[0]
            next_page = next_page.replace('/', '', 1)
            xml += "<dir>"\
                   "    <title>Next Page</title>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <eporner>%s</eporner>"\
                   "</dir>" % (next_icon,next_page)
        except:
            pass
    except:
        pass

    if total > 0:
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='PlayEporner', args=["url"])
def play_eporner(url):
    try:
        headers = {'User_Agent':User_Agent}
        vid_html = requests.get(url,headers=headers).content
        download_div = dom_parser.parseDOM(vid_html, 'div', attrs={'id':'hd-porn-dload'})[0]
        sources = re.compile('href="(.+?)"',re.DOTALL).findall(str(download_div))

        names = []
        for item in sources:
            quality = item.split('/')[3] + 'p'
            names.append(quality)
        selected = xbmcgui.Dialog().select('Select Quality',names)
        if selected ==  -1:
            return        

        vid_url = urlparse.urljoin('https://www.eporner.com/', sources[selected])
        xbmc.executebuiltin("PlayMedia(%s)" % str(vid_url))
    except:
        return


def save_to_db(item, url):
    if not item or not url:
        return False
    try:
        koding.reset_db()
        koding.Remove_From_Table(
            "eporner_com_plugin",
            {
                "url": url
            })

        koding.Add_To_Table("eporner_com_plugin",
                            {
                                "url": url,
                                "item": base64.b64encode(item),
                                "created": time.time()
                            })
    except:
        return False


def fetch_from_db(url):
    koding.reset_db()
    eporner_plugin_spec = {
        "columns": {
            "url": "TEXT",
            "item": "TEXT",
            "created": "TEXT"
        },
        "constraints": {
            "unique": "url"
        }
    }
    koding.Create_Table("eporner_com_plugin", eporner_plugin_spec)
    match = koding.Get_From_Table(
        "eporner_com_plugin", {"url": url})
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


def remove_non_ascii(text):
    return unidecode(text)

