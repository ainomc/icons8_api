# -*- coding: utf-8 -*-

import pytest
import paramiko

from icons8_api.api_logic import attrib_value, all_tag_attrib, all_tag_attrib_with_icon_number, \
    tag_value_with_icon_number, word_count, check_all_categories
from context.icons_context import ContextIconsApi


"""
python -m pytest -v tests_latest_api.py -s     --   runner

"""


# Test Search Api with Default values. https://demoapi.icons8.com/manual/latest
class TestIconsApi(ContextIconsApi):


    # Test 'icon' tag
    def test_icon_tag(self):
        tag_attribs = all_tag_attrib(ContextIconsApi.response_root,
                                     'icon', ContextIconsApi.icon_number)
        value_of_attrib = attrib_value(tag_attribs, 'id')
        print (value_of_attrib + ' icon id what checked')
        assert word_count(value_of_attrib) >= 1

        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert word_count(value_of_attrib) >= 1

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert check_all_categories(value_of_attrib) == True

        value_of_attrib = attrib_value(tag_attribs, 'created')
        assert value_of_attrib[:2] == '20'

        value_of_attrib = attrib_value(tag_attribs, 'attributes')
        assert word_count(value_of_attrib) >= 0

        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert value_of_attrib[:9] == "/web-app/"

    # Test 'svg' tag
    def test_svg_tag(self):
        value_of_tag = tag_value_with_icon_number(ContextIconsApi.response_root,
                                                  ContextIconsApi.icon_number, 'svg', '1')
        assert word_count(value_of_tag) > 1

    # Test icon 26 tag
    def test_png_tag(self):
        tag_attribs = all_tag_attrib_with_icon_number(ContextIconsApi.response_root,
                                                      ContextIconsApi.icon_number, 'png/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'width')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'height')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'

    # Test 'bitmap' tag
    def test_bitmap_tag(self):
        value_of_tag = tag_value_with_icon_number(ContextIconsApi.response_root,
                                                  ContextIconsApi.icon_number, 'features/bitmap', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'vector' test
    def test_vector_tag(self):
        value_of_tag = tag_value_with_icon_number(ContextIconsApi.response_root,
                                                  ContextIconsApi.icon_number, 'features/vector', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'nolink' test
    def test_nolink_tag(self):
        value_of_tag = tag_value_with_icon_number(ContextIconsApi.response_root,
                                                  ContextIconsApi.icon_number, 'features/nolink', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'categories/category' test
    def test_categorychild_tag(self):
        value_of_tag = tag_value_with_icon_number(ContextIconsApi.response_root,
                                                  ContextIconsApi.icon_number, 'categories/category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'category' test
    def test_category_tag(self):
        value_of_tag = tag_value_with_icon_number(ContextIconsApi.response_root,
                                                  ContextIconsApi.icon_number, 'category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'share' tag
    def test_share_tag(self):
        tag_attribs = all_tag_attrib_with_icon_number(ContextIconsApi.response_root,
                                                      ContextIconsApi.icon_number, 'share', '1')
        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert value_of_attrib[:16] == "http://demo.ic8."

    # Test 'share/png' 1 tag
    def test_share_png_tag(self):
        tag_attribs = all_tag_attrib_with_icon_number(ContextIconsApi.response_root,
                                                      ContextIconsApi.icon_number, 'share/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'


