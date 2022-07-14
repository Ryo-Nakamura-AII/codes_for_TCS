import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# text = '<li><a href="/terms/sa_index.html">さ行</a></li>'
# URL = [https://www.jpx.co.jp/glossary/all/index.html]
URL = "https://www.daiwa.jp/glossary/"
html_content = requests.get(URL)

html_content.encoding = 'shift_jis'

# print(html_content)

soup = BeautifulSoup(html_content, "html.parser")


# regix= re.compile('"([^"]*)"')

# words = soup.find_all("div", {"id": "categoryWrapper"})
# w = soup.find_all("div", {"id": "category"})
print(w)
def get_words():
    words = soup.find_all("ul", {"class": "keyList column3 p2 mtxt"})

    data = pd.DataFrame(columns=['日本取引所'])
    for w in words:
    # if 'terms' in str(w):
        data = data.append({'日本取引所':w.text}, ignore_index=True)


def get_link():
    words = soup.find_all("a")
    links =regix.findall(str(words))[1:]
    baseURL = "https://www.nomura.co.jp"
    fulllinks = [baseURL+l for l in links]
    # class="menu -parent -active"
    return fulllinks


    


# fulllinks = get_link()
# print(fulllinks)

def get_all_words():
    data = pd.DataFrame(columns=['野村証券'])
    for u in fulllinks:
        each_html_content = requests.get(u)

        each_html_content.encoding = 'UTF-8'
        each_html_content = each_html_content.text

        each_soup = BeautifulSoup(each_html_content, "html.parser")
        
        words = each_soup.find_all("a", {"class": "link -forward"})
        for w in words:
            if 'terms' in str(w):
                data = data.append({'野村証券':w.text}, ignore_index=True)
    return data


# data = get_words()

# print(data)


# data.to_csv('daiwa.csv', encoding='utf-8')