import time
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def scraper(url: str):
    driver = webdriver.Firefox()

    driver.get(url+"/authors")
    elems = driver.find_elements(By.CLASS_NAME, "col-24-24")
    print(len(elems), "entries found.\n")
    scraped_txt = ""
    for elem in elems:
        if len(elem.text)>len(scraped_txt):
            scraped_txt = elem.text
    time.sleep(1)
    store(scraped_txt)
    driver.close()


def store(txt: str):
    lst = txt.split(sep="\n")
    print(lst)
    d = dict()
    d[lst[0][:-1]] = lst[1]
    d[lst[2][:13]] = lst[2][14:]
    d[lst[3][:18]] = lst[3][19:]
    d[lst[7][:3]] = lst[7][4:]
    d[lst[8][:9]] = lst[8][10:]
    d[lst[10][:]] = [": ".join([lst[i],lst[i+1]]) for i in range(11,len(lst)-6,2)]
    print(d)
    '''with open(file_name, "a") as f:
        pass'''


URL = "https://ieeexplore.ieee.org/document/4460684"
scraper(URL)
print("\n\n Document2:\n")
URL = "https://ieeexplore.ieee.org/document/9497989"
scraper(URL)
print("Program end.")
