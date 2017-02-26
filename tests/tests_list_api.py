# -*- coding: utf-8 -*-

import pytest

from icons8_api.api_logic import attrib_value, tag_value, all_tag_attrib, word_count
from context.list_context import ContextListApi


# Test Search Api with Default values. https://demoapi.icons8.com/manual/suggest
class TestListApi(ContextListApi):

    # Test 'list' 1 tag with any input
    def test_list1_tag(self):

        if ContextListApi.search_platform == "":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '1')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "iPhone/iOS 10"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    # Test 'list' 2 tag with any input
    def test_list2_tag(self):

        if ContextListApi.search_platform == "":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '2')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "Windows 10/Threshold"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    # Test 'list' 3 tag with any input
    def test_list3_tag(self):

        if ContextListApi.search_platform == "":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '3')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "Android" or "Windows 8/Metro"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    # Test 'list' 4 tag with any input
    def test_list4_tag(self):

        if ContextListApi.search_platform == "":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '4')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "Material"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    # Test 'list' 5 tag with any input
    def test_list5_tag(self):

        if ContextListApi.search_platform == "":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '5')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "Android 4"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    # Test 'list' 6 tag with any input
    def test_list6_tag(self):

        if ContextListApi.search_platform == "":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '6')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "Color"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    # Test 'list' 7 tag with any input
    def test_list7_tag(self):

        if ContextListApi.search_platform == "":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '7')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "Office"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    # Test 'list' win8 tag with any input
    def test_list_win8_tag(self):

        if ContextListApi.search_platform == "win8":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '1')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "Windows 8/Metro"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    # Test 'list' ios7 tag with any input
    def test_list_ios7_tag(self):

        if ContextListApi.search_platform == "ios7":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '1')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "iPhone/iOS 10"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    # Test 'list' android tag with any input
    def test_list_android_tag(self):

        if ContextListApi.search_platform == "android":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '1')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "Android 4"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    # Test 'list' androidL tag with any input
    def test_list_androidL_tag(self):

        if ContextListApi.search_platform == "androidL":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '1')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "Android L"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    # Test 'list' color tag with any input
    def test_list_color_tag(self):

        if ContextListApi.search_platform == "color":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '1')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "Color"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    # Test 'list' win10 tag with any input
    def test_list_win10_tag(self):

        if ContextListApi.search_platform == "win10":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '1')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "Windows 10/Threshold"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    # Test 'list' office tag with any input
    def test_list_office_tag(self):

        if ContextListApi.search_platform == "office":
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '1')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert value_of_attrib == "Office"

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"