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

    Usage Examples:

<dir>
<title>Collection of Best Porn - Display Category content</title>
<cobp>category/squirting</sport_stream>
</dir>




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
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'

class COBP(Plugin):
    name = "cobp"

    def process_item(self, item_xml):
        if "<cobp>" in item_xml:
            item = JenItem(item_xml)
            if "http" in item.get("cobp", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "PlayVideo",
                    'url': item.get("cobp", ""),
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
            elif "category" in item.get("cobp", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "COBP",
                    'url': item.get("cobp", ""),
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


@route(mode='COBP', args=["url"])
def get_stream(url):
    xml = ""
    try:
        url = urlparse.urljoin('http://collectionofbestporn.com/', url)
        headers = {'User_Agent':User_Agent}
        html = requests.get(url,headers=headers).content
        vid_divs = dom_parser.parseDOM(html, 'div', attrs={'class':'video-item col-sm-5 col-md-4 col-xs-10'})
        count = 0
        for vid_section in vid_divs:
            thumb_div = dom_parser.parseDOM(vid_section, 'div', attrs={'class':'video-thumb'})[0]
            thumbnail = re.compile('<img src="(.+?)"',re.DOTALL).findall(str(thumb_div))[0]
            vid_page_url = re.compile('href="(.+?)"',re.DOTALL).findall(str(thumb_div))[0]

            title_div = dom_parser.parseDOM(vid_section, 'div', attrs={'class':'title'})[0]
            title = remove_non_ascii(re.compile('title="(.+?)"',re.DOTALL).findall(str(title_div))[0])
            count += 1

            xml += "<item>"\
                   "    <title>%s</title>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <cobp>%s</cobp>"\
                   "    <summary>%s</summary>"\
                   "</item>" % (title,thumbnail,vid_page_url, title)

            if count == 24:
                pagination = dom_parser.parseDOM(html, 'li', attrs={'class':'next'})[0]
                next_page = dom_parser.parseDOM(pagination, 'a', ret='href')[0]
                xml += "<dir>"\
                       "    <title>Next Page</title>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "    <cobp>%s</cobp>"\
                       "</dir>" % (addon_icon,next_page)
    except:
        pass
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='PlayVideo', args=["url"])
def play_source(url):
    try:
        headers = {'User_Agent':User_Agent}
        vid_html = requests.get(url,headers=headers).content

        sources = dom_parser.parseDOM(vid_html, 'source', ret='src')
        vid_url = sources[len(sources)-1]

        xbmc.executebuiltin("PlayMedia(%s)" % vid_url)
    except:
        return

def remove_non_ascii(text):
    return unidecode(text)

