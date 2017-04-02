import xml.etree.cElementTree as ET
import re

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def get_key_types(file_name):
    key_types = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0 }
    for event, element in ET.iterparse(file_name, events=("start", )):
        if element.tag == "tag":
            if lower.match(element.attrib["k"]):
                val = key_types["lower"]
                val = val + 1
                key_types["lower"] = val
            elif lower_colon.match(element.attrib["k"]):
                val = key_types["lower_colon"]
                val = val + 1
                key_types["lower_colon"] = val
            elif problemchars.match(element.attrib["k"]):
                val = key_types["problemchars"]
                val = val + 1
                key_types["problemchars"] = val
            else:
                val = key_types["other"]
                val = val + 1
                key_types["other"] = val

    return key_types

def print_key_types(keys):
    for val in keys:
        print(val, keys[val])