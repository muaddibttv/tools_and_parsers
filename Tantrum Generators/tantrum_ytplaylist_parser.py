# -*- coding: UTF-8 -*-
""" Processes HTML of a YT channel's Playlists, to build a template file for all of them. """

import datetime, json, os, re, requests, sys, traceback

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

            inp = requests.get(url, headers={'User-Agent':randomagent()})
            resp = inp.json()
            playlist_count = len(resp["items"])
            playlist_worked = 1;
            for playlist in resp['items']:
                title_temp = playlist["snippet"]["localized"]["title"]
                title = title_temp
                title_temp = replaceHTMLCodes(title_temp)
                title_temp = replaceEscapeCodes(title_temp)
                title_temp = title_temp.replace(u'\xa0', u' ').replace(u'\xe4', u'a').replace(u'\xe9', u'e').replace(u'\xeb', u'e').replace(u'\xe6', u'ae').replace(u'\xfa', u'u').replace(u'\xda', u'U').replace(u'\xe7', u'c')
                title_temp = title_temp.replace(u'\xe0', u'a').replace(u'\xc9', u'E').replace(u'\xf3', u'o').replace(u'\xff', u'y').replace(u'\xe1', u'a').replace(u'\xed', u'i').replace(u'\xf1', u'n').replace(u'\xe3', u'a')
                title_temp = title_temp.lower()

                playlist_id = playlist["id"]
                try:
                    thumbnail = playlist["snippet"]["thumbnails"]["standard"]["url"]
                except:
                    thumbnail = playlist["snippet"]["thumbnails"]["default"]["url"]

                output_string = output_string + 'name="' + str(title) + '"\n'
                output_string = output_string + 'section="false"\n'
                output_string = output_string + 'search="false"\n'
                output_string = output_string + 'subid="false"\n'
                output_string = output_string + 'playlistid="' + str(playlist_id) + '"\n'
                output_string = output_string + 'channelid="false"\n'
                output_string = output_string + 'videoid="false"\n'
                output_string = output_string + 'icon="' + str(thumbnail) + '"\n'
                if not self.fanart == None:
                    output_string = output_string + 'fanart="' + str(self.fanart) + '"\n'
                else:
                    output_string = output_string + 'fanart="http://"\n'
                output_string = output_string + 'description="' + str(title) + '"\n\n'
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

def randomagent():
    import random
    BR_VERS = [
        ['%s.0' % i for i in range(18, 50)],
        ['37.0.2062.103', '37.0.2062.120', '37.0.2062.124', '38.0.2125.101', '38.0.2125.104', '38.0.2125.111', '39.0.2171.71', '39.0.2171.95', '39.0.2171.99',
         '40.0.2214.93', '40.0.2214.111',
         '40.0.2214.115', '42.0.2311.90', '42.0.2311.135', '42.0.2311.152', '43.0.2357.81', '43.0.2357.124', '44.0.2403.155', '44.0.2403.157', '45.0.2454.101',
         '45.0.2454.85', '46.0.2490.71',
         '46.0.2490.80', '46.0.2490.86', '47.0.2526.73', '47.0.2526.80', '48.0.2564.116', '49.0.2623.112', '50.0.2661.86', '51.0.2704.103', '52.0.2743.116',
         '53.0.2785.143', '54.0.2840.71', '61.0.3163.100'],
        ['11.0'],
        ['8.0', '9.0', '10.0', '10.6']]
    WIN_VERS = ['Windows NT 10.0', 'Windows NT 7.0', 'Windows NT 6.3', 'Windows NT 6.2', 'Windows NT 6.1', 'Windows NT 6.0', 'Windows NT 5.1', 'Windows NT 5.0']
    FEATURES = ['; WOW64', '; Win64; IA64', '; Win64; x64', '']
    RAND_UAS = ['Mozilla/5.0 ({win_ver}{feature}; rv:{br_ver}) Gecko/20100101 Firefox/{br_ver}',
                'Mozilla/5.0 ({win_ver}{feature}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{br_ver} Safari/537.36',
                'Mozilla/5.0 ({win_ver}{feature}; Trident/7.0; rv:{br_ver}) like Gecko',
                'Mozilla/5.0 (compatible; MSIE {br_ver}; {win_ver}{feature}; Trident/6.0)']
    index = random.randrange(len(RAND_UAS))
    return RAND_UAS[index].format(win_ver=random.choice(WIN_VERS), feature=random.choice(FEATURES), br_ver=random.choice(BR_VERS[index]))

if ( __name__ == "__main__" ):
    # start
    Generator()