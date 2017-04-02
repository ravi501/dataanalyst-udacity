import xml.etree.cElementTree as ET

FILE_NAME = "Seattle_dataset.osm"

def update_phone_numbers(phone_number):

    formatted_phone_number = ""
    number = ""

    if "NULL" in phone_number:
        return ""

    if "http" in phone_number:
        return ""
    if phone_number == "911":
        return "911"

    if "+1 " in phone_number:
        number = phone_number.split("+1 ")[1]
    elif "+1" in phone_number:
        number = phone_number.split("+1")[1]
    elif "+!" in phone_number:
        number = phone_number.split("+!")[1]
    else:
        number = phone_number

    formatted_phone_number += "+1 "

    if number[0] == "1" and number[1] == "-":
        number = number[2:]

    if "+ " in number:
        number = number.replace("+ ", "")

    if "-" in number:
        number = number.replace("-", "")

    if " " in number:
        number = number.replace(" ", "")

    if "(" in number:
        number = number.replace("(", "")

    if ")" in number:
        number = number.replace(")", "")

    if "." in number:
        number = number.replace(".", "")

    if "x3" in number:
        number = number.replace("x3", "")

    if "–" in number:
        number = number.replace("–", "")

    if "=" in number:
        number = number.replace("=", "")

    if "?" in number:
        number = number.replace("?", "")

    if ";" in number:
        number = number.split(";")[0]

    if len(number) > 10:
        if number[0] == '1':
            number = number[1:]

    number = "(" + number[:3] + ")" + " " + number[3:6] + "-" + number[6:]

    formatted_phone_number += number

    return formatted_phone_number


def has_phone_number(tag):
    return tag.attrib['k'] == "phone"


def get_phone_number_valid_format(element):
    updated_phone_number = ""

    for tag in element.iter("tag"):
        if has_phone_number(tag):
            updated_phone_number = update_phone_numbers(tag.attrib['v'])

    return updated_phone_number

"""
def init():
    for event, element in ET.iterparse(FILE_NAME, events=("start",)):

        if element.tag == "node" or element.tag == "way":
            for tag in element.iter("tag"):
                if has_phone_number(tag):
                    print(update_phone_numbers(tag.attrib['v']))



init()

"""