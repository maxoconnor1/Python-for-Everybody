import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide="yes"/>
    </person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text) # the .text method returns the text beneath the name node
print('Attr:', tree.find('email').get('hide')) # find locates the entire email object set and get finds the hide attribute

