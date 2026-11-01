import xml.etree.ElementTree as ET

tree = ET.parse("Sinhvien.xml")

root = tree.getroot()

# Nhập mã sinh viên cần xóa
MaCanXoa = input("Nhap ma sinh vien can xoa: ")

# Biến kiểm tra có tìm thấy hay không
Tim = False

# Duyệt danh sách sinh viên
for sinhvien in root.findall("sinhvien"):

    masv = sinhvien.find("masv").text

    if masv == MaCanXoa:
        root.remove(sinhvien)

        Tim = True
        break

# Nếu tìm thấy thì lưu lại
if Tim:
    tree.write("Sinhvien.xml", encoding="utf-8", xml_declaration=True)
    print("Da xoa sinh vien!")
else:
    print("Khong tim thay sinh vien!")