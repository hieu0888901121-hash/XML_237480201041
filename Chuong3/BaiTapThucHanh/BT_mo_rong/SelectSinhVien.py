import xml.etree.ElementTree as ET

tree = ET.parse("Sinhvien.xml")

root = tree.getroot()

MaCanTim = input("Nhap ma sinh vien: ")

Tim = False

# Duyệt danh sách sinh viên
for sinhvien in root.findall("sinhvien"):

    masv = sinhvien.find("masv").text

    if masv == MaCanTim:
        hoten = sinhvien.find("hoten").text
        lop = sinhvien.find("lop").text
        diem = sinhvien.find("diem").text

        print("Ma SV:", masv)
        print("Ho ten:", hoten)
        print("Lop:", lop)
        print("Diem:", diem)

        Tim = True
        break

# Nếu không tìm thấy
if Tim == False:
    print("Khong tim thay sinh vien!")