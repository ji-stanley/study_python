# __author__: Stanley
# date: 2018/4/27

from xml.etree import  ElementTree as ET

tree = ET.parse("test_xml.xml")
root = tree.getroot()
print(root.tag) # 打印根标签。

# 遍历xml文档
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text)


#　只遍历　year  节点
for node  in root.iter('year'):
    print(node.tag,node.text)