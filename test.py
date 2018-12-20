import xml.etree.ElementTree as ET

tree = ET.parse('data/akiva/015968100_511033060_KGM_201803201907_1.xml')
root = tree.getroot()
print(root.tag)