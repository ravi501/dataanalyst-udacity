import xml.etree.cElementTree as ET

FILE_NAME = "Seattle_dataset.osm"

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons", "Northeast", "Northwest", "North", "Broadway", "Alley",
            "Southwest", "Circle", "Terrace", "Way", "East", "West", "South", "Jackson", "65th",
            "207", "Place", "Driveway", "36th", "98103", "149"]

mapping = { "NE": "Northeast",
            "N": "North",
            "NW": "Northwest",
            "St": "Street",
            "S": "South",
            "street": "Street",
            "Pl": "Place",
            "driveway": "Driveway",
            "St.": "Street",
            "Ave": "Avenue",
            "Blvd": "Boulevard",
            "N.E.": "Northeast",
            "E": "East",
            "N.": "North",
            "SW": "Southwest",
            "W": "West"
          }


"""
This method checks if address information is present in the given tag or not
"""
def is_street_name(tag):
    return tag.attrib['k'] == "addr:street"


"""
This method audits and cleans the address
"""
def audit_and_update_street_name(street_name):
    if " " in street_name:
        name = street_name.split(" ")

        if name[len(name) - 1] in mapping:
            name[len(name) - 1] = mapping[name[len(name) - 1]]
            street_name = "".join(name)

    return street_name


"""
This method updates unexpected street name values
"""
def update_unexpected_street_names(element):
    street_name = ""

    for tag in element.iter("tag"):
        if is_street_name(tag):
            street_name = audit_and_update_street_name(tag.attrib['v'])

    return street_name


"""
This method checks if post code information is present in the given tag or not
"""
def is_contains_post_code(tag):
    return tag.attrib['k'] == "addr:postcode"


"""
This is the initialization method for post code
"""
def get_post_codes(element):
    for tag in element.iter("tag"):
        if is_contains_post_code(tag):
            return tag.attrib['v']


"""
This method checks if house number information is provided in the data
"""
def is_house_number(tag):
    return tag.attrib['k'] == "addr:housenumber"


"""
This method retrieved the house number information
"""
def get_house_number(element):
    for tag in element.iter("tag"):
        if is_house_number(tag):
            return tag.attrib['v']

"""
This method provides the address information to the __init__ class
"""
def get_address_information(element):
    address = {}

    if element.tag == "node" or element.tag == "way":
        street_name = update_unexpected_street_names(element)
        address["street"] = street_name
        address["postcode"] = get_post_codes(element)
        address["housenumber"] = get_house_number(element)

    return address
