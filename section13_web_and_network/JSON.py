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

import json

j = {
    "employee": [
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"}
    ]
}

print(j)
print('##########')
print(json.dumps(j))   # JSONは必ずダブルクォーテーションになる

with open('section13_web_and_network/test.json', 'w') as f:
    json.dump(j, f)
    
print('##########')
with open('section13_web_and_network/test.json', 'r') as f:
    print(json.load(f))