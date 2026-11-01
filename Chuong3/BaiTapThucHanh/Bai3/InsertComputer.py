import xml.etree.ElementTree as ET

# Đọc file XML
tree = ET.parse("Computer.xml")
root = tree.getroot()

# Tạo máy tính mới
computer = ET.Element("computer")

name = ET.SubElement(computer, "name")
name.text = "Asus 2021"

cpu = ET.SubElement(computer, "cpu")
cpu.text = "Core i5 3.0Ghz"

ram = ET.SubElement(computer, "ram")
ram.text = "16GB"

ssd = ET.SubElement(computer, "ssd")
ssd.text = "256GB"
# Thêm vào cuối danh sách
root.append(computer)

ET.indent(tree, space="    ")

# Lưu lại file XML
tree.write("Computer.xml", encoding="utf-8", xml_declaration=True)

print("Đã thêm vào danh sách!")