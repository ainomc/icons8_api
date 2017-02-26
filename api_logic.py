# -*- coding: utf-8 -*-

import json
import random
import time
import requests
import os
from requests.exceptions import ConnectionError
import xml.etree.ElementTree as ET


print os.getcwd()

my_data = json.loads(open("param.json").read())
request_url = my_data['request_url']
auth_id = my_data['auth_id']

print ('>>> PARAM URL: %s ' % request_url)

if request_url == '':
    request_url = 'demoapi'
if auth_id == '':
    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'

print ('>>> PARAM URL: %s ' % request_url)
# Do request, check response and return root of response. apiType - type of api, payload - values for url to request
def request(api_type, payload, verison, type):
    try:
        if verison == "v1":
            response = requests.get('https://%s.icons8.com/api/iconsets/%s' %
                                    (request_url, api_type), params=payload)
        elif verison == "v2" or verison == "v3":
            response = requests.get('https://%s.icons8.com/api/iconsets/%s/%s' %
                                    (request_url, verison, api_type), params=payload)
    except ConnectionError:
        time.sleep(5)
    response.raise_for_status()

    if type == "xml":
        return ET.fromstring(response.content)
    elif type == "json":
        return response.json()

# Find xml key by xpath and return key value.
def tag_value(root, tag, tag_xpath_number):
    return root.find('.//%s[%s]' % (tag, tag_xpath_number)).text

# Return all attributes from tag
def all_tag_attrib(root, tag, tag_xpath_number):
    return root.find('.//%s[%s]' % (tag, tag_xpath_number)).attrib

# Find xml key by xpath and return key value.
def tag_value_with_icon_number(root, icon, tag, tag_xpath_number):
    if icon == 0:
        pass
    else:
        return root.find('.//icon[%s]/%s[%s]' % (icon, tag, tag_xpath_number)).text

# Return all attributes from tag
def all_tag_attrib_with_icon_number(root, icon, tag, tag_xpath_number):
    if icon == 0:
        pass
    else:
        return root.find('.//icon[%s]/%s[%s]' % (icon, tag, tag_xpath_number)).attrib

# Return  attribute value
def attrib_value(tag_all_attrib, Attrib):
    return tag_all_attrib.get(Attrib)


# Возвращает случайное значение из списка
def random_between_values(first_value, last_value):
    return random.randint(first_value, last_value)

# Возвращает случайное значение из списка
def random_list_value(list):
    return random.choice(list)


def word_count(word):
    return len(word)


def check_all_categories(test_categories):
    all_categories = ["Windows 8/Metro", "iPhone/iOS 10", "Android 4", "Android L",
                     "Color", "Windows 10/Threshold", "Office", "Material", "1em", "Gradient"]
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

# parse tickets jsons
# example: json_parse("json file", 1, ["colors", "red"])
def json_parse(json_text, values):

    count_values = len(values)
    if count_values == 1:
        resuilt = json_text[values[0]]
    elif count_values == 2:
        resuilt = json_text[values[0]][values[1]]
    elif count_values == 3:
        resuilt = json_text[values[0]][values[1]][values[2]]
    elif count_values == 4:
        resuilt = json_text[values[0]][values[1]][values[2]][values[3]]
    elif count_values == 5:
        resuilt = json_text[values[0]][values[1]][values[2]][values[3]][values[4]]
    elif count_values == 6:
        resuilt = json_text[values[0]][values[1]][values[2]][values[3]][values[4]]\
            [values[5]]
    elif count_values == 7:
        resuilt = json_text[values[0]][values[1]][values[2]][values[3]][values[4]]\
            [values[5]][values[6]]
    elif count_values == 8:
        resuilt = json_text[values[0]][values[1]][values[2]][values[3]][values[4]]\
            [values[5]][values[6]][values[7]]
    elif count_values == 9:
        resuilt = json_text[values[0]][values[1]][values[2]][values[3]][values[4]]\
            [values[5]][values[6]][values[7]][values[8]]
    else:
        assert count_values == 9 or count_values > 9
    return resuilt



