import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# text = '<li><a href="/terms/sa_index.html">さ行</a></li>'
# URL = [https://www.jpx.co.jp/glossary/all/index.html]
def create_soup(siteurl):
    URL = siteurl
    html_content = requests.get(URL)

    html_content.encoding = 'UTF-8'
    html_content = html_content.text

    soup = BeautifulSoup(html_content, "html.parser")
    return soup
    
soup = create_soup("https://www.jpx.co.jp/glossary/all/index.html")

regix= re.compile('"([^"]*)"')

def get_link():
    words = soup.find_all("ul", {"class": "menu -parent"})
    links =regix.findall(str(words))[1:]
    baseURL = "https://www.nomura.co.jp"
    fulllinks = [baseURL+l for l in links]
    # class="menu -parent -active"
    return fulllinks


# fulllinks = get_link()
# print(fulllinks)
def get_words():
    words = soup.find_all("a", {"class": "link-window"})

    data = pd.DataFrame(columns=['words'])
    for w in words:
    # if 'terms' in str(w):
        data = data.append({'words':w.text}, ignore_index=True)

    return data


data = get_words()
data.to_csv('japan_dealing.csv',index=False, encoding='utf-8')