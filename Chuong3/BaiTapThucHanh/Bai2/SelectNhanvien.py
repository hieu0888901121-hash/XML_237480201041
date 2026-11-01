import xml.etree.ElementTree as ET

tree = ET.parse("hoso.xml")

root = tree.getroot()

for nhanvien in root.findall("nhanvien"):
    manv = nhanvien.find("manv").text

    if manv == "002":
        hoten = nhanvien.find("hoten").text
        donvi = nhanvien.find("donvi").text
        luong = nhanvien.find("luong").text

        print("Mã nhân viên:", manv)
        print("Họ tên:", hoten)
        print("Đơn vị:", donvi)
        print("Lương:", luong)