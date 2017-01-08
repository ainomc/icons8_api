# -*- coding: utf-8 -*-

import pytest

from icons8_api.api_logic import json_parse
from context.category_v3_context_json import ContextCategoryv3ApiJson



"""
api_context - file with fixtures and settings
api_logic - file with main logic of tests
One class - tested one response with some values
One test method - test one xml tag and in one tag can be 2+ attributes

python -m pytest -v tests_icon_api.py -s     --   runner

"""

@pytest.fixture(scope="function", params=[
    (ContextCategoryv3ApiJson.response_root),
    (ContextCategoryv3ApiJson.response_root_auth)
])
def param_test(request):
    return request.param

# Test icon API https://demoapi.icons8.com/api/iconsets/v2/icon
class TestCategoryApiJson(ContextCategoryv3ApiJson):

    # Test parameters object
    def test_parameters(self, param_test):
        (json) = param_test

        assert json_parse(json, ["parameters", "amount"]) == str(ContextCategoryv3ApiJson.amount)
        assert json_parse(json, ["parameters", "category"]) == ContextCategoryv3ApiJson.category
        assert json_parse(json, ["parameters", "platform"]) == ContextCategoryv3ApiJson.platform
        assert json_parse(json, ["parameters", "offset"]) == 0
        assert json_parse(json, ["parameters", "subcategory_id"]) == 0
        assert json_parse(json, ["parameters", "impresser_preview"]) == False
        assert json_parse(json, ["parameters", "language"]) == None

    # Test category object
    def test_category(self, param_test):
        (json) = param_test

        assert json_parse(json, ["result", "category", "category_code"]) == ContextCategoryv3ApiJson.category
        assert json_parse(json, ["result", "category", "category_name"]) == ContextCategoryv3ApiJson.category

    # Test category object
    def test_subcategory(self, param_test):
        (json) = param_test

        assert len(json_parse(json, ["result", "category", "subcategory", 0, 'subcategory_code'])) > 0
        assert len(json_parse(json, ["result", "category", "subcategory", 0, 'subcategory_code'])) > 0

    icon_numbers = []
    icon_count = len(json_parse(ContextCategoryv3ApiJson.response_root_auth, ["result", "category", "subcategory", 0, 'icons']))
    for icon_num in range(icon_count):
        icon_numbers.append(icon_num)
    print icon_numbers
"""
    @pytest.mark.parametrize("icon_number", icon_numbers)
    @pytest.mark.parametrize("json", [ContextCategoryv3ApiJson.response_root, ContextCategoryv3ApiJson.response_root_auth])
    # Test isons object
    def test_icons(self, icon_number, json):
        assert len(json_parse(json, ["result", "category", "subcategory", 0, 'icons', icon_number, 'id'])) > 0
"""