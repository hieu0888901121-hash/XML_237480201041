import xml.etree.ElementTree as ET

tree = ET.parse("hoso.xml")
root = tree.getroot()

for element in root.iter():
    # tim the 
    if element.tag and element.tag.strip():
        print(element.tag.strip())