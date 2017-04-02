import xml.etree.cElementTree as ET
import codecs
import json

from data_audit.data_cleaning import get_other_fields
from data_audit.data_cleaning import address_cleaning
from data_audit.data_cleaning import phone_number_cleaning


FILE_NAME="Seattle_dataset.osm"
FILE_OUT="output.json"


def init_clean_and_build_json():

    with codecs.open(FILE_OUT, "w") as fo:
        for event, element in ET.iterparse(FILE_NAME, events=("start",)):
            if element.tag == "node" or element.tag == "way":
                json_object = get_other_fields.get_all_other_fields(element)
                json_object["address"] = address_cleaning.get_address_information(element)
                json_object["phone"] = phone_number_cleaning.get_phone_number_valid_format(element)

                fo.write(json.dumps(json_object)+"\n")





init_clean_and_build_json()