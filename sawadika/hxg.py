__author__ = 'Liang Li'
import requests
from bs4 import BeautifulSoup

def diversity_inclusion_search(url):
    source_code = requests.get(url)
    plain_txt = source_code.text
    soup = BeautifulSoup(plain_txt)
    has_DI = False
    href = ''
    for link in soup.findAll('a'):
        link_text = link.string
        if link_text is not None and \
                        "Diversity".lower() in link_text.lower() and "Inclusion".lower() in link_text.lower():
            has_DI = True
            href = link.get("href")

    # Check if "Diversity and Inclusion" is under a tab
    # all_li_string = soup.get_text("li")
    # all_li_string = all_li_string.replace("li", "")
    # print(all_li_string)

    # Check if "search" is in tag attributes
    all_tags = soup.findAll(True)
    all_tags_string = ''
    for tag in all_tags:
        tag_attrs_value = list(tag.attrs.values())
        for value in tag_attrs_value:
            ele_type = type(value)
            while ele_type is not str:
                value = ''.join(value)
                ele_type = type(value)
            all_tags_string += value
    has_search = "search" in all_tags_string.lower()
    return {'has_DI': has_DI, 'DI_url': href, 'has_search': has_search}

# result = diversity_inclusion_search("http://www.unitedway.org/")
# print(result['has_DI'], result['DI_url'], result['has_search'])
