import xml.etree.ElementTree as ET
import re

# CHANGEME Set this to the name of your Jen XML file you want to sort.
tree = ET.parse("chocolatemain.xml")

# CHANGEME Make sure you have <element> structure around your Jen's XML entries (like <xml><my_stuff> at the top of the file and </my_stuff></xml> at the end of the file)
container = tree.find("csb")

# CHANGEME Change the "title" to the key you want to sort the listings by. Typically, title is the choice.
def get_title(elem):
    return re.sub('\[.*?]','',str(elem.findtext("title").lower()))

container[:] = sorted(container, key=get_title)
tree.write("!sorted.xml")