# -*- coding: utf-8 -*-

import json
import random
import time
import requests
from requests.exceptions import ConnectionError
import xml.etree.ElementTree as ET

# Read param.json
my_data = json.loads(open("param.json").read())
request_url = my_data['request_url']
auth_id = my_data['auth_id']
platform_list = my_data['platform_list']
platform_code_list = my_data['platform_code_list']
all_categories = my_data['all_categories']

# default request_url and auth_id if no any request_url or auth_id
if request_url == '':
    request_url = 'devapi'
if auth_id == '':
    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'


def request(api_type, payload, verison, type):
    """ Do request, check response and return root of response.
     apiType - type of api, payload - values for url to request
     """
    # Change request url depending on api versions (1v, 2v, 3v)
    if verison == "v1":
        response = requests.get('https://%s.icons8.com/api/iconsets/%s' %
                                (request_url, api_type), params=payload, verify=False)
    elif verison == "v2" or verison == "v3":
        response = \
            requests.get('https://%s.icons8.com/api/iconsets/%s/%s' %
                         (request_url, verison, api_type), params=payload, verify=False)

    # Check status of api
    response.raise_for_status()

    # Change parser depending on type
    if type == "xml":
        return ET.fromstring(response.content)
    elif type == "json":
        return response.json()


def tag_value(root, tag, tag_xpath_number):
    """Find xml key by xpath and return key value."""
    return root.find('.//%s[%s]' % (tag, tag_xpath_number)).text


def all_tag_attrib(root, tag, tag_xpath_number):
    """Return all attributes from tag"""
    return root.find('.//%s[%s]' % (tag, tag_xpath_number)).attrib


def tag_value_with_icon_number(root, icon, tag, tag_xpath_number):
    """Find xml key by xpath and return key value."""
    if icon == 0:
        pass
    else:
        return root.find('.//icon[%s]/%s[%s]' %
                         (icon, tag, tag_xpath_number)).text


def all_tag_attrib_with_icon_number(root, icon, tag, tag_xpath_number):
    """Return all attributes from tag"""
    if icon == 0:
        pass
    else:
        return root.find('.//icon[%s]/%s[%s]' %
                         (icon, tag, tag_xpath_number)).attrib


def attrib_value(tag_all_attrib, attrib):
    """Return attribute value"""
    return tag_all_attrib.get(attrib)


def random_between_values(first_value, last_value):
    """Return random value between from first_value to last_value"""
    return random.randint(first_value, last_value)


def random_list_value(list):
    """Return random value from list"""
    return random.choice(list)


def word_count(word):
    """Return word count"""
    return len(word)


def check_all_categories(test_categories):
    """Check categories in list categories"""
    all_categories = ["Windows 8/Metro", "iPhone/iOS 10", "Android 4",
                      "Android L", "Color", "Windows 10/Threshold",
                      "Office", "Material", "Gradient", "Ultraviolet",
                      "Nolan", "DottyDots", "Red Short Lines", "1em",
                      "iPhone/iOS 11", "1em", "Dusk", "Wired", "Metro",
                      "iPhone/iOS", "Ice Cream", "Dotty Dots"]
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


def json_parse(json_text, keys):
    """parse tickets jsons
     example: json_parse("json file", 1, ["colors", "red"])
     """
    value = json_text
    for key in keys:
        value = value[key]
    return value
