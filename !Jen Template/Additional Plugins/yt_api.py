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
        2018.6.29:
            - Added ytdash to enable and setup Dash in YT and enable Adaptive and RTMP

    Usage Examples:

    <item>
        <title>Apply the Addon's Youtube API Keys to Kodi</title>
        <ytapi>titleforyouapigoeshere/apikeygoeshere/clientgoeshere/secretgoeshere</ytapi>
    </item>

    <item>
        <title>Activate YouTube Dash for Live and CAMS</title>
        <ytdash></ytdash>
    </item>


"""

import glob,requests,re,json,os,traceback,urlparse
import koding
import __builtin__
import xbmc,xbmcaddon,xbmcgui
from koding import route
try:    from sqlite3 import dbapi2 as database
except: from pysqlite2 import dbapi2 as database
from resources.lib.plugin import Plugin
from resources.lib.util import dom_parser
from resources.lib.util.context import get_context_items
from resources.lib.util.xml import JenItem, JenList, display_list
from datetime import datetime
from unidecode import unidecode

CACHE_TIME = 3600  # change to wanted cache time in seconds

addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
addon_icon = xbmcaddon.Addon().getAddonInfo('icon')
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'

class YTAPI(Plugin):
    name = "ytapi"

    def process_item(self, item_xml):
        if "<ytapi>" in item_xml:
            item = JenItem(item_xml)
            result_item = {
                'label': item["title"],
                'icon': item.get("thumbnail", addon_icon),
                'fanart': item.get("fanart", addon_fanart),
                'mode': "YTAPI",
                'url': item.get("ytapi", ""),
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
            result_item["properties"] = {
                'fanart_image': result_item["fanart"]
            }
            result_item['fanart_small'] = result_item["fanart"]
            return result_item
        elif "<ytdash>" in item_xml:
            item = JenItem(item_xml)
            result_item = {
                'label': item["title"],
                'icon': item.get("thumbnail", addon_icon),
                'fanart': item.get("fanart", addon_fanart),
                'mode': "YTDASH",
                'url': item.get("ytdash", ""),
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
            result_item["properties"] = {
                'fanart_image': result_item["fanart"]
            }
            result_item['fanart_small'] = result_item["fanart"]
            return result_item


@route(mode='YTAPI', args=["url"])
def apply_ytapi(url):
    xml = ""
    try:
        yt_path = xbmc.translatePath(os.path.join('special://home/addons/','plugin.video.youtube'))
        if not os.path.exists(yt_path):
            dialog = xbmcgui.Dialog()
            dialog.ok('Youtube',"[COLOR red]The Youtube Addon is not installed. Canceling API update....[/COLOR]")
            quit()
        try:
            ytapi_set = url.split('/')
            dialog = xbmcgui.Dialog()
            if dialog.yesno(ytapi_set[0], "Do you want to apply this Youtube API Key to Kodi?"):
                yt_settings = xbmcaddon.Addon(id='plugin.video.youtube')
                yt_settings.setSetting("youtube.api.enable", 'true')
                yt_settings.setSetting("youtube.api.last.switch", 'own')
                yt_settings.setSetting("youtube.api.key", ytapi_set[1])
                yt_settings.setSetting("youtube.api.id", ytapi_set[2])
                yt_settings.setSetting("youtube.api.secret", ytapi_set[3])
                dialog.ok(ytapi_set[0],"[COLOR snow]The Youtube addon has been updated.[/COLOR]")
        except:
            pass
    except:
        pass


@route(mode='YTDASH', args=["url"])
def apply_ytdash(url):
    xml = ""
    try:
        yt_path = xbmc.translatePath(os.path.join('special://home/addons/','plugin.video.youtube'))
        if not os.path.exists(yt_path):
            dialog = xbmcgui.Dialog()
            dialog.ok('Youtube',"[COLOR red]The Youtube Addon is not installed. Canceling Dash update....[/COLOR]")
            quit()
            return
        try:
            dialog = xbmcgui.Dialog()
            if dialog.yesno("Dash and CAMS", "Do you want to update your Kodi to handle YouTube Live, HD, and CAMS better?"):
                update_addon('inputstream.adaptive', 1)
                update_addon('inputstream.rtmp', 1)

                yt_settings = xbmcaddon.Addon(id='plugin.video.youtube')
                yt_settings.setSetting("kodion.video.quality.mpd", 'true')
                yt_settings.setSetting("kodion.video.support.mpd.addon", 'true')
                yt_settings.setSetting("kodion.video.quality", '4')
                yt_settings.setSetting("kodion.setup_wizard", 'false')

                xbmc.executebuiltin('UpdateAddonRepos()')
                xbmc.executebuiltin('UpdateLocalAddons()')
                xbmc.executebuiltin('Container.Refresh')

                dialog.ok("Dash and CAMS","[COLOR snow]The YouTube addon has been updated.[/COLOR]")
        except:
            failure = traceback.format_exc()
            xbmcgui.Dialog().textviewer('Exception', str(failure))
            pass
    except:
        failure = traceback.format_exc()
        xbmcgui.Dialog().textviewer('Exception', str(failure))
        pass


DATABASE = xbmc.translatePath('special://home/userdata/Database')
def latest_db(DB):
    if DB in ['Addons', 'ADSP', 'Epg', 'MyMusic', 'MyVideos', 'Textures', 'TV', 'ViewModes']:
        match = glob.glob(os.path.join(DATABASE,'%s*.db' % DB))
        comp = '%s(.+?).db' % DB[1:]
        highest = 0
        for file in match :
            try: check = int(re.compile(comp).findall(file)[0])
            except: check = 0
            if highest < check :
                highest = check
        return '%s%s.db' % (DB, highest)
    else: return False


def update_addon(addon=None, state=1):
    dbfile = latest_db('Addons')
    dbfile = os.path.join(DATABASE, dbfile)
    installedtime = str(datetime.now())[:-7]
    if os.path.exists(dbfile):
        try:
            textdb = database.connect(dbfile)
            textexe = textdb.cursor()
        except:
            failure = traceback.format_exc()
            print(str(failure))
            return False
    else: 
        return False
    if state == 2:
        try:
            textexe.execute("DELETE FROM installed WHERE addonID = ?", (addon,))
            textdb.commit()
            textexe.close()
        except:
            print("Error Removing %s from DB" % addon)
        return True
    try:
        textexe.execute("SELECT id, addonID, enabled FROM installed WHERE addonID = ?", (addon,))
        found = textexe.fetchone()
        if found == None:
            textexe.execute('INSERT INTO installed (addonID , enabled, installDate) VALUES (?,?,?)', (addon, state, installedtime,))
            print("Insert %s into db" % addon)
        else:
            tid, taddonid, tenabled = found
            textexe.execute('UPDATE installed SET enabled = ? WHERE id = ? ', (state, tid,))
            print("Updated %s in db" % addon)
        textdb.commit()
        textexe.close()
    except:
        print("Erroring enabling addon: %s" % addon)


def remove_non_ascii(text):
    return unidecode(text)

