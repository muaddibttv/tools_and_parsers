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

    Usage:
        Set the current_version to a number higher than existing (if any) 'update_ver'
            setting in your addon. If this is the first time using this, you can leave
            current_version at 1.
        When the service runs, it checks if the current_version below is greater than 
            the 'update_ver' setting. If it is, it updates the settings for your addon 
            in userdata to the updated entries you entered below.
        If it is not greater (meaning, current same as updated_ver) then it just ignores

        If you want to let the end user know you updated something, set the 
            "enable_notification" to True, otherwise set it to False


"""

import xbmc,xbmcaddon,xbmcgui


addon_id   = xbmcaddon.Addon().getAddonInfo('id')
addon_name = xbmcaddon.Addon().getAddonInfo('name')
addon_icon = xbmcaddon.Addon().getAddonInfo('icon')
ownAddon   = xbmcaddon.Addon(id=addon_id)

#######################################################################
# My New Settings
current_version             = '1' # increase this when you want the service to update the below settings
enable_notification         = True
updated_root_xml            = 'file://main.xml'
updated_tvdb_api_key        = ''
updated_tmdb_api_key        = ''
updated_trakt_api_id        = ''
updated_trakt_api_secret    = ''
updated_TRAKT_ACCESS_TOKEN  = ''
updated_TRAKT_EXPIRES_AT    = ''
updated_TRAKT_REFRESH_TOKEN = ''
updated_lastfm_api_key      = ''
updated_lastfm_secret       = ''
updated_search_db_location  = ''
#######################################################################

def main():
    class enableAll():
        def __init__(self):
            self.current_root_xml            = ownAddon.getSetting('root_xml')
            self.current_tvdb_api_key        = ownAddon.getSetting('tvdb_api_key')
            self.current_tmdb_api_key        = ownAddon.getSetting('tmdb_api_key')
            self.current_trakt_api_id        = ownAddon.getSetting('trakt_api_client_id')
            self.current_trakt_api_secret    = ownAddon.getSetting('trakt_api_client_secret')
            self.current_TRAKT_ACCESS_TOKEN  = ownAddon.getSetting('TRAKT_ACCESS_TOKEN')
            self.current_TRAKT_EXPIRES_AT    = ownAddon.getSetting('TRAKT_EXPIRES_AT')
            self.current_TRAKT_REFRESH_TOKEN = ownAddon.getSetting('TRAKT_REFRESH_TOKEN')
            self.current_lastfm_api_key      = ownAddon.getSetting('lastfm_api_key')
            self.current_lastfm_secret       = ownAddon.getSetting('lastfm_secret')
            self.current_search_db_location  = ownAddon.getSetting('search_db_location')


    try:
        update_version = ownAddon.getSetting('update_ver')
        if update_version == "":
            update_version = '0'
        if int(current_version) > int(update_version):
            ownAddon.setSetting('root_xml', updated_root_xml)
            ownAddon.setSetting('tvdb_api_key', updated_tvdb_api_key)
            ownAddon.setSetting('tmdb_api_key', updated_tmdb_api_key)
            ownAddon.setSetting('trakt_api_client_id', updated_trakt_api_id)
            ownAddon.setSetting('trakt_api_client_secret', updated_trakt_api_secret)
            ownAddon.setSetting('TRAKT_ACCESS_TOKEN', '')
            ownAddon.setSetting('TRAKT_EXPIRES_AT', '')
            ownAddon.setSetting('TRAKT_REFRESH_TOKEN', '')
            ownAddon.setSetting('lastfm_api_key', updated_lastfm_api_key)
            ownAddon.setSetting('lastfm_secret', updated_lastfm_secret)
            ownAddon.setSetting('search_db_location', updated_search_db_location)

            ownAddon.setSetting('update_ver', current_version)

            if enable_notification:
                xbmcgui.Dialog().notification(addon_name, 'Updated API keys', addon_icon)
        else:
            pass
    except:
        pass


if __name__ == '__main__':
    main()