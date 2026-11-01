import xml.etree.ElementTree as ET

tree = ET.parse("Computer.xml")

root = tree.getroot()

# Duyệt từng máy tính
i = 1

for computer in root.findall("computer"):
    name = computer.find("name").text
    cpu = computer.find("cpu").text
    ram = computer.find("ram").text

    print(i, ".")
    print("name: ", name)
    print("cpu: ", cpu)
    print("ram: ", ram)

    print()

    i += 1