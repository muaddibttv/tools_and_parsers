"""

    Copyright (C) 2018

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
    
    Changelog:
        2018-6-17
            - Initial Version

    Usage Examples:



"""

import base64,json,re,requests,os,traceback,urlparse
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
addon_icon   = xbmcaddon.Addon().getAddonInfo('icon')
User_Agent   = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'

base_main_link = 'https://www.example.com/'

class PluginTemplate(Plugin):
    name = "plugintemplate"

    def process_item(self, item_xml):
        if "<template>" in item_xml:
            item = JenItem(item_xml)
            if "category/" in item.get("template", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "Template_Category",
                    'url': item.get("template", ""),
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
            elif "displayitem/" in item.get("template", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "Template_Item",
                    'url': item.get("template", ""),
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
            }
            result_item["properties"] = {
                'fanart_image': result_item["fanart"]
            result_item['fanart_small'] = result_item["fanart"]
            return result_item


@route(mode='Template_Category', args=["url"])
def get_TemplateCategory(url):
    xml = ""
    url = url.replace('category/', '') # Strip our category tag off.
    try:
        url = urlparse.urljoin(base_main_link, url)

        html = requests.get(url).content
        sections = dom_parser.parseDOM(html, 'table', attrs={'class':'series_index'})

        for table in sections:
            try:
                the_cols = dom_parser.parseDOM(table, 'td')
                for column in the_cols:
                    if '&nbsp;' in column:
                        continue
                    show_url, title = re.compile('<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(column)[0]
                    title = refreshtitle(title)
                    title = remove_non_ascii(title)
                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <meta>"\
                           "        <summary>%s</summary>"\
                           "    </meta>"\
                           "    <template>displayitem/%s</template>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "</dir>" % (title,title,show_url,addon_icon)
            except:
                continue
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='Template_Item', args=["url"])
def show_Template_Item(url):
    xml = ""
    url = url.replace('main/', '', 1) # Strip our category tag off.
    try:
        url = urlparse.urljoin(base_main_link, url)

        html = requests.get(url).content
        sections = dom_parser.parseDOM(html, 'table', attrs={'class':'series_index'})

        for table in sections:
            try:
                the_cols = dom_parser.parseDOM(table, 'td')
                for column in the_cols:
                    if '&nbsp;' in column:
                        continue
                    show_url, title = re.compile('<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(column)[0]
                    title = refreshtitle(title)
                    title = remove_non_ascii(title)
                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <meta>"\
                           "        <summary>%s</summary>"\
                           "    </meta>"\
                           "    <link>%s</link>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "</dir>" % (title,title,show_url,addon_icon)
            except:
                continue
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


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

