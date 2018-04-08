# -*- coding: UTF-8 -*-
""" Processes HTML of a YT channel's Playlists, to build a template file for all of them. """

import datetime, json, urllib, os, re, sys, traceback, unicodedata
from unidecode import unidecode

YOUTUBE_API_KEY = "AIzaSyA4ktCh7tLBk467AYgPMykgdtMZ8HL68hE"
RESULTS_PER_PAGE = '40' # 1-50 as per Google's rules.

class Generator:
    def __init__( self ):
        # create initial variables needed later
        self.base_search_url = 'https://www.googleapis.com/youtube/v3/playlists?'
        self.tools_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__))))

        # CHANGEME to match the path needed for your generic fanart to add to each entry. Set to None to not set it.
        # Example: self.fanart = None
        self.fanart = None

        # CHANGEME to match the channel ID you want to pull
        self.channel = 'UC3OFPTgSjbex5P4TcL_XINA'
        # generate files
        self._generate_yt_templates()

        # notify user
        print('Finished parsing the Youtube Channel. Output saved as playlists.txt')

    def _generate_yt_templates ( self ):

        print('Contacting Youtube API.....')

        first_url = self.base_search_url+'key={}&order=date&maxResults={}'.format(YOUTUBE_API_KEY, RESULTS_PER_PAGE)
        try:
            output_string = ''

            total_results = 0
            cycle = 0
            url = first_url + '&channelId='+self.channel+'&part=id,snippet,contentDetails'

            inp = urllib.urlopen(url)
            resp = json.load(inp)
            playlist_count = len(resp["items"])
            playlist_worked = 1;
            for playlist in resp['items']:
                title_temp = playlist["snippet"]["localized"]["title"]
                title = title_temp
                title_temp = replaceHTMLCodes(title_temp)
                title_temp = unidecode(u'%s' % title_temp)
                title_temp = replaceEscapeCodes(title_temp)
                title_temp = title_temp.replace(u'\xa0', u' ').replace(u'\xe4', u'a').replace(u'\xe9', u'e').replace(u'\xeb', u'e').replace(u'\xe6', u'ae').replace(u'\xfa', u'u').replace(u'\xda', u'U').replace(u'\xe7', u'c')
                title_temp = title_temp.replace(u'\xe0', u'a').replace(u'\xc9', u'E').replace(u'\xf3', u'o').replace(u'\xff', u'y').replace(u'\xe1', u'a').replace(u'\xed', u'i').replace(u'\xf1', u'n').replace(u'\xe3', u'a')
                title_temp = title_temp.lower()

                playlist_id = playlist["id"]
                try:
                    thumbnail = playlist["snippet"]["thumbnails"]["standard"]["url"]
                except:
                    thumbnail = playlist["snippet"]["thumbnails"]["default"]["url"]

                output_string = output_string + '<plugin>\n'
                output_string = output_string + '    <title>' + str(title) + '</title>\n'
                output_string = output_string + '    <link>plugin://plugin.video.youtube/playlist/' + str(playlist_id) + '/</link>\n'
                output_string = output_string + '    <thumbnail>' + str(thumbnail) + '</thumbnail>\n'
                if not self.fanart == None:
                    output_string = output_string + '    <fanart>' + str(self.fanart) + '</fanart>\n'
                output_string = output_string + '</plugin>\n\n'
        except:
            failure = traceback.format_exc()
            print('Youtube Playlist Parser - Exception: \n' + str(failure))

        # save file
        with open('playlists.txt','w') as f:
            f.write(output_string)

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

if ( __name__ == "__main__" ):
    # start
    Generator()