#!/usr/bin/python
# encoding=utf8
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
    <title>Latest Releases (Short List)</title>
    <wctoon>main/updates/0</wctoon>
</dir>

<dir>
    <title>Latest Releases (Full List)</title>
    <wctoon>wcdaily-updates</wctoon>
</dir>

<dir>
    <title>Popular Series (Short List)</title>
    <wctoon>main/popular_series/0</wctoon>
</dir>

<dir>
    <title>Popular Series (Full List)</title>
    <wctoon>popular-cartoon</wctoon>
</dir>

<dir>
    <title>Cartoons</title>
    <wctoon>category/cartoon</wctoon>
</dir>

<dir>
    <title>Movies</title>
    <wctoon>category/movies</wctoon>
</dir>

<dir>
    <title>Search Movies</title>
    <wctoon>wcsearch</wctoon>
</dir>

<dir>
    <title>All 101 Dalmatians Movies</title>
    <wctoon>wcsearch/101 dalmatians</wctoon>
</dir>




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


class WatchCartoon(Plugin):
    name = "wctoon"

    def process_item(self, item_xml):
        if "<wctoon>" in item_xml:
            item = JenItem(item_xml)
            if "wcepisode/" in item.get("wctoon", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "WCEpisodes",
                    'url': item.get("wctoon", ""),
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
            elif "wcsearch" in item.get("wctoon", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "WCSearch",
                    'url': item.get("wctoon", ""),
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
            elif "list-videos/" in item.get("wctoon", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "WCListVideos",
                    'url': item.get("wctoon", ""),
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
            elif "direct/" in item.get("wctoon", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "WCPlayVideo",
                    'url': item.get("wctoon", ""),
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
            elif "main/" in item.get("wctoon", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "WCMain",
                    'url': item.get("wctoon", ""),
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
            elif "popular-cartoon" in item.get("wctoon", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "WCPopular",
                    'url': item.get("wctoon", ""),
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
            elif "wcdaily-updates" in item.get("wctoon", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "WCDaily",
                    'url': item.get("wctoon", ""),
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
            elif "category/" in item.get("wctoon", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "WatchCartoon",
                    'url': item.get("wctoon", ""),
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


@route(mode='WatchCartoon', args=["url"])
def get_wcstream(url):
    xml = ""
    url = url.replace('category/', '') # Strip our category tag off.
    try:
        url = urlparse.urljoin('http://www.toonova.net/', url)

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
                           "    <wctoon>wcepisode/%s</wctoon>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (title,show_url,addon_icon,title)
            except:
                continue
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='WCMain', args=["url"])
def get_wcmainstream(subid):
    xml = ""
    subid = subid.replace('main/', '', 1) # Strip our category tag off.
    subid = subid.split('/')

    try:
        html = requests.get('http://www.toonova.net/').content
        if subid[0] == 'popular_series':
            thedivs = dom_parser.parseDOM(html, 'div', attrs={'id':subid[0]})[int(subid[1])]
            list_items = dom_parser.parseDOM(thedivs, 'li')
            for content in list_items:
                try:
                    info_div = dom_parser.parseDOM(content, 'div', attrs={'class':'slink'})[0]
                    show_url, title = re.compile('<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(info_div)[0]
                    title = refreshtitle(title).replace('Episode ', 'EP:')
                    title = remove_non_ascii(title)
                    show_icon = re.compile('src="(.+?)"',re.DOTALL).findall(content)[0]
                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <wctoon>wcepisode/%s</wctoon>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (title,show_url,show_icon,title)
                except:
                    continue
        elif subid[0] == 'updates':
            thetable = dom_parser.parseDOM(html, 'table', attrs={'id':subid[0]})[int(subid[1])]
            the_rows = dom_parser.parseDOM(thetable, 'tr')
            for content in the_rows:
                try:
                    the_lists = dom_parser.parseDOM(content, 'li')
                    for item in the_lists:
                        show_url, title = re.compile('<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(item)[0]
                        title = refreshtitle(title).replace('Episode ', 'EP:')
                        title = remove_non_ascii(title)
                        xml += "<dir>"\
                               "    <title>%s</title>"\
                               "    <wctoon>wcepisode/%s</wctoon>"\
                               "    <thumbnail>%s</thumbnail>"\
                               "    <summary>%s</summary>"\
                               "</dir>" % (title,show_url,addon_icon,title)
                except:
                    continue
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='WCPopular', args=["url"])
def get_wcpopular(url):
    xml = ""
    url = urlparse.urljoin('http://www.toonova.net/', url)

    try:
        html = requests.get(url).content
        thedivs = dom_parser.parseDOM(html, 'div', attrs={'class':'series_list'})[1]
        list_items = dom_parser.parseDOM(thedivs, 'li')
        for content in list_items:
            try:
                info_header = dom_parser.parseDOM(content, 'h3')[0]
                show_url, title = re.compile('<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(info_header)[0]
                title = refreshtitle(title).replace('Episode ', 'EP:')
                title = remove_non_ascii(title)
                show_icon = re.compile('src="(.+?)"',re.DOTALL).findall(content)[0]
                xml += "<dir>"\
                       "    <title>%s</title>"\
                       "    <wctoon>wcepisode/%s</wctoon>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "    <summary>%s</summary>"\
                       "</dir>" % (title,show_url,show_icon,title)
            except:
                continue

        pagination = dom_parser.parseDOM(html, 'ul', attrs={'class':'pagination'})[0]
        if len(pagination) > 0:
            list_items = dom_parser.parseDOM(pagination, 'li')
            next_li = list_items[(len(list_items)-1)]
            next_url = 'popular-cartoon/%s' % (re.compile('href="http://www.toonova.net/popular-cartoon/(.+?)"',re.DOTALL).findall(next_li)[0])
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <wctoon>%s</wctoon>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page</summary>"\
                   "</dir>" % (next_url,show_icon)
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='WCDaily', args=["url"])
def get_wcdaily(url):
    xml = ""
    url = url.replace('wcdaily-', '') # Strip our episode tag off.
    url = urlparse.urljoin('http://www.toonova.net/', url)
    try:
        html = requests.get(url).content
        thetable = dom_parser.parseDOM(html, 'table', attrs={'id':'updates'})[0]
        the_rows = dom_parser.parseDOM(thetable, 'tr')
        for content in the_rows:
            try:
                the_lists = dom_parser.parseDOM(content, 'li')
                for item in the_lists:
                    show_url, title = re.compile('<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(item)[0]
                    title = refreshtitle(title).replace('Episode ', 'EP:')
                    title = remove_non_ascii(title)
                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <wctoon>wcepisode/%s</wctoon>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (title,show_url,addon_icon,title)
            except:
                continue

        pagination = dom_parser.parseDOM(html, 'ul', attrs={'class':'pagination'})[0]
        if len(pagination) > 0:
            list_items = dom_parser.parseDOM(pagination, 'li')
            next_li = list_items[(len(list_items)-1)]
            next_url = 'wcdaily-updates/%s' % (re.compile('href="http://www.toonova.net/updates/(.+?)"',re.DOTALL).findall(next_li)[0])
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <wctoon>%s</wctoon>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page</summary>"\
                   "</dir>" % (next_url,addon_icon)
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='WCEpisodes', args=["url"])
def get_wcepisodes(url):
    xml = ""
    url = url.replace('wcepisode/', '') # Strip our episode tag off.

    try:
        url = urlparse.urljoin('http://www.toonova.net/', url)

        html = requests.get(url).content
        thediv = dom_parser.parseDOM(html, 'div', attrs={'id':'videos'})[0]
        lists = dom_parser.parseDOM(thediv, 'li')

        for entry in lists:
            show_url, title = re.compile('<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(entry)[0]
            title = refreshtitle(title).replace('Episode ', 'EP:')
            title = remove_non_ascii(title)
            show_icon = dom_parser.parseDOM(html, 'div', attrs={'id':'series_info'})[0]
            show_icon = re.compile('src="(.+?)"',re.DOTALL).findall(show_icon)[0]
            xml += "<item>"\
                   "    <title>%s</title>"\
                   "    <wctoon>list-videos/%s</wctoon>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>%s</summary>"\
                   "</item>" % (title,show_url,show_icon,title)
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='WCSearch', args=["url"])
def get_wcsearch(url):
    xml = ""
    url = url.replace('wcsearch/', '') # Strip our search tag off when used with keywords in the xml
    url = url.replace('wcsearch', '') # Catch plain case, for when overall search is used.

    if url != None and url != "":
        search = url
    else:
        keyboard = xbmc.Keyboard('', 'Search for Movies')
        keyboard.doModal()
        if keyboard.isConfirmed() != None and keyboard.isConfirmed() != "":
            search = keyboard.getText()
        else:
            return

    if search == None or search == "":
        xml += "<item>"\
               "    <title>Search Cancelled</title>"\
               "    <link>plugin://plugin.video.squadcontrol/?mode=section_item</link>"\
               "    <thumbnail>%s</thumbnail>"\
               "</item>" % (addon_icon)
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type())
        return

    total = 0

    try:
        search_url = 'http://www.toonova.net/toon/search?key=%s' % search.replace(' ', '+')
        html = requests.get(search_url).content
        thedivs = dom_parser.parseDOM(html, 'div', attrs={'class':'series_list'})[0]
        list_items = dom_parser.parseDOM(thedivs, 'li')
        for content in list_items:
            try:
                info_header = dom_parser.parseDOM(content, 'h3')[0]
                show_url, title = re.compile('<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(info_header)[0]
                title = refreshtitle(title).replace('Episode ', 'EP:')
                title = remove_non_ascii(title)
                show_icon = re.compile('src="(.+?)"',re.DOTALL).findall(content)[0]
                xml += "<dir>"\
                       "    <title>%s</title>"\
                       "    <wctoon>wcepisode/%s</wctoon>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "    <summary>%s</summary>"\
                       "</dir>" % (title,show_url,show_icon,title)
                total += 1
            except:
                continue

        pagination = dom_parser.parseDOM(html, 'ul', attrs={'class':'pagination'})[0]
        if len(pagination) > 0:
            list_items = dom_parser.parseDOM(pagination, 'li')
            next_li = list_items[(len(list_items)-1)]
            next_url = 'popular-cartoon/%s' % (re.compile('href="http://www.toonova.net/popular-cartoon/(.+?)"',re.DOTALL).findall(next_li)[0])
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <wctoon>%s</wctoon>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page</summary>"\
                   "</dir>" % (next_url,show_icon)
    except:
        pass

    if total > 0:
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='WCListVideos', args=["url"])
def get_wclistvideos(url):
    xml = ""
    url = url.replace('list-videos/', '') # Strip our episode tag off.
    try:
        html = requests.get(url).content
        the_divs = dom_parser.parseDOM(html, 'div', attrs={'class':'vmargin'})
        for video_entry in the_divs:
            iframe = re.compile('iframe src="(.+?)"',re.DOTALL).findall(video_entry)[0]

            html = requests.get(iframe)
            url = re.findall(r'''file:\s*['\"]([^'\"]+)['\"](?:\,\s*label:\s*|)(?:['\"]|)([\d]+|)''', html.text)
            if len(url) == 1:
                host = url[0][0].split('//')[1].replace('www.','')
                host = host.split('/')[0].split('.')[1].upper() 
                xml += "<item>"\
                       "    <title>%s</title>"\
                       "    <wctoon>direct/%s</wctoon>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "    <summary>%s</summary>"\
                       "</item>" % (host,str(url[0][0]),addon_icon,host)
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())

@route(mode='WCPlayVideo', args=["url"])
def get_wcplayvideo(url):
    url = url.replace('direct/', '') # Strip our episode tag off.
    try:
        xbmc.executebuiltin("PlayMedia(%s)" % (url))
        quit()
        return
    except:
        pass

def refreshtitle(title):
    title = replaceEscapeCodes(title)
    title = replaceHTMLCodes(title).replace('English Dubbed','[COLOR yellow](English Dubbed)[/COLOR]').replace('English Subbed','[COLOR orange](English Subbed)[/COLOR]')
    return title

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

