import xml.etree.cElementTree as ET

def get_attributes(file_name):
    attributes = {}
    for event, elem in ET.iterparse(file_name, events=("start", )):
        for attr in elem.attrib:
            if attr not in attributes:
                attributes[attr] = 1
            else:
                count = attributes[attr]
                count += 1
                attributes[attr] = count
    return attributes

def print_attributes(attributes):
    for val in attributes:
        print(val, attributes[val])
