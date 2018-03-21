# -*- coding: UTF-8 -*-
""" Processes HTML of a YT channel's Playlists, to build a template file for all of them. """

import os, re, unicodedata
import dom_parser

class Generator:
    def __init__( self ):
        # create initial variables needed later
        self.htmlFilename = 'ytplaylistpage.txt'
        self.tools_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__))))

        # CHANGEME to match the path needed for your generic fanart to add to each entry. Set to None to not set it.
        # Example: self.fanart = None
        self.fanart = 'https://raw.githubusercontent.com/muaddibttv/tantrumxmls/master/jbuddentv/media/fanart.jpg'

        # generate files
        self._generate_yt_templates()

        # notify user
        print "Finished parsing the html. Output saved as output_html.txt"

    def _generate_yt_templates ( self ):

        print "Reading HTML File....."

        try:
            output_string = ''

            _path = self.tools_path + os.path.sep + self.htmlFilename   
            r = open(_path)
            html = r.read()       

            the_divs = parseDOM(html, 'div', attrs={'class':'feed-item-dismissable '})
            print 'Total Playlists: ' + str(len(the_divs))
            for the_div in the_divs:
                header = parseDOM(the_div, 'h3', attrs={'class':'yt-lockup-title '})[0]
                link = parseDOM(header, 'a', attrs={'class':'yt-uix-sessionlink.+?'}, ret='href')[0]
                title = parseDOM(header, 'a', attrs={'class':'yt-uix-sessionlink.+?'}, ret='title')[0]
                title = replaceEscapeCodes(title)
                title = replaceHTMLCodes(title).replace('"', '\'')
                title = unicodedata.normalize('NFKD', title).encode('ascii','ignore')
                try:
                    icon = parseDOM(the_div, 'img', attrs={'aria-hidden':'true'}, ret='data-thumb')[0]
                except:
                    icon = parseDOM(the_div, 'img', attrs={'aria-hidden':'true'}, ret='src')[0]

                list = link.split('list=')[1]

                output_string = output_string + 'name="' + str(title) + '"\n'
                output_string = output_string + 'section="false"\n'
                output_string = output_string + 'search="false"\n'
                output_string = output_string + 'subid="false"\n'
                output_string = output_string + 'playlistid="' + str(list) + '"\n'
                output_string = output_string + 'channelid="false"\n'
                output_string = output_string + 'videoid="false"\n'
                output_string = output_string + 'icon="' + str(icon) + '"\n'
                if not self.fanart == None:
                    output_string = output_string + 'fanart="' + str(self.fanart) + '"\n'
                else:
                    output_string = output_string + 'fanart="http://"\n'
                output_string = output_string + 'description="' + str(title) + '"\n\n'            

        except Exception, e:
            # missing or poorly formatted xml
            print "What the fuck dude? %s" % ( e )

        # save file
        with open("output_html.txt","w") as f:
            f.write(output_string)

def parseDOM(html, name='', attrs=None, ret=False):
    if attrs: attrs = dict((key, re.compile(value + ('$' if value else ''))) for key, value in attrs.iteritems())
    results = dom_parser.parse_dom(html, name, attrs, ret)
    if ret:
        results = [result.attrs[ret.lower()] for result in results]
    else:
        results = [result.content for result in results]
    return results

def replaceHTMLCodes(txt):
    txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
    import HTMLParser
    txt = HTMLParser.HTMLParser().unescape(txt)
    txt = txt.replace("&quot;", "\"")
    txt = txt.replace("&amp;", "&")
    txt = txt.strip()
    return txt

def replaceEscapeCodes(txt):
    import HTMLParser
    txt = HTMLParser.HTMLParser().unescape(txt)
    return txt

if ( __name__ == "__main__" ):
    # start
    Generator()