from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = r"C:\Users\ryona\Downloads\chromedriver"
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get('https://www.daiwa.jp/glossary/')


l = driver.find_elements_by_tag_name('a')

fulllinks = []
for lnk in l:
    li = lnk.get_attribute('href')
    if li and 'glossary/cat' in li:
        fulllinks.append(li)


def get_all_words():
    data = pd.DataFrame(columns=['大和証券'])
    for u in fulllinks:
        driver.get(u)

        words = driver.find_elements_by_xpath('//ul[@class="keyList column3 p2 mtxt"]/li')
        for w in words:
            data = data.append({'大和証券':w.text}, ignore_index=True)
    return data


data = get_all_words()

data.to_csv('daiwa.csv', encoding='utf-8')