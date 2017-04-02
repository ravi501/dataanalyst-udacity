import xml.etree.cElementTree as ET

def get_tags(file_name):
    tag_count = {}
    for event, elem in ET.iterparse(file_name, events=("start",)):
        if elem.tag not in tag_count:
            tag_count[elem.tag] = 1
        else:
            count = tag_count[elem.tag]
            count = count + 1
            tag_count[elem.tag] = count

    return tag_count

def print_tags(tags):
    for val in tags:
        print(val, tags[val])