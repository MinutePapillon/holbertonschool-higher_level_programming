#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("Data")
    for key, value in dictionary.items():
        ET.SubElement(root, '{}'.format(key)).text = value
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    my_dict = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for element in root:
        my_dict[element.tag] = element.text
    return my_dict
