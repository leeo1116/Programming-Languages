__author__ = 'Liang Li'
import requests
from bs4 import BeautifulSoup

def web_spider(url):
    link_set = set()
    source_code = requests.get(url)
    plain_txt = source_code.text
    if "Diversity".lower() in plain_txt.lower() and "Inclusion".lower() in plain_txt.lower():
        print("Diversity and Inclusion found!")
    soup = BeautifulSoup(plain_txt)
    for link in soup.findAll('a'):  # ('a', {"class": "item-name"})
        link_text = link.string
        if link_text is not None and \
                        "Diversity".lower() in link_text.lower() and "Inclusion".lower() in link_text.lower():
            href = link.get("href")
            print(link_text, ':', href)

web_spider("http://www.unitedway.org/")
