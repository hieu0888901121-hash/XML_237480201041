import xml.etree.ElementTree as ET

tree = ET.parse("bai3/Computer.xml")

root = tree.getroot()

for element in root.iter():
    if element.tag and element.tag.strip():
            print(element.tag.strip())