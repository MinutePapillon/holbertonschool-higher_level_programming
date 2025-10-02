#!/usr/bin/python3
import xml.etree.ElementTree as ET


def convert_xml_to_dict(filename):
    """
    Convert an XML file into a Python dictionary
    Returns the dictionary if successful, None otherwise
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        def parse_element(element):
            parsed = {}
            # Si l'élément a des enfants
            if list(element):
                for child in element:
                    child_data = parse_element(child)
                    if child.tag in parsed:
                        # Plusieurs enfants avec la même balise => liste
                        if isinstance(parsed[child.tag], list):
                            parsed[child.tag].append(child_data[child.tag])
                        else:
                            parsed[child.tag] = [parsed[child.tag], child_data[child.tag]]
                    else:
                        parsed.update(child_data)
            else:
                parsed[element.tag] = element.text
                return parsed

            return {element.tag: parsed}

        return parse_element(root)
    except Exception:
        return None
