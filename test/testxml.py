import xml.etree.ElementTree as ET

#tree = ET.parse('characterization/akiva/015968100_511033060_KGM_201803201907_1.xml')
tree = ET.parse('c:\\work\\015968100_512065202_KGM_201803201907_2.xml')
root = tree.getroot()
print(root.tag)