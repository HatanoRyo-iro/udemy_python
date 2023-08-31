"""
# XML
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <emoloyee>
        <employ>
            <id>111</id>
            <name>Mike</name>
        </employ>
        <employ>
            <id>222</id>
            <name>Nancy</name>
        </employ>
    </emoloyee>
</root>

# JSON
{
    "employee": [
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"}
    ]
}
"""

import xml.etree.ElementTree as ET

root = ET.Element('root')
tree = ET.ElementTree(element=root)

employee = ET.SubElement(root, 'employee')

employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '111'
employ_name = ET.SubElement(employ, 'name')
employ_name.text = 'Mike'

employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '222'
employ_name = ET.SubElement(employ, 'name')
employ_name.text = 'Nancy'

tree.write('section13_web_and_network/test.xml', encoding='utf-8', xml_declaration=True)

# 読み込み
tree = ET.ElementTree(file='section13_web_and_network/test.xml')
root = tree.getroot()

for employee in root:
    for employ in employee:
        for person in employ:
            print(person.tag, person.text)