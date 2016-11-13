# -*- coding: utf-8 -*-
import requests
import random
import xml.etree.ElementTree as ET



# Do request, check response and return root of response. apiType - type of api, payload - values for url to xml
def request(apiType, payload):
    response = requests.get('https://demoapi.icons8.com/api/iconsets/%s' % apiType, params=payload)
    response.raise_for_status()
    return ET.fromstring(response.content)

# Find xml key by xpath and return key value.
def tag_value(root, tag, tag_xpath_number):
    return root.find('.//%s[%s]' % (tag, tag_xpath_number)).text

# Return all attributes from tag
def all_tag_attrib(root, tag, tag_xpath_number):
    return root.find('.//%s[%s]' % (tag, tag_xpath_number)).attrib

# Return  attribute value
def attrib_value(tag_all_attrib, Attrib):
    return tag_all_attrib.get(Attrib)


# Возвращает случайное значение из списка
def random_between_values(first_value, last_value):
    return random.randint(first_value, last_value)

def word_count(word):
    return len(word)

def check_all_categories(test_categories):
    all_categories = ["Windows 8/Metro", "iPhone/iOS 7", "Android", "Android L", "Color", "Windows 10/Threshold",
                      "Office"]
    all_categories_count = len(all_categories)
    current_categories = 0
    for categories in all_categories:
        try:
            assert test_categories == categories
            print (all_categories[current_categories] + " was found")
            break
        except AssertionError:
            current_categories += 1
            all_categories_count -= 1

    assert all_categories_count != 0
    return True



