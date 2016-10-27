# -*- coding: utf-8 -*-
#from api_logic import *
from api_context import *
import pytest


# python -m pytest -v api_tests.py -s     --   runner

# Test icon API https://demoapi.icons8.com/manual/icon
class TestIconApi(IconSettings):

    # Do Request and return response root
    payload = {'id': '941'}
    response_root = request('icon', payload)

    # Test resuilt tag
    def test_resuilt_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'result', '1')
        value_of_attrib = attrib_value(tag_attribs, 'id')
        assert value_of_attrib == '941'

    # Test icon tag
    def test_icon_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'icon', '1')
        value_of_attrib = attrib_value(tag_attribs, 'id')
        assert value_of_attrib == '941'

        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Rabbit"

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert value_of_attrib == "Windows 8/Metro"

        value_of_attrib = attrib_value(tag_attribs, 'created')
        assert value_of_attrib == '2012-06-19T03:45:02+04:00'

        value_of_attrib = attrib_value(tag_attribs, 'attributes')
        assert value_of_attrib == ""

        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert value_of_attrib == "/web-app/941/rabbit"

    # Test svg test
    def test_svg_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'svg', '1')
        assert value_of_tag[0:15] == 'PHN2ZyB4bWxucz0'

    # Test icon 26 tag
    def test_png26_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'png/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'width')
        assert value_of_attrib == '26'

        value_of_attrib = attrib_value(tag_attribs, 'height')
        assert value_of_attrib == '26'

        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-6:] == '26.png'

    # Test icon 104 tag
    def test_png104_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'png/png', '5')
        value_of_attrib = attrib_value(tag_attribs, 'width')
        assert value_of_attrib == '104'

        value_of_attrib = attrib_value(tag_attribs, 'height')
        assert value_of_attrib == '104'

        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-7:] == '104.png'

    # Test bitmap test
    def test_bitmap_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'bitmap', '1')
        assert value_of_tag == '0'

    # Test vector test
    def test_vector_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'vector', '1')
        assert value_of_tag == '0'

    # Test nolink test
    def test_nolink_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'nolink', '1')
        assert value_of_tag == '0'

    # Test categories/category test
    def test_categorychild_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'categories/category', '1')
        assert value_of_tag == 'Animals'

    # Test category test
    def test_category_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'category', '1')
        assert value_of_tag == 'Animals'

    # Test subcategory tag
    def test_subcategory_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'subcategory', '1')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == 'Wildlife'

        value_of_attrib = attrib_value(tag_attribs, 'api_code')
        assert value_of_attrib == 'wildlife'

    # Test share tag
    def test_share_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'share', '1')
        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert value_of_attrib == 'http://demo.ic8.link/941'

    # Test share/png 1 tag
    def test_sharepng1_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'share/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-10:] == 'rabbit.png'

    # Test share/png 2 tag
    def test_sharepng2_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'share/png', '2')
        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-10:] == 'rabbit.png'

        value_of_attrib = attrib_value(tag_attribs, 'type')
        assert value_of_attrib == 'twitter'

    # Test share/png 3 tag
    def test_sharepng3_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'share/png', '3')
        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-10:] == 'rabbit.png'

        value_of_attrib = attrib_value(tag_attribs, 'type')
        assert value_of_attrib == 'social'