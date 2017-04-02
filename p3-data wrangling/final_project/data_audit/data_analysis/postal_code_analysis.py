import xml.etree.cElementTree as ET

def is_postal_code(tag):
    return tag.attrib['k'] == "addr:postcode"


def get_postal_codes(file_name):
    postal_codes = {}
    for event, element in ET.iterparse(file_name, events=("start",)):
        if element.tag == "node" or element.tag == "way":
            for tag in element.iter("tag"):
                if is_postal_code(tag):
                    if tag.attrib['v'] in postal_codes:
                        count = postal_codes[tag.attrib['v']]
                        count = count + 1
                        postal_codes[tag.attrib['v']] = count
                    else:
                        postal_codes[tag.attrib['v']] = 1


    return postal_codes


def print_postal_codes(postal_codes):
    for codes in postal_codes:
        print(codes)