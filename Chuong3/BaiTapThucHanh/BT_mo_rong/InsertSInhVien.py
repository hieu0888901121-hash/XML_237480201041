import xml.etree.ElementTree as ET

tree = ET.parse("Sinhvien.xml")

root = tree.getroot()

masv = input("Nhap ma sinh vien: ")
hoten = input("Nhap ho ten: ")
lop = input("Nhap lop: ")
diem = input("Nhap diem: ")

sinhvien = ET.SubElement(root, "sinhvien")

ET.SubElement(sinhvien, "masv").text = masv
ET.SubElement(sinhvien, "hoten").text = hoten
ET.SubElement(sinhvien, "lop").text = lop
ET.SubElement(sinhvien, "diem").text = diem

# Lưu lại file XML
ET.indent(tree, space="    ")
tree.write("Sinhvien.xml", encoding="utf-8", xml_declaration=True)

print("Da them sinh vien!")