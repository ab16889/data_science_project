
# coding: utf-8

# In[2]:

import xml.etree.ElementTree as ET
tree = ET.parse('FTDA-1991-0629.xml')
root = tree.getroot()







headlines = []
content=[]




for x in root.iterfind(".//text.title"):
    check = False
    for y in x.iter():
        if y.get('pgref') == '1':
            check = True
        if check:
            print y.text
            headlines.append(y.text)




#check headlines size ~ 200 words per day
len(headlines)



for x in root.iterfind(".//text.cr"):
    check = False
    for y in x.iter():
        if y.get('pgref') == '1':
            check = True
        if check:
            print y.text
            content.append(y.text)




#check content size ~3000 words per day
len(content)






