# -*- coding: utf-8 -*-

import pytest
import paramiko

from icons8_api.api_logic import attrib_value, tag_value, all_tag_attrib, word_count
from icons8_api.api_context import ContextTotalApi


"""
python -m pytest -v tests_total_api.py -s     --   runner

"""


# Test Search Api with Default values. https://demoapi.icons8.com/manual/total
class TestTotalApi(ContextTotalApi):


    # Test total tag
    def test_total_tag(self):
        tag_attribs = all_tag_attrib(TestTotalApi.response_root, 'total', '1')
        value_of_attrib = attrib_value(tag_attribs, 'since')
        assert word_count(value_of_attrib) > 1

    # Test platform 1 (win8) tag
    def test_platform_win8_tag(self):
        tag_attribs = all_tag_attrib(TestTotalApi.response_root, 'platform', '1')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Windows 8/Metro"

        value_of_tag = tag_value(TestTotalApi.response_root, 'platform', '1')
        assert word_count(value_of_tag) >= 1

    # Test platform 2 (ios7) tag
    def test_platform_ios7_tag(self):
        tag_attribs = all_tag_attrib(TestTotalApi.response_root, 'platform', '2')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "iPhone/iOS 7"

        value_of_tag = tag_value(TestTotalApi.response_root, 'platform', '2')
        assert word_count(value_of_tag) >= 1

    # Test platform 3 (android) tag
    def test_platform_android_tag(self):
        tag_attribs = all_tag_attrib(TestTotalApi.response_root, 'platform', '3')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Android"

        value_of_tag = tag_value(TestTotalApi.response_root, 'platform', '3')
        assert word_count(value_of_tag) >= 1

    # Test platform 4 (android L) tag
    def test_platform_androidl_tag(self):
        tag_attribs = all_tag_attrib(TestTotalApi.response_root, 'platform', '4')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Android L"

        value_of_tag = tag_value(TestTotalApi.response_root, 'platform', '4')
        assert word_count(value_of_tag) >= 1

    # Test platform 5 (Color) tag
    def test_platform_color_tag(self):
        tag_attribs = all_tag_attrib(TestTotalApi.response_root, 'platform', '5')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Color"

        value_of_tag = tag_value(TestTotalApi.response_root, 'platform', '5')
        assert word_count(value_of_tag) >= 1

    # Test platform 6 (win10) tag
    def test_platform_win10_tag(self):
        tag_attribs = all_tag_attrib(TestTotalApi.response_root, 'platform', '6')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Windows 10/Threshold"

        value_of_tag = tag_value(TestTotalApi.response_root, 'platform', '6')
        assert word_count(value_of_tag) >= 1

    # Test platform 7 (Office) tag
    def test_platform_office_tag(self):
        tag_attribs = all_tag_attrib(TestTotalApi.response_root, 'platform', '7')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Office"

        value_of_tag = tag_value(TestTotalApi.response_root, 'platform', '7')
        assert word_count(value_of_tag) >= 1