"""

    Copyright (C) 2018, MuadDib

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    -------------------------------------------------------------

"""

import requests,re,json,os,urlparse
import koding
import __builtin__
import xbmc,xbmcaddon,xbmcgui
from koding import route
from resources.lib.plugin import Plugin
from resources.lib.util import dom_parser
from resources.lib.util.context import get_context_items
from resources.lib.util.xml import JenItem, JenList, display_list
from unidecode import unidecode

CACHE_TIME = 3600  # change to wanted cache time in seconds

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


@route(mode='EPorner_Cat', args=["url"])
def category_eporner(url):
    xml = ""
    try:
        url = urlparse.urljoin('https://www.eporner.com/', url)
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

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='EPorner_Stars', args=["url"])
def pornstars_eporner(url):
    xml = ""
    try:
        url = urlparse.urljoin('https://www.eporner.com/', url)
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

def remove_non_ascii(text):
    return unidecode(text)

