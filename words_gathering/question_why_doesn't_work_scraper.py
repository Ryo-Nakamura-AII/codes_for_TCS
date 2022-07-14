import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# text = '<li><a href="/terms/sa_index.html">さ行</a></li>'
# URL = [https://www.jpx.co.jp/glossary/all/index.html]
URL = "https://www.nomura.co.jp/terms/a_index.html"
html_content = requests.get(URL)

html_content.encoding = 'UTF-8'
html_content = html_content.text

soup = BeautifulSoup(html_content, "html.parser")

regix= re.compile('"([^"]*)"')


def get_link():
    words = soup.find_all("ul", {"class": "menu -parent"})
    links =regix.findall(str(words))[1:]
    baseURL = "https://www.nomura.co.jp"
    fulllinks = [baseURL+l for l in links]
    # class="menu -parent -active"
    return fulllinks


    


fulllinks = get_link()
# print(fulllinks)

# data.to_csv('words.csv', encoding='utf-8')
def get_all_words():
    data = pd.DataFrame(columns=['野村証券'])
    for u in fulllinks:
        each_html_content = requests.get(u)

        each_html_content.encoding = 'UTF-8'
        each_html_content = each_html_content.text

        each_soup = BeautifulSoup(each_html_content, "html.parser")
        
        data = get_words()
    return data

def get_words():
    words = each_soup.find_all("a", {"class": "link -forward"})
    for w in words:
        if 'terms' in str(w):
            data = data.append({'words':w.text}, ignore_index=True)

    return data

data =get_all_words()