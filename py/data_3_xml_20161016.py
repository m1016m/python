#data_3_xml_20161016.py
#XML
#以符號分隔的檔案只能表達兩個維度:列與欄。
#如果要在程式間傳送檔案結構,需將階層、序列、集合及其他結構編碼成文字。
#XML使用標籤來劃分資料:
#
#Python’s interfaces for processing XML are grouped in the xml package.
#https://docs.python.org/3/library/xml.html?highlight=xml#module-xml
#本程式以 'country_data.xml' 為例

#在Python中,最簡單的XML解析方式是使用ElementTree。
import xml.etree.ElementTree as et #import xml.etree.ElementTree
tree1=et.ElementTree(file='country_data.xml') #解析 country_data.xml
root1=tree1.getroot() #取得root element
root1.tag #display tag of root element
for child in root1:    #印出一些標籤和屬性
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)
        
#--------------------------------------------------------------------------
#xml.dom
#xml.sax