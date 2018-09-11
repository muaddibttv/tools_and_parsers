#!/usr/bin/python
# encoding=utf8
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

        2018.6.21:
            - Added caching to primary menus (Cache time is 3 hours)

    Usage Examples:

    <dir>
        <title>HD Videos</title>
        <cobp>tag/hd-porn/newest</cobp>
    </dir>

    <dir>
        <title>Most Popular</title>
        <cobp>most-viewed</cobp>
    </dir>

    <dir>
        <title>Most Recent</title>
        <cobp>most-recent</cobp>
    </dir>

    <dir>
        <title>Amateur</title>
        <cobp>category/amateur</cobp>
    </dir>

    <dir>
        <title>Anal</title>
        <cobp>category/anal</cobp>
    </dir>

    <dir>
        <title>Asian</title>
        <cobp>category/asian</cobp>
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
            elif "category/" in item.get("cobp", ""):
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
            elif "tag/" in item.get("cobp", ""):
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
            elif "most-" in item.get("cobp", ""):
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

    def clear_cache(self):
        dialog = xbmcgui.Dialog()
        if dialog.yesno(xbmcaddon.Addon().getAddonInfo('name'), "Clear COBP Plugin Cache?"):
            koding.Remove_Table("cobp_com_plugin")


@route(mode='COBP', args=["url"])
def get_stream(url):
    url = urlparse.urljoin('http://collectionofbestporn.com/', url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:
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
                       "    <meta>"\
                       "        <summary>%s</summary>"\
                       "    </meta>"\
                       "    <cobp>%s</cobp>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "</item>" % (title,title,vid_page_url,thumbnail)

            try:
                pagination = dom_parser.parseDOM(html, 'li', attrs={'class':'next'})[0]
                next_page = dom_parser.parseDOM(pagination, 'a', ret='href')[0]
                xml += "<dir>"\
                       "    <title>Next Page</title>"\
                       "    <meta>"\
                       "        <summary>Click here for more porn bitches!</summary>"\
                       "    </meta>"\
                       "    <cobp>%s</cobp>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "</dir>" % (next_page,next_icon)
            except:
                pass
            save_to_db(xml, url)
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


def save_to_db(item, url):
    if not item or not url:
        return False
    try:
        koding.reset_db()
        koding.Remove_From_Table(
            "cobp_com_plugin",
            {
                "url": url
            })

        koding.Add_To_Table("cobp_com_plugin",
                            {
                                "url": url,
                                "item": base64.b64encode(item),
                                "created": time.time()
                            })
    except:
        return False


def fetch_from_db(url):
    koding.reset_db()
    cobp_plugin_spec = {
        "columns": {
            "url": "TEXT",
            "item": "TEXT",
            "created": "TEXT"
        },
        "constraints": {
            "unique": "url"
        }
    }
    koding.Create_Table("cobp_com_plugin", cobp_plugin_spec)
    match = koding.Get_From_Table(
        "cobp_com_plugin", {"url": url})
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

