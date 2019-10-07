import xml.etree_ElemenTree as ET
import codecs

f = codecs.open("movie.xml", encoding = "utf-8")
data = f.read()
tree = ET.ElementTree(ET.fromstring(data))
root = tree.getRoot()
print(root.jpg)

for child in root :
    print("tag : " + child.tag, child.text)
f.close()


for childe as import
    