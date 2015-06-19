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

    # Check if "search" is in tag attributes
    all_tags = soup.findAll(True)
    all_tags_string = []
    all_tags_string.append(list(tag.attrs.values()) for tag in all_tags)

def read_url_database(database_file):
    pass
web_spider("http://www.unitedway.org/")
