# -*- coding: utf-8 -*-
import requests
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