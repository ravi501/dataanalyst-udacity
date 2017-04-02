
from data_audit.data_analysis import data_read_analysis
from data_audit.data_analysis import tags_analysis
from data_audit.data_analysis import attributes_analysis
from data_audit.data_analysis import key_types_analysis
from data_audit.data_analysis import street_name_analysis
from data_audit.data_analysis import postal_code_analysis
from data_audit.data_analysis import house_number_aanalysis
from data_audit.data_analysis import phone_number_analysis

FILE_NAME="Seattle_dataset.osm"


def initiate_analysis_process(option):

    if "1" in option.split(" "):
        tags = tags_analysis.get_tags(FILE_NAME)
        tags_analysis.print_tags(tags)

    if "2" in option.split(" "):
        attributes = attributes_analysis.get_attributes(FILE_NAME)
        attributes_analysis.print_attributes(attributes)

    if "3" in option.split(" "):
        key_types = key_types_analysis.get_key_types(FILE_NAME)
        key_types_analysis.print_key_types(key_types)

    if "4" in option.split(" "):
        house_numbers = house_number_aanalysis.get_house_numbers(FILE_NAME)
        house_number_aanalysis.print_house_numbers(house_numbers)

    if "5" in option.split(" "):
        unexpected_street_names = street_name_analysis.get_unexpected_street_names(FILE_NAME)
        street_name_analysis.print_unexpected_street_names(unexpected_street_names)

    if "6" in option.split(" "):
        postal_codes = postal_code_analysis.get_postal_codes(FILE_NAME)
        postal_code_analysis.print_postal_codes(postal_codes)

    if "7" in option.split(" "):
        phone_numbers = phone_number_analysis.get_phone_numbers(FILE_NAME)
        phone_number_analysis.print_phone_numbers(phone_numbers)

initiate_analysis_process("7")
