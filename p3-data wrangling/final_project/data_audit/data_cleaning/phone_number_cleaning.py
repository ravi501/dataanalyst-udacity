import xml.etree.cElementTree as ET

FILE_NAME = "Seattle_dataset.osm"

"""
This method cleanes the phone numbers.

The different types of out of order phone numbers observed are:
 1-206-296-4441
+1-206-441-9729
+1 (844) 585 2487 x3
+ 206 436-6836
12067200969
+!-206-453-3068
+1 206-622–2036
206-903-022
+1 206–547–1226
http://www.couperokei.com
206-621-8656;2066218656

This method cleanes such data and returns phone numbers in +1 (xxx) yyy-zzzz format.
"""
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


"""
This method checks if the given tag contains phone number attribute
"""
def has_phone_number(tag):
    return tag.attrib['k'] == "phone"


"""
This is the initialization method to process phone numbers
"""
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