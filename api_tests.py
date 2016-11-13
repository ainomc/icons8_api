# -*- coding: utf-8 -*-
#from api_logic import *
from api_context import *
import pytest
import paramiko


# python -m pytest -v api_tests.py -s     --   runner

# Test icon API https://demoapi.icons8.com/manual/icon
class TestIconApi(Context):

    # icon id what will be in request
    icon_id = str(random_between_values(100, 20000))
    print (icon_id + ' test icon')
    # Do Request and return response root
    payload = {'id': icon_id}
    response_root = request('icon', payload)

    # Test 'resuilt' tag
    def test_resuilt_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'result', '1')
        value_of_attrib = attrib_value(tag_attribs, 'id')
        assert value_of_attrib == TestIconApi.icon_id

    # Test 'icon' tag
    def test_icon_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'icon', '1')
        value_of_attrib = attrib_value(tag_attribs, 'id')
        assert word_count(value_of_attrib) >= 1

        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert word_count(value_of_attrib) > 1

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
        value_of_tag = tag_value(TestIconApi.response_root, 'svg', '1')
        assert word_count(value_of_tag) > 1

    # Test icon 26 tag
    def test_png_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'png/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'width')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'height')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'

    # Test 'bitmap' tag
    def test_bitmap_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'bitmap', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'vector' test
    def test_vector_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'features/vector', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'nolink' test
    def test_nolink_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'nolink', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'categories/category' test
    def test_categorychild_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'categories/category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'category' test
    def test_category_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'share' tag
    def test_share_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'share', '1')
        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert value_of_attrib[:21] == "http://demo.ic8.link/"

    # Test 'share/png' 1 tag
    def test_share_png_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'share/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'