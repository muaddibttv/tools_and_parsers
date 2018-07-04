import xml.etree.ElementTree as ET
import re,traceback

try:
    # CHANGEME Set this to the name of your Jen XML file you want to sort.
    tree = ET.parse("concerts.xml")

    # CHANGEME Make sure you have <element> structure around your Jen's XML entries (like <xml><my_stuff> at the top of the file and </my_stuff></xml> at the end of the file)
    container = tree.find("wannabe")

    # CHANGEME Change the "title" to the key you want to sort the listings by. Typically, title is the choice.
    def get_title(elem):
        txt = re.sub('\[.*?]','',str(elem.findtext("title").lower()))
        return replaceHTMLCodes(txt)

    def replaceHTMLCodes(txt):
        txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
        txt = txt.replace("&quot;", "\"").replace("&amp;", "&")
        txt = txt.replace('&#8216;','\'').replace('&#8217;','\'').replace('&#038;','&').replace('&#8230;','....')
        txt = txt.strip()
        return txt

    container[:] = sorted(container, key=get_title)
    tree.write("!sorted.xml")
except:
    failure = traceback.format_exc()
    print('Exception: ' + failure)