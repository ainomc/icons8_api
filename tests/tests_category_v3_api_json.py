# -*- coding: utf-8 -*-

import pytest

from api_logic import json_parse
from context.category_v3_context_json import ContextCategoryv3ApiJson


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

        amount = json_parse(json, ["parameters", "amount"])
        assert amount == str(ContextCategoryv3ApiJson.amount), \
            '>>> %s - "amount" in response, %s - in request <<<' % (amount, ContextCategoryv3ApiJson.amount)

        category = json_parse(json, ["parameters", "category"])
        assert category == ContextCategoryv3ApiJson.category, \
            '>>> %s - "category" in response, %s - in request <<<' % (category, ContextCategoryv3ApiJson.category)

        platform = json_parse(json, ["parameters", "platform"])
        assert platform == ContextCategoryv3ApiJson.platform, \
            '>>> %s - "platform" in response,  %s- in request<<<' % (platform, ContextCategoryv3ApiJson.platform)
        assert json_parse(json, ["parameters", "offset"]) == 0
        assert json_parse(json, ["parameters", "subcategory_id"]) == 0
        assert json_parse(json, ["parameters", "impresser_preview"]) == False
        assert json_parse(json, ["parameters", "language"]) == None

    # Test category object
    def test_category(self, param_test):
        (json) = param_test

        category_code = json_parse(json, ["result", "category", "category_code"])
        assert category_code == ContextCategoryv3ApiJson.category, \
            '>>> %s - "category_code" in response, %s - in request <<<' \
            % (category_code, ContextCategoryv3ApiJson.category)
        category_name = json_parse(json, ["result", "category", "category_name"])
        assert category_name == ContextCategoryv3ApiJson.category, \
            '>>> %s "" in response, %s - in request <<<' % (category_name, ContextCategoryv3ApiJson.category)

    # Test hare object
    def test_share(self, param_test):
        (json) = param_test
        assert json_parse(json, ["result", "category", "share", 'url'])[:20] == 'http://demo.ic8.link'
        assert json_parse(json, ["result", "category", "share", 'share_preview'])[:41] == \
               'https://demost.icons8.com/Share/category/'
        assert json_parse(json, ["result", "category", "share", 'icons_preview'])[:47] == \
               'https://demost.icons8.com/Share/category_icons/'

    # Test subcategories object
    def test_subcategories(self, param_test):
        (json) = param_test
        len(json_parse(json, ["result", "category", "subcategories"])) >= 0

    # Test category object
    def test_subcategory(self, param_test):
        (json) = param_test
        assert len(json_parse(json, ["result", "category", "subcategory", 0, 'subcategory_code'])) > 0
        assert len(json_parse(json, ["result", "category", "subcategory", 0, 'subcategory_code'])) > 0

    icon_numbers = []
    icon_count = len(json_parse(ContextCategoryv3ApiJson.response_root_auth, ["result", "category", "subcategory", 0, 'icons']))
    for icon_num in range(icon_count):
        icon_numbers.append(icon_num)

    @pytest.mark.parametrize("icon_number", icon_numbers)
    @pytest.mark.parametrize("json", [ContextCategoryv3ApiJson.response_root, ContextCategoryv3ApiJson.response_root_auth])
    # Test isons object
    def test_icons(self, icon_number, json):
        assert len(json_parse(json, ["result", "category", "subcategory", 0, 'icons', icon_number, 'id'])) > 0
        assert len(json_parse(json, ["result", "category", "subcategory", 0, 'icons', icon_number, 'name'])) > 0
        assert ContextCategoryv3ApiJson.platform_code_list.count(json_parse(json, ["result", "category", "subcategory", 0, 'icons', icon_number, 'platform_code'])) == 1
        assert len(json_parse(json, ["result", "category", "subcategory", 0, 'icons', icon_number, 'created'])) > 20
        assert json_parse(json, ["result", "category", "subcategory", 0, 'icons', icon_number, 'url'])[:9] == '/web-app/'
        assert len(json_parse(json, ["result", "category", "subcategory", 0, 'icons', icon_number, 'common_icon_id'])) > 1
        assert len(json_parse(json, ["result", "category", "subcategory", 0, 'icons', icon_number, 'svg'])) > 20

    @pytest.mark.parametrize("icon_number", icon_numbers)
    @pytest.mark.parametrize("json", [ContextCategoryv3ApiJson.response_root, ContextCategoryv3ApiJson.response_root_auth])
    # Test isons features object
    def test_icons_features(self, icon_number, json):
        for features in ["bitmap", "vector", "nolink"]:
            assert json_parse(json, ["result", "category", "subcategory", 0,
                                     'icons', icon_number, 'features', 'bitmap']) == 0 or 1






