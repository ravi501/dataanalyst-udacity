

def get_all_other_fields(element):
    node = {}
    if element.tag == "node" or element.tag == "way":
        node["id"] = element.attrib["id"]

        created = {}
        created["version"] = element.attrib["version"]
        created["changeset"] = element.attrib["changeset"]
        created["timestamp"] = element.attrib["timestamp"]
        created["user"] = element.attrib["user"]
        created["uid"] = element.attrib["uid"]
        node["created"] = created

        if "lat" in element.attrib:
            pos = []
            pos.append(float(element.attrib["lat"]))
            pos.append(float(element.attrib["lon"]))
            node["pos"] = pos
        else:
            node["pos"] = []

    return node