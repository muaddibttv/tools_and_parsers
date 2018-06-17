# -*- coding: UTF-8 -*-
""" Processes HTML of a YT channel's videos, to build a template file for all of them. """

import datetime, json, os, re, requests, sys, traceback

YOUTUBE_API_KEY = "AIzaSyA4ktCh7tLBk467AYgPMykgdtMZ8HL68hE"
RESULTS_PER_PAGE = '40' # 1-50 as per Google's rules.

class Generator:
    def __init__( self ):
        # create initial variables needed later
        self.base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
        self.tools_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__))))

        # CHANGEME to match the path needed for your generic fanart to add to each entry. Set to None to not set it.
        # Example: self.fanart = None
        self.fanart = None

        # CHANGEME to match the playlist ID you want to pull
        self.channelId = 'UCXB9905ejCSMh3f7-WjDDRQ'
        # generate files
        self._generate_yt_templates()

        # notify user
        print('Finished parsing the YouTube Channel. Output saved as channel_videos.xml')

    def _generate_yt_templates ( self ):

        print('Contacting YouTube API.....')

        try:
            output_string = self.get_all_video_in_channel()
        except:
            failure = traceback.format_exc()
            print('Youtube Playlist Parser - Exception: \n' + str(failure))

        # save file
        with open('wmhd.xml','w') as f:
            f.write(output_string)


    def get_all_video_in_channel(self):
        first_url = self.base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults={}'.format(YOUTUBE_API_KEY, self.channelId, RESULTS_PER_PAGE)

        output_string = ''

        total_results = 0
        cycle = 0
        url = first_url

        while True:
            inp = requests.get(url, headers={'User-Agent':randomagent()})
            resp = inp.json()
            for video_item in resp['items']:
                if not video_item['id']['kind'] == "youtube#video":
                    continue

                title_temp = video_item["snippet"]["title"]
                desc = video_item["snippet"]["description"].encode('ascii',errors='ignore')
                title_temp = replaceHTMLCodes(title_temp)
                title_temp = replaceEscapeCodes(title_temp)
                title_temp = title_temp.replace(u'\xa0', u' ').replace(u'\xa9', u'').replace(u'\xe4', u'a').replace(u'\xe9', u'e').replace(u'\xeb', u'e').replace(u'\xe6', u'ae').replace(u'\xfa', u'u').replace(u'\xda', u'U').replace(u'\xe7', u'c')
                title_temp = title_temp.replace(u'\xe0', u'a').replace(u'\xc9', u'E').replace(u'\xf3', u'o').replace(u'\xff', u'y').replace(u'\xe1', u'a').replace(u'\xed', u'i').replace(u'\xf1', u'n').replace(u'\xe3', u'a')
                title_temp = title_temp.encode('ascii',errors='ignore').lower()
                title = title_temp

                video_id = video_item['id']['videoId']
                try:
                    thumbnail = video_item["snippet"]["thumbnails"]["standard"]["url"]
                except:
                    thumbnail = video_item["snippet"]["thumbnails"]["default"]["url"]

                output_string = output_string + '<item>\n'
                output_string = output_string + '    <title>' + str(title) + '</title>\n'
                output_string = output_string + '    <meta>\n'
                output_string = output_string + '        <summary>' + str(desc) + ' </summary>\n'
                output_string = output_string + '    </meta>\n'
                output_string = output_string + '    <link>https://www.youtube.com/watch?v=' + str(video_id) + '</link>\n'
                output_string = output_string + '    <thumbnail>' + str(thumbnail) + '</thumbnail>\n'
                if not self.fanart == None:
                    output_string = output_string + '    <fanart>' + str(self.fanart) + '</fanart>\n'
                output_string = output_string + '</item>\n\n'

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except:
                break
        return output_string

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