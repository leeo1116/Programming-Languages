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

    # Check if "Diversity and Inclusion" is under a tab
    all_li_tags = soup.findAll("li")
    all_li_string = soup.get_text("li")
    all_li_string = all_li_string.replace("li", "")
    print(all_li_string)
        #print((li_tag.string))
        # all_li_string += li_tag.string


    # Check if "search" is in tag attributes
    all_tags = soup.findAll(True)
    #print('\n'.join([tag.name for tag in all_tags]))
    all_tags_string = ''
    for tag in all_tags:
        tag_attrs_value = list(tag.attrs.values())
        for value in tag_attrs_value:
            ele_type = type(value)
            while ele_type is not str:
                value = ''.join(value)
                ele_type = type(value)
            all_tags_string += value
    print("search" in all_tags_string.lower())

def read_url_database(database_file):
    pass
web_spider("http://www.unitedway.org/")
