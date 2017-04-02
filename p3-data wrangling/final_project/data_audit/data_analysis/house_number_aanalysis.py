import xml.etree.cElementTree as ET


def is_house_number(tag):
    return tag.attrib['k'] == "addr:housenumber"


def get_house_numbers(file_name):
    house_numbers = {}
    for event, element in ET.iterparse(file_name, events=("start",)):
        if element.tag == "node" or element.tag == "way":
            for tag in element.iter("tag"):
                if is_house_number(tag):
                    if tag.attrib['v'] in house_numbers:
                        count = house_numbers[tag.attrib['v']]
                        count = count + 1
                        house_numbers[tag.attrib['v']] = count
                    else:
                        house_numbers[tag.attrib['v']] = 1

    return house_numbers


def print_house_numbers(house_numbers):
    for num in house_numbers:
        print(num)