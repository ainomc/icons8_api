# -*- coding: utf-8 -*-

import pytest

from api_logic import attrib_value, tag_value, all_tag_attrib, word_count
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

    for platform_num in range(1, 12):
        # Test platform tag
        def test_platform_ios10_tag(self, param_test):
            (root) = param_test
            tag_attribs = all_tag_attrib(TestTotalApi.response_root, 'platform', TestTotalApi.platform_num)
            value_of_attrib = attrib_value(tag_attribs, 'name')
            assert value_of_attrib in TestTotalApi.platform_list

            value_of_tag = tag_value(TestTotalApi.response_root, 'platform', '1')
            assert word_count(value_of_tag) >= 1