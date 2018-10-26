import xml.etree.ElementTree as etree
tree = etree.parse ('q02.xml')
root = tree.getroot()
all_tags = tree.findall('.//') # Парсинг всей структуры xml
#print (all_tags[7].text) # Вывод значение аттрибута

f = open ('data.doc','w')

# Создать массив и сохранить в файл
for name in all_tags:
    f.write("%s\t" % name.tag) # Запись тега
    f.write("%s\n" % name.text) # Запись значения тега
   
    



