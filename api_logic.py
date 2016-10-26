# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET

# Main logic for all api types
class BaseApiLogic(object):

    # Do request, check response and return root of response. apiType - type of api, payload - values for url to xml
    def request(self, apiType, payload):
        self.requests = requests
        response = self.requests.get('https://api.icons8.com/api/iconsets/%s' % apiType, params=payload)
        response.raise_for_status()
        responseRoot = ET.fromstring(response.content)
        return responseRoot

    # Find xml key by xpath and return key value.
    def tagValue(self, root, tag, tagXpathNumber):
        tagValue = root.find('.//%s[%s]' % (tag, tagXpathNumber)).text
        return tagValue

    # Check actual result of xml value, equal or not to expected result
    def assertEqual(self, value, expectedResult):
        assert value == expectedResult

    # Return all attributes from tag
    def tagAllAttrib(self, root, tag, tagXpathNumber):
        tagValue = root.find('.//%s[%s]' % (tag, tagXpathNumber)).attrib
        return tagValue

    # Return  attribute value
    def AtrbValue(self, tagAllAttrib, Attrib):
        AtrbValue = tagAllAttrib.get(Attrib)
        return AtrbValue
