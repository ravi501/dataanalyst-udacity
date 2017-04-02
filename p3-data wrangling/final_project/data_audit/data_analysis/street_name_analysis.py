import xml.etree.cElementTree as ET
import re

from collections import defaultdict

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons"]


def is_street_name(element):
    return (element.attrib['k'] == "addr:street")

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def get_unexpected_street_names(file_name):
    street_names = {}
    street_types = defaultdict(set)
    for event, element in ET.iterparse(file_name, events=("start", )):
        if element.tag == "node" or element.tag == "way":
            for tag in element.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])

    return street_types


def print_unexpected_street_names(street_names):
    for type in street_names:
        print(type)