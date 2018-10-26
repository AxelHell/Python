import requests
import bs4
from lxml import html
import pandas as pd

f = open ('data.csv','w')

user_id = 12345
url = "https://www.investing.com/equities/uralkaliy_rts-balance-sheet".format (user_id)
url_1 = "https://www.investing.com/instruments/Financials/changereporttypeajax?action=change_report_type&pair_ID=13722&report_type=BAL&period_type=Annual".format (user_id)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
r = requests.get(url, headers = headers)
r_1 = requests.get(url_1, headers = headers)

b_1 = bs4.BeautifulSoup(r_1.text, "html.parser").get_text()

www = pd.read_html(r_1.text)[1:]

idx = pd.concat(www).reset_index(drop=True)

print (idx)

#df = www.at[1,1]

#tjson = www.to_json()
#tcsv = idx.to_csv()
#ttext = www.to_string()
#print (tjson)
#f.write(tcsv)


doc = html.fromstring(r_1.content)

td = doc.xpath('//span') 

#print (td)

col = []

i = 0


# Сделать преобразование списка col в dict
for te in td:
    i+=1
    name = te.text_content()
    #print (i,name)
    col.append(name) 







b = bs4.BeautifulSoup(r.text, "html.parser")



section = []

tds = b.find_all('table', class_ = 'genTbl reportTbl') # Запись таблиц в массив. Раздел таблицы = элементу массива

# with open('test.txt', 'w', encoding='utf-8') as output_file:
#  output_file.write(r.text)

