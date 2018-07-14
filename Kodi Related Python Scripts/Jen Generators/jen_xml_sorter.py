#!/usr/bin/python
# encoding=utf8
"""

    Copyright (C) 2018 MuadDib

    ----------------------------------------------------------------------------
    "THE BEER-WARE LICENSE" (Revision 42):
    @tantrumdev wrote this file.  As long as you retain this notice you
    can do whatever you want with this stuff. If we meet some day, and you think
    this stuff is worth it, you can buy him a beer in return. - Muad'Dib
    ----------------------------------------------------------------------------

    Changelog:
        2018.7.12:
            Minor updates, adding documentation for Jen Files Chat

    Update all entries in the script that have # CHANGEME above them.

    Make sure your XML is of proper format (for xml format I mean). Below is an example.
    I know most Jens do not use the two entry point XML tags, which is why the example is
        given below. This is needed for the script to be able to process them.

    Youtube URL explaining the use of this script: https://www.youtube.com/watch?v=H8QPo8fdeLs

    <my_addon>
        <main_menu>
            <dir>
                blah blah
            </dir>

            <item>
                blah blah
            </item>
        </main_menu>
    </my_addon>



"""

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