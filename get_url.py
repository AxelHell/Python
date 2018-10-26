import requests
import bs4
from lxml import html
import pandas as pd
import re
import json

user_id = 12345
search_url = "https://www.investing.com/search/?q=fbr".format(user_id)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
r = requests.get(search_url, headers = headers)
b = bs4.BeautifulSoup(r.text, "html.parser")
#print (b)
www = b.find('div', class_='js-inner-all-results-quotes-wrapper newResultsContainer quatesTable')
www_1 = www.find('script').getText()

pattern = re.search("\[(.*?)\]", www_1).group(1)
#pattern_1 = re.search("\[{.*?}\]", pattern).group(1)
#print (pattern_1)

fake_dict = {'false':'0','null':'0', '\/':'/'}
for x,y in fake_dict.items():
    pattern = pattern.replace (x,y)

# Переформатирование строки в список (элемент = непреобразованному словарю)
pattern_new = pattern.replace('},{','}(,){').split('(,)')

print (pattern_new)

#dct = eval(pattern_new[0])
str_json = json.loads(pattern_new[0])
print (str_json['pairId'])