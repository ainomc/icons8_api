# -*- coding: utf-8 -*-

import pytest
import paramiko

from icons8_api.api_logic import attrib_value, tag_value, all_tag_attrib, word_count
from context.total_context import ContextTotalApi

@pytest.fixture(scope="function", params=[
    (ContextTotalApi.response_root),
    (ContextTotalApi.response_root_auth)
])
def param_test(request):
    return request.param

# Test Search Api with Default values. https://demoapi.icons8.com/manual/total
class TestTotalApi(ContextTotalApi):


    # Test total tag
    def test_total_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'total', '1')
        value_of_attrib = attrib_value(tag_attribs, 'since')
        assert word_count(value_of_attrib) > 1

    # Test platform 1 (iso10) tag
    def test_platform_ios10_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(TestTotalApi.response_root, 'platform', '1')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "iPhone/iOS 10"

        value_of_tag = tag_value(TestTotalApi.response_root, 'platform', '1')
        assert word_count(value_of_tag) >= 1

    # Test platform 2 (ios7) tag
    def test_platform_win10_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'platform', '2')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Windows 10/Threshold"

        value_of_tag = tag_value(root, 'platform', '2')
        assert word_count(value_of_tag) >= 1

    # Test platform 3 (win8) tag
    def test_platform_win8_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'platform', '3')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Windows 8/Metro"

        value_of_tag = tag_value(TestTotalApi.response_root, 'platform', '3')
        assert word_count(value_of_tag) >= 1

    # Test platform 4 (Material) tag
    def test_platform_material_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'platform', '4')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Material"

        value_of_tag = tag_value(TestTotalApi.response_root, 'platform', '4')
        assert word_count(value_of_tag) >= 1

    # Test platform 5 (Android 4") tag
    def test_platform_android4_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'platform', '5')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Android 4"

        value_of_tag = tag_value(root, 'platform', '5')
        assert word_count(value_of_tag) >= 1

    # Test platform 6 (win10) tag
    def test_platform_color_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'platform', '6')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Color"

        value_of_tag = tag_value(root, 'platform', '6')
        assert word_count(value_of_tag) >= 1

    # Test platform 7 (Office) tag
    def test_platform_office_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'platform', '7')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Office"

        value_of_tag = tag_value(root, 'platform', '7')
        assert word_count(value_of_tag) >= 1

    # Test platform 8 (1em) tag
    def test_platform_1em_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'platform', '8')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "1em"

        value_of_tag = tag_value(root, 'platform', '8')
        assert word_count(value_of_tag) >= 1

    # Test platform 9 (Gradient) tag
    def test_platform_Gradient_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'platform', '9')
        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert value_of_attrib == "Gradient"

        value_of_tag = tag_value(root, 'platform', '9')
        assert word_count(value_of_tag) >= 1