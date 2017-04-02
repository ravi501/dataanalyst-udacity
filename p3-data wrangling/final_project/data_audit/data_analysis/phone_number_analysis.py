
import xml.etree.cElementTree as ET


def is_phone_number(tag):
    return tag.attrib['k'] == "phone"


def get_phone_numbers(file_name):
    phone_numbers = {}
    for event, element in ET.iterparse(file_name, events=("start",)):
        if element.tag == "node" or element.tag == "way":
            for tag in element.iter("tag"):
                if is_phone_number(tag):
                    if tag.attrib['v'] in phone_numbers:
                        count = phone_numbers[tag.attrib['v']]
                        count = count + 1
                        phone_numbers[tag.attrib['v']] = count
                    else:
                        phone_numbers[tag.attrib['v']] = 1

    return phone_numbers

"""
def print_phone_numbers(phone_numbers):
    for num in phone_numbers:
        print(num)

        """