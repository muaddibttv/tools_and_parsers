# -*- coding: UTF-8 -*-
""" Processes HTML of the Hip Hop Golden Age artist's list page and generate a Jen Template for it. """
""" *** Requires the requests module to be installed. If you do not have it, run 'pip install requests' from the command prompt """

import os, re, requests, traceback, unicodedata
import dom_parser

class Generator:
    def __init__( self ):
        # create initial variables needed later

        # CHANGEME to filename you want the output to be
        self.output = 'artists.xml'

        # CHANGEME if url changes for the website.
        self.url = 'http://hiphopgoldenage.com/artists/'
        self.tools_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__))))

        # CHANGEME to match the path needed for your generic fanart to add to each entry. Set to None to not set it.
        # Example: self.fanart = None
        self.fanart = 'https://raw.githubusercontent.com/muaddibttv/tantrumxmls/master/jbuddentv/media/fanart.jpg'

        # CHANGEME if you want artist all lower case in the lastfm line
        self.makelower = False

        # CHANGEME if you want the artist name to contain no spaces in the lastfm line
        self.nospaces = False

        # generate files
        self._generate_templates()

        # notify user
        print('Finished parsing the website. Output saved as xml files in the same folder as this tool.')

    def _generate_templates ( self ):

        print('Processing website.....')

        try:
            output_string = ''
            html = requests.get(self.url, headers={'User-Agent':randomagent()}).content

            the_div = parseDOM(html, 'div', attrs={'class':'artist-grid'})[0]
            artists = parseDOM(the_div, 'a', attrs={'class':'item letter letter.+?'})

            count = 0
            for para in artists:
                artist = re.compile('<p>(.+?)</p>').findall(para)[0]

                artist_alt = artist
                if self.makelower == True:
                    artist_alt = artist_alt.lower()
                if self.nospaces == True:
                    artist_alt = artist_alt.replace(' ', '')

                output_string = output_string + '<dir>\n'
                output_string = output_string + '    <title>' + str(artist) + ' Tracks</title>\n'
                output_string = output_string + '    <lastfm>artist/' + str(artist_alt) + '/tracks</lastfm>\n'
                if not self.fanart == None:
                    output_string = output_string + '    <fanart>' + str(self.fanart) + '</fanart>\n'
                output_string = output_string + '</dir>\n\n'
                output_string = output_string + '<dir>\n'
                output_string = output_string + '    <title>' + str(artist) + ' Albums</title>\n'
                output_string = output_string + '    <lastfm>artist/' + str(artist_alt) + '/albums</lastfm>\n'
                output_string = output_string + '</dir>\n\n'
                count += 1

            print('Completed Track and Album entries for ' + str(count) + ' artists/groups')
        except:
            failure = traceback.format_exc()
            print('HHGA Artist Parser - Exception: \n' + str(failure))

        # save file
        with open(self.output,"w") as f:
            f.write(output_string)

def parseDOM(html, name='', attrs=None, ret=False):
    if attrs: attrs = dict((key, re.compile(value + ('$' if value else ''))) for key, value in attrs.items())
    results = dom_parser.parse_dom(html, name, attrs, ret)
    if ret:
        results = [result.attrs[ret.lower()] for result in results]
    else:
        results = [result.content for result in results]
    return results

def replaceHTMLCodes(txt):
    txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
    try:
        import HTMLParser as html_parser
    except:
        import html.parser as html_parser
    txt = html_parser.HTMLParser().unescape(txt)
    txt = html_parser.HTMLParser().unescape(txt)
    txt = txt.replace("&quot;", "\"")
    txt = txt.replace("&amp;", "&")
    txt = txt.strip()
    return txt

def replaceEscapeCodes(txt):
    try:
        import HTMLParser as html_parser
    except:
        import html.parser as html_parser
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