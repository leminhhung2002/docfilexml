import xml.etree.ElementTree as ET
import time


file = ET.parse('hung.xml')

ACT = file.getroot()
print ("ID  Name  Age  CreateAt")
for i in ACT.findall('people'):
  ID = i.get('id')
  Name = i.find("name").text
  Age = i.find("age").text
  CreateAt = i.get('createAt')
  chain = time.strftime('%d/%m/%Y', time.localtime(int(CreateAt)))
  print(ID,Name, Age, chain )