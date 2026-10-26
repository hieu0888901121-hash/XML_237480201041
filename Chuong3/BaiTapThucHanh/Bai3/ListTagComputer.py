import xml.etree.ElementTree as ET

# Đọc file XML
tree = ET.parse("bai3/Computer.xml")

# Lấy phần tử gốc
root = tree.getroot()

# In tên các thẻ
for element in root.iter():
    if element.tag and element.tag.strip():
            print(element.tag.strip())