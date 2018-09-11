#!/usr/bin/python
# encoding=utf8
"""

    Copyright (C) 2018 MuadDib

    ----------------------------------------------------------------------------
    "THE BEER-WARE LICENSE - JEN EDITION":
    @tantrumdev wrote this file.  As long as you retain this notice you can do 
    whatever you want with this stuff. Just Ask first when not released through
    the tools and parser GIT. If we meet some day, and you think this stuff is
    worth it, you can buy him a beer in return. - Muad'Dib
    ----------------------------------------------------------------------------


    Examples:
        Examples are in the zip file thearchives.zip, located in my git

"""

import json,re,requests,os,traceback,urlparse
import koding
import __builtin__
import xbmc,xbmcaddon,xbmcgui
from koding import route
from resources.lib.plugin import Plugin
from resources.lib.util import dom_parser
from resources.lib.util.context import get_context_items
from resources.lib.util.xml import JenItem, JenList, display_list
from unidecode import unidecode

CACHE_TIME = 86400  # change to wanted cache time in seconds, 24 hours = 86400

addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
addon_icon   = xbmcaddon.Addon().getAddonInfo('icon')
User_Agent   = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'

archive_links = { 'vod':'https://archive.org/details/moviesandfilms', 'vodshort':'https://archive.org/details/',
                    'ab':'https://archive.org/details/librivoxaudio/', 'abshort':'https://archive.org/details/',
                    'lm':'https://archive.org/details/etree/', 'lmshort':'https://archive.org/details/' }

class TheArchives(Plugin):
    name = "thearchives"

    def process_item(self, item_xml):
        if "<archives>" in item_xml:
            item = JenItem(item_xml)
            if "vodyear/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHVODYear",
                    'url': item.get("archives", ""),
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
            elif "abyear/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHABYear",
                    'url': item.get("archives", ""),
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
            elif "lmyear/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHLMYear",
                    'url': item.get("archives", ""),
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
            elif "vodsubject/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHVODSubject",
                    'url': item.get("archives", ""),
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
            elif "absubject/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHABSubject",
                    'url': item.get("archives", ""),
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
            elif "lmsubject/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHLMSubject",
                    'url': item.get("archives", ""),
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
            elif "vodcollection/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHVODCollection",
                    'url': item.get("archives", ""),
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
            elif "abcollection/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHABCollection",
                    'url': item.get("archives", ""),
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
            elif "lmcollection/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHLMCollection",
                    'url': item.get("archives", ""),
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
            elif "vodlang/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHVODLang",
                    'url': item.get("archives", ""),
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
            elif "abauthor/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHABAuthor",
                    'url': item.get("archives", ""),
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
            elif "vodmovie/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHVODMovie",
                    'url': item.get("archives", ""),
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
            elif "lmtrack/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHLMTrack",
                    'url': item.get("archives", ""),
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
            elif "abbook/" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHABBook",
                    'url': item.get("archives", ""),
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
            elif "search_title_vod" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHVODSearch",
                    'url': item.get("archives", ""),
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
            elif "search_title_ab" in item.get("archives", "") or "search_author_ab" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHABSearch",
                    'url': item.get("archives", ""),
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
            elif "search_title_lm" in item.get("archives", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "ARCHLMSearch",
                    'url': item.get("archives", ""),
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
            try:
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item
            except:
                return

    def clear_cache(self):
        dialog = xbmcgui.Dialog()
        if dialog.yesno(xbmcaddon.Addon().getAddonInfo('name'), "Clear The Archives Plugin Cache?"):
            koding.Remove_Table("thearchives_plugin")


@route(mode='ARCHVODYear', args=["url"])
def get_archvodyear(url):
    orig_url = url
    url = url.replace('vodyear/', '') # Strip our category tag off.
    sdate, page = url.split('/')
    url = '?and[]=year:"%s"&sort=-publicdate&page=%s' % (sdate,page)
    url = urlparse.urljoin(archive_links['vod'], url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:
            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
            vod_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
            cnt = 0
            for entry in vod_list:
                cnt += 1
                try:
                    vod_url, vod_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                    try:
                        entry = " ".join(entry.split()).replace('\n','')
                        vod_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                        vod_icon = urlparse.urljoin('https://archive.org/', vod_icon)
                    except:
                        vod_icon = addon_icon
                    vod_title = remove_non_ascii(vod_title)
                    vod_title = replaceHTMLCodes(vod_title)
                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <archives>vodmovie/%s</archives>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (vod_title,vod_url,vod_icon,vod_title)
                except:
                    continue
        except:
            pass

        if cnt == 75:
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <archives>vodmovie/%s/%s</archives>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page >></summary>"\
                   "</dir>" % (sdate,str(int(page)+1),addon_icon)
        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHABYear', args=["url"])
def get_archabyear(url):
    orig_url = url
    url = url.replace('abyear/', '') # Strip our category tag off.
    sdate, page = url.split('/')
    url = '?and[]=year:"%s"&sort=-date&page=%s' % (sdate,page)
    url = urlparse.urljoin(archive_links['ab'], url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:
            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
            book_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
            cnt = 0
            for entry in book_list:
                cnt += 1
                try:
                    book_url, book_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                    try:
                        entry = " ".join(entry.split()).replace('\n','')
                        book_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                        book_icon = urlparse.urljoin('https://archive.org/', book_icon)
                    except:
                        book_icon = addon_icon
                    book_title = remove_non_ascii(book_title)
                    book_title = replaceHTMLCodes(book_title)
                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <archives>abbook/%s</archives>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (book_title,book_url,book_icon,book_title)
                except:
                    continue
        except:
            pass

        if cnt == 75:
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <archives>abyear/%s/%s</archives>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page >></summary>"\
                   "</dir>" % (sdate,str(int(page)+1),addon_icon)

        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHLMYear', args=["url"])
def get_archlmyear(url):
    orig_url = url
    url = url.replace('lmyear/', '') # Strip our category tag off.
    sdate, page = url.split('/')
    url = '?and[]=year:"%s"&sort=-date&page=%s' % (sdate,page)
    url = urlparse.urljoin(archive_links['lm'], url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:
            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
            track_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
            cnt = 0
            for entry in track_list:
                cnt += 1
                try:
                    track_url, track_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                    try:
                        entry = " ".join(entry.split()).replace('\n','')
                        track_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                        track_icon = urlparse.urljoin('https://archive.org/', track_icon)
                    except:
                        track_icon = addon_icon
                    track_title = remove_non_ascii(track_title)
                    track_title = replaceHTMLCodes(track_title)
                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <archives>lmtrack/%s</archives>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (track_title,track_url,track_icon,track_title)
                except:
                    continue
        except:
            pass

        if cnt == 75:
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <archives>lmyear/%s/%s</archives>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page >></summary>"\
                   "</dir>" % (sdate,str(int(page)+1),addon_icon)

        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHVODSubject', args=["url"])
def get_archvodsubject(url):
    orig_url = url
    url = url.replace('vodsubject/', '') # Strip our category tag off.
    subject, page = url.split('/')
    subject = subject.replace(' ','+')
    url = '?and[]=subject:"%s"&sort=-publicdate&page=%s' % (subject,page)
    url = urlparse.urljoin(archive_links['vod'], url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:
            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
            vod_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
            cnt = 0
            for entry in vod_list:
                cnt += 1
                try:
                    vod_url, vod_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                    try:
                        entry = " ".join(entry.split()).replace('\n','')
                        vod_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                        vod_icon = urlparse.urljoin('https://archive.org/', vod_icon)
                    except:
                        vod_icon = addon_icon
                    vod_title = remove_non_ascii(vod_title)
                    vod_title = replaceHTMLCodes(vod_title)
                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <archives>vodmovie/%s</archives>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (vod_title,vod_url,vod_icon,vod_title)
                except:
                    continue
        except:
            pass

        if cnt == 75:
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <archives>vodsubject/%s/%s</archives>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page >></summary>"\
                   "</dir>" % (subject,str(int(page)+1),addon_icon)

        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHABSubject', args=["url"])
def get_archabsubject(url):
    orig_url = url
    url = url.replace('absubject/', '') # Strip our category tag off.
    subject, page = url.split('/')
    subject = subject.replace(' ','+')
    url = '?and[]=subject:"%s"&sort=-date&page=%s' % (subject,page)
    url = urlparse.urljoin(archive_links['ab'], url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:

            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
            book_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
            cnt = 0
            for entry in book_list:
                cnt += 1
                try:
                    book_url, book_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                    try:
                        entry = " ".join(entry.split()).replace('\n','')
                        book_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                        book_icon = urlparse.urljoin('https://archive.org/', book_icon)
                    except:
                        book_icon = addon_icon
                    book_title = remove_non_ascii(book_title)
                    book_title = replaceHTMLCodes(book_title)
                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <archives>abbook/%s</archives>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (book_title,book_url,book_icon,book_title)
                except:
                    continue
        except:
            pass

        if cnt == 75:
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <archives>absubject/%s/%s</archives>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page >></summary>"\
                   "</dir>" % (subject,str(int(page)+1),addon_icon)

        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHLMSubject', args=["url"])
def get_archlmsubject(url):
    orig_url = url
    url = url.replace('lmsubject/', '') # Strip our category tag off.
    subject, page = url.split('/')
    subject = subject.replace(' ','+')
    url = '?and[]=subject:"%s"&sort=-date&page=%s' % (subject,page)
    url = urlparse.urljoin(archive_links['lm'], url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:

            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
            track_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
            cnt = 0
            for entry in track_list:
                cnt += 1
                try:
                    track_url, track_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                    try:
                        entry = " ".join(entry.split()).replace('\n','')
                        track_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                        track_icon = urlparse.urljoin('https://archive.org/', track_icon)
                    except:
                        track_icon = addon_icon
                    track_title = remove_non_ascii(track_title)
                    track_title = replaceHTMLCodes(track_title)
                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <archives>lmtrack/%s</archives>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (track_title,track_url,track_icon,track_title)
                except:
                    continue
        except:
            pass

        if cnt == 75:
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <archives>lmsubject/%s/%s</archives>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page >></summary>"\
                   "</dir>" % (subject,str(int(page)+1),addon_icon)

        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHVODCollection', args=["url"])
def get_archvodcollection(url):
    orig_url = url
    url = url.replace('vodcollection/', '') # Strip our category tag off.
    collection, page = url.split('/')
    collection = collection.replace(' ','-')
    url = '?and[]=collection:"%s"&sort=-publicdate&page=%s' % (collection,page)
    url = urlparse.urljoin(archive_links['vod'], url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:
            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
            book_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
            cnt = 0
            for entry in book_list:
                cnt += 1
                try:
                    book_url, book_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                    try:
                        entry = " ".join(entry.split()).replace('\n','')
                        book_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                        book_icon = urlparse.urljoin('https://archive.org/', book_icon)
                    except:
                        book_icon = addon_icon
                    book_title = remove_non_ascii(book_title)
                    book_title = replaceHTMLCodes(book_title)
                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <archives>vodmovie/%s</archives>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (book_title,book_url,book_icon,book_title)
                except:
                    continue
        except:
            pass

        if cnt == 75:
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <archives>vodcollection/%s/%s</archives>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page >></summary>"\
                   "</dir>" % (collection,str(int(page)+1),addon_icon)

        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHABCollection', args=["url"])
def get_archabcollection(url):
    orig_url = url
    url = url.replace('abcollection/', '') # Strip our category tag off.
    collection, page = url.split('/')
    collection = collection.replace(' ','-')
    url = '?and[]=collection:"%s"&sort=-date&page=%s' % (collection,page)
    url = urlparse.urljoin(archive_links['ab'], url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:
            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
            book_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
            cnt = 0
            for entry in book_list:
                cnt += 1
                try:
                    book_url, book_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                    try:
                        entry = " ".join(entry.split()).replace('\n','')
                        book_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                        book_icon = urlparse.urljoin('https://archive.org/', book_icon)
                    except:
                        book_icon = addon_icon
                    book_title = remove_non_ascii(book_title)
                    book_title = replaceHTMLCodes(book_title)

                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <archives>abbook/%s</archives>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (book_title,book_url,book_icon,book_title)
                except:
                    continue
        except:
            pass

        if cnt == 75:
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <archives>abcollection/%s/%s</archives>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page >></summary>"\
                   "</dir>" % (collection,str(int(page)+1),addon_icon)

        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHLMCollection', args=["url"])
def get_archlmcollection(url):
    orig_url = url
    url = url.replace('lmcollection/', '') # Strip our category tag off.
    collection, page = url.split('/')
    collection = collection.replace(' ','-')
    url = '?and[]=collection:"%s"&sort=-date&page=%s' % (collection,page)
    url = urlparse.urljoin(archive_links['lm'], url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:
            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
            track_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
            cnt = 0
            for entry in track_list:
                cnt += 1
                try:
                    track_url, track_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                    try:
                        entry = " ".join(entry.split()).replace('\n','')
                        track_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                        track_icon = urlparse.urljoin('https://archive.org/', track_icon)
                    except:
                        track_icon = addon_icon
                    track_title = remove_non_ascii(track_title)
                    track_title = replaceHTMLCodes(track_title)

                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <archives>lmtrack/%s</archives>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (track_title,track_url,track_icon,track_title)
                except:
                    continue
        except:
            pass

        if cnt == 75:
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <archives>lmcollection/%s/%s</archives>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page >></summary>"\
                   "</dir>" % (collection,str(int(page)+1),addon_icon)

        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHABAuthor', args=["url"])
def get_archabauthor(url):
    orig_url = url
    url = url.replace('abauthor/', '') # Strip our category tag off.
    creator, page = url.split('/')
    creator = creator.replace(' ','+')
    url = '?and[]=creator:"%s"&sort=-date&page=%s' % (creator,page)
    url = urlparse.urljoin(archive_links['ab'], url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:
            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
            book_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
            cnt = 0
            for entry in book_list:
                cnt += 1
                try:
                    book_url, book_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                    try:
                        entry = " ".join(entry.split()).replace('\n','')
                        book_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                        book_icon = urlparse.urljoin('https://archive.org/', book_icon)
                    except:
                        book_icon = addon_icon
                    book_title = remove_non_ascii(book_title)
                    book_title = replaceHTMLCodes(book_title)
                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <archives>abbook/%s</archives>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (book_title,book_url,book_icon,book_title)
                except:
                    continue
        except:
            pass

        if cnt == 75:
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <archives>abauthor/%s/%s</archives>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page >></summary>"\
                   "</dir>" % (creator,str(int(page)+1),addon_icon)

        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHVODLang', args=["url"])
def get_archvodlang(url):
    orig_url = url
    url = url.replace('vodlang/', '') # Strip our category tag off.
    the_lang, page = url.split('/')
    the_lang = the_lang.replace(' ','+')
    url = '?and[]=languageSorter:"%s"&sort=-publicdate&page=%s' % (the_lang,page)
    url = urlparse.urljoin(archive_links['vod'], url)

    xml = fetch_from_db(url)
    if not xml:
        xml = ""
        try:
            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
            book_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
            cnt = 0
            for entry in book_list:
                cnt += 1
                try:
                    book_url, book_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                    try:
                        entry = " ".join(entry.split()).replace('\n','')
                        book_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                        book_icon = urlparse.urljoin('https://archive.org/', book_icon)
                    except:
                        book_icon = addon_icon
                    book_title = remove_non_ascii(book_title)
                    book_title = replaceHTMLCodes(book_title)
                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <archives>vodmovie/%s</archives>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (book_title,book_url,book_icon,book_title)
                except:
                    continue
        except:
            pass

        if cnt == 75:
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <archives>vodlang/%s/%s</archives>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "    <summary>Next Page >></summary>"\
                   "</dir>" % (the_lang,str(int(page)+1),addon_icon)

        save_to_db(xml, url)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHVODSearch', args=["url"])
def get_archvodsearch(search_type):
    search_type = search_type.replace('search_title_vod/', '') # Strip our search tag off when used with keywords in the xml
    search_type = search_type.replace('search_title_vod', '') # Catch plain case, for when overall search is used.

    if search_type != None and search_type != "":
        search = search_type
    else:
        keyboard = xbmc.Keyboard('', 'Search for')
        keyboard.doModal()
        if keyboard.isConfirmed() != None and keyboard.isConfirmed() != "":
            search = keyboard.getText()
        else:
            return

    xml = ""
    if search == None or search == "":
        xml += "<item>"\
               "    <title>Search Canceled</title>"\
               "    <link>file://main.xml</link>"\
               "    <thumbnail>%s</thumbnail>"\
               "</item>" % (addon_icon)
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type())
        return

    total = 0

    try:
        url = '?and[]=%s&sin=&sort=titleSorter' % (search.replace(' ', '+'))
        url = urlparse.urljoin(archive_links['vod'], url)
        headers = {'User_Agent':User_Agent}
        html = requests.get(url,headers=headers).content

        results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
        video_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
        cnt = 0
        for entry in video_list:
            cnt += 1
            try:
                book_url, book_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                try:
                    entry = " ".join(entry.split()).replace('\n','')
                    book_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                    book_icon = urlparse.urljoin('https://archive.org/', book_icon)
                except:
                    book_icon = addon_icon
                book_title = remove_non_ascii(book_title)

                xml += "<item>"\
                       "    <title>%s</title>"\
                       "    <archives>vodmovie/%s</archives>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "    <summary>%s</summary>"\
                       "</item>" % (book_title,book_url,book_icon,book_title)
                total += 1
            except:
                continue
    except:
        pass

    if total > 0:
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHABSearch', args=["url"])
def get_archabsearch(search_type):
    if 'author' in search_type:
        search_type = search_type.replace('search_author_ab/', '') # Strip our search tag off when used with keywords in the xml
        search_type = search_type.replace('search_author_ab', '') # Catch plain case, for when overall search is used.
    else:
        search_type = search_type.replace('search_title_ab/', '') # Strip our search tag off when used with keywords in the xml
        search_type = search_type.replace('search_title_ab', '') # Catch plain case, for when overall search is used.

    if search_type != None and search_type != "":
        search = search_type
    else:
        keyboard = xbmc.Keyboard('', 'Search for')
        keyboard.doModal()
        if keyboard.isConfirmed() != None and keyboard.isConfirmed() != "":
            search = keyboard.getText()
        else:
            return

    xml = ""
    if search == None or search == "":
        xml += "<item>"\
               "    <title>Search Canceled</title>"\
               "    <link>file://main.xml</link>"\
               "    <thumbnail>%s</thumbnail>"\
               "</item>" % (addon_icon)
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type())
        return

    total = 0

    try:
        if 'author' in search_type:
            url = '?and[]=creator:"%s"&sort=-date' % (search.replace(' ', '+'))
            url = urlparse.urljoin(archive_links['ab'], url)
            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
            book_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
            cnt = 0
            for entry in book_list:
                cnt += 1
                try:
                    book_url, book_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                    try:
                        entry = " ".join(entry.split()).replace('\n','')
                        book_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                        book_icon = urlparse.urljoin('https://archive.org/', book_icon)
                    except:
                        book_icon = addon_icon
                    book_title = remove_non_ascii(book_title)

                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <archives>abbook/%s</archives>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (book_title,book_url,book_icon,book_title)
                    total += 1
                except:
                    continue
        else:
            url = '?and[]=%s&sin=&sort=titleSorter' % (search.replace(' ', '+'))
            url = urlparse.urljoin(archive_links['ab'], url)
            headers = {'User_Agent':User_Agent}
            html = requests.get(url,headers=headers).content

            results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
            book_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
            cnt = 0
            for entry in book_list:
                cnt += 1
                try:
                    book_url, book_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                    try:
                        entry = " ".join(entry.split()).replace('\n','')
                        book_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                        book_icon = urlparse.urljoin('https://archive.org/', book_icon)
                    except:
                        book_icon = addon_icon
                    book_title = remove_non_ascii(book_title)

                    xml += "<dir>"\
                           "    <title>%s</title>"\
                           "    <archives>abbook/%s</archives>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "    <summary>%s</summary>"\
                           "</dir>" % (book_title,book_url,book_icon,book_title)
                    total += 1
                except:
                    continue
    except:
        pass

    if total > 0:
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHLMSearch', args=["url"])
def get_archlmsearch(search_type):
    search_type = search_type.replace('search_title_lm/', '') # Strip our search tag off when used with keywords in the xml
    search_type = search_type.replace('search_title_lm', '') # Catch plain case, for when overall search is used.

    if search_type != None and search_type != "":
        search = search_type
    else:
        keyboard = xbmc.Keyboard('', 'Search for')
        keyboard.doModal()
        if keyboard.isConfirmed() != None and keyboard.isConfirmed() != "":
            search = keyboard.getText()
        else:
            return

    xml = ""
    if search == None or search == "":
        xml += "<item>"\
               "    <title>Search Canceled</title>"\
               "    <link>file://main.xml</link>"\
               "    <thumbnail>%s</thumbnail>"\
               "</item>" % (addon_icon)
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type())
        return

    total = 0

    try:
        url = '?and[]=%s&sin=&sort=titleSorter' % (search.replace(' ', '+'))
        url = urlparse.urljoin(archive_links['lm'], url)
        headers = {'User_Agent':User_Agent}
        html = requests.get(url,headers=headers).content

        results = dom_parser.parseDOM(html, 'div', attrs={'class':'results'})[0]
        video_list = dom_parser.parseDOM(results, 'div', attrs={'class':'item-ia'})
        cnt = 0
        for entry in video_list:
            cnt += 1
            try:
                track_url, track_title = re.compile('a href="(.+?)" title="(.+?)"').findall(entry)[0]
                try:
                    entry = " ".join(entry.split()).replace('\n','')
                    track_icon = re.compile('img class="item-img " source="(.+?)"').findall(entry)[0]
                    track_icon = urlparse.urljoin('https://archive.org/', track_icon)
                except:
                    track_icon = addon_icon
                track_title = remove_non_ascii(track_title)

                xml += "<item>"\
                       "    <title>%s</title>"\
                       "    <archives>lmtrack/%s</archives>"\
                       "    <thumbnail>%s</thumbnail>"\
                       "    <summary>%s</summary>"\
                       "</item>" % (track_title,track_url,track_icon,track_title)
                total += 1
            except:
                continue
    except:
        pass

    if total > 0:
        jenlist = JenList(xml)
        display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHVODMovie', args=["url"])
def get_archvodmovie(url):
    url = url.replace('vodmovie/', '') # Strip our category tag off.
    url = urlparse.urljoin(archive_links['vodshort'], url)

    xml = ""
    try:
        headers = {'User_Agent':User_Agent}
        html = requests.get(url,headers=headers).content
        groups = dom_parser.parseDOM(html, 'div', attrs={'class':'format-group'})
        mpeg2 = ""; mpeg4 = ""; avi = ""; ogg = ""
        for video_list in groups:
            try:
                if 'MPEG2' in video_list:
                    part_url = re.compile('href="(.+?)"').findall(video_list)[0]
                    mpeg2 = urlparse.urljoin('https://archive.org/', part_url)
                elif 'MPEG4' in video_list and not '512kb' in video_list:
                    part_url = re.compile('href="(.+?)"').findall(video_list)[0]
                    mpeg4 = urlparse.urljoin('https://archive.org/', part_url)
                elif 'CINEPACK' in video_list:
                    part_url = re.compile('href="(.+?)"').findall(video_list)[0]
                    avi = urlparse.urljoin('https://archive.org/', part_url)
                elif 'OGG' in video_list:
                    part_url = re.compile('href="(.+?)"').findall(video_list)[0]
                    ogg = urlparse.urljoin('https://archive.org/', part_url)
            except:
                continue

        names = []
        if len(mpeg2) > 0:
            names.append('MPEG2')
        if len(mpeg4) > 0:
            names.append('MPEG4')
        if len(avi) > 0:
            names.append('CINEPACK')
        if len(ogg) > 0:
            names.append('OGG')

        selected = xbmcgui.Dialog().select('Select Video Format',names)
        if selected ==  -1:
            return
        selected_item = names[selected]
        if 'MPEG2' in selected_item:
            xbmc.executebuiltin("PlayMedia(%s)" % (mpeg2))
        elif 'MPEG4' in selected_item:
            xbmc.executebuiltin("PlayMedia(%s)" % (mpeg4))
        elif 'CINEPACK' in selected_item:
            xbmc.executebuiltin("PlayMedia(%s)" % (avi))
        elif 'OGG' in selected_item:
            xbmc.executebuiltin("PlayMedia(%s)" % (ogg))
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHABBook', args=["url"])
def get_archabbook(url):
    url = url.replace('abbook/', '') # Strip our category tag off.
    url = urlparse.urljoin(archive_links['abshort'], url)

    xml = ""
    try:
        headers = {'User_Agent':User_Agent}
        html = requests.get(url,headers=headers).content
        book_icon = re.compile('og:image" content="(.+?)"').findall(html)[0]
        groups = dom_parser.parseDOM(html, 'div', attrs={'class':'format-group'})
        xml_128 = ""; xml_64 = ""
        for audio_list in groups:
            try:
                if 'formats=128KBPS MP3' in audio_list or 'formats=64KBPS MP3' in audio_list:
                    list = dom_parser.parseDOM(audio_list, 'div', attrs={'class':'format-file'})
                    for item in list:
                        part_url, title = re.compile('href="(.+?)">\s(.+?)<span').findall(item)[0]
                        part_url = urlparse.urljoin('https://archive.org/', part_url)
                        title = title.strip()
                        if 'formats=128KBPS MP3' in audio_list:
                            title = title + " (128kb)"
                            xml_128 += "<item>"\
                                   "    <title>%s</title>"\
                                   "    <link>%s</link>"\
                                   "    <thumbnail>%s</thumbnail>"\
                                   "    <summary>%s</summary>"\
                                   "</item>" % (title,part_url,book_icon,title)
                        else:
                            title = title + " (64kb)"
                            xml_64 += "<item>"\
                                   "    <title>%s</title>"\
                                   "    <link>%s</link>"\
                                   "    <thumbnail>%s</thumbnail>"\
                                   "    <summary>%s</summary>"\
                                   "</item>" % (title,part_url,book_icon,title)
            except:
                continue

        names = []
        if len(xml_64) > 0:
            names.append('64kb Audio')
        if len(xml_128) > 0:
            names.append('128kb Audio')

        selected = xbmcgui.Dialog().select('Select Audio Format',names)
        if selected ==  -1:
            return
        selected_item = names[selected]
        if '64' in selected_item:
            xml = xml_64
        elif '128' in selected_item:
            xml = xml_128
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='ARCHLMTrack', args=["url"])
def get_archlmtrack(url):
    url = url.replace('lmtrack/', '') # Strip our category tag off.
    url = urlparse.urljoin(archive_links['lmshort'], url)

    xml = ""
    try:
        headers = {'User_Agent':User_Agent}
        html = requests.get(url,headers=headers).content
        track_icon = re.compile('og:image" content="(.+?)"').findall(html)[0]
        groups = dom_parser.parseDOM(html, 'div', attrs={'class':'format-group'})
        xml_ogg = ""; xml_vbr = ""; xml_flac = ""; xml_flac24 = ""; xml_wave = ""
        for audio_list in groups:
            try:
                if 'formats=OGG' in audio_list:
                    list = dom_parser.parseDOM(audio_list, 'div', attrs={'class':'format-file'})
                    for item in list:
                        part_url, title = re.compile('href="(.+?)">\s(.+?)<span').findall(item)[0]
                        part_url = urlparse.urljoin('https://archive.org/', part_url)
                        title = title.strip()
                        title = title + " (OGG Vorbis)"
                        xml_ogg += "<item>"\
                               "    <title>%s</title>"\
                               "    <link>%s</link>"\
                               "    <thumbnail>%s</thumbnail>"\
                               "    <summary>%s</summary>"\
                               "</item>" % (title,part_url,track_icon,title)
                elif 'formats=VBR MP3' in audio_list:
                    list = dom_parser.parseDOM(audio_list, 'div', attrs={'class':'format-file'})
                    for item in list:
                        part_url, title = re.compile('href="(.+?)">\s(.+?)<span').findall(item)[0]
                        part_url = urlparse.urljoin('https://archive.org/', part_url)
                        title = title.strip()
                        title = title + " (VBR MP3)"
                        xml_vbr += "<item>"\
                               "    <title>%s</title>"\
                               "    <link>%s</link>"\
                               "    <thumbnail>%s</thumbnail>"\
                               "    <summary>%s</summary>"\
                               "</item>" % (title,part_url,track_icon,title)
                elif 'formats=WAVE' in audio_list:
                    list = dom_parser.parseDOM(audio_list, 'div', attrs={'class':'format-file'})
                    for item in list:
                        part_url, title = re.compile('href="(.+?)">\s(.+?)<span').findall(item)[0]
                        part_url = urlparse.urljoin('https://archive.org/', part_url)
                        title = title.strip()
                        title = title + " (WAVE)"
                        xml_wave += "<item>"\
                               "    <title>%s</title>"\
                               "    <link>%s</link>"\
                               "    <thumbnail>%s</thumbnail>"\
                               "    <summary>%s</summary>"\
                               "</item>" % (title,part_url,track_icon,title)
                elif 'formats=24BIT FLAC' in audio_list:
                    list = dom_parser.parseDOM(audio_list, 'div', attrs={'class':'format-file'})
                    for item in list:
                        part_url, title = re.compile('href="(.+?)">\s(.+?)\s<span').findall(item)[0]
                        part_url = urlparse.urljoin('https://archive.org/', part_url)
                        title = title.strip()
                        title = title + " (FLAC)"
                        xml_flac24 += "<item>"\
                               "    <title>%s</title>"\
                               "    <link>%s</link>"\
                               "    <thumbnail>%s</thumbnail>"\
                               "    <summary>%s</summary>"\
                               "</item>" % (title,part_url,track_icon,title)
                elif 'formats=FLAC' in audio_list:
                    list = dom_parser.parseDOM(audio_list, 'div', attrs={'class':'format-file'})
                    for item in list:
                        part_url, title = re.compile('href="(.+?)">\s(.+?)\s<span').findall(item)[0]
                        part_url = urlparse.urljoin('https://archive.org/', part_url)
                        title = title.strip()
                        title = title + " (FLAC)"
                        xml_flac += "<item>"\
                               "    <title>%s</title>"\
                               "    <link>%s</link>"\
                               "    <thumbnail>%s</thumbnail>"\
                               "    <summary>%s</summary>"\
                               "</item>" % (title,part_url,track_icon,title)
            except:
                continue

        names = []
        if len(xml_wave) > 0:
            names.append('WAVE Audio')
        if len(xml_ogg) > 0:
            names.append('OGG Vorbis Audio')
        if len(xml_vbr) > 0:
            names.append('VBR MP3 Audio')
        if len(xml_flac) > 0:
            names.append('FLAC Audio')
        if len(xml_flac24) > 0:
            names.append('FLAC 24Bit Audio')

        selected = xbmcgui.Dialog().select('Select Audio Format',names)
        if selected ==  -1:
            return
        selected_item = names[selected]
        if 'OGG' in selected_item:
            xml = xml_ogg
        elif 'VBR MP3' in selected_item:
            xml = xml_vbr
        elif 'WAVE' in selected_item:
            xml = xml_wave
        elif 'FLAC Audio' in selected_item:
            xml = xml_flac
        elif 'FLAC 24' in selected_item:
            xml = xml_flac24
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


def save_to_db(item, url):
    if not item or not url:
        return False
    try:
        koding.reset_db()
        koding.Remove_From_Table(
            "thearchives_plugin",
            {
                "url": url
            })

        koding.Add_To_Table("thearchives_plugin",
                            {
                                "url": url,
                                "item": base64.b64encode(item),
                                "created": time.time()
                            })
    except:
        return False


def fetch_from_db(url):
    koding.reset_db()
    thearchives_plugin_spec = {
        "columns": {
            "url": "TEXT",
            "item": "TEXT",
            "created": "TEXT"
        },
        "constraints": {
            "unique": "url"
        }
    }
    koding.Create_Table("thearchives_plugin", thearchives_plugin_spec)
    match = koding.Get_From_Table(
        "thearchives_plugin", {"url": url})
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

