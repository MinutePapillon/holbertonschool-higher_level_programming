#!/usr/bin/python3
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError


def convert_xml_to_dict(filename):
    """
    Convert an XML file into a Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
    except (FileNotFoundError, ParseError):
        return None

    def _parse(element):
        children = list(element)
        # Leaf node: return its text (stripped) or empty string if None/whitespace
        if not children:
            text = element.text
            return text.strip() if isinstance(text, str) else ""

        result = {}
        for child in children:
            value = _parse(child)
            tag = child.tag
            if tag in result:
                # If tag already present, ensure it's a list and append
                if isinstance(result[tag], list):
                    result[tag].append(value)
                else:
                    result[tag] = [result[tag], value]
            else:
                result[tag] = value
        return result

    parsed = _parse(root)

    # If root has repeated child tags, keep the root tag in the output
    child_tags = [child.tag for child in root]
    if len(child_tags) != len(set(child_tags)):
        return {root.tag: parsed}

    return parsed
