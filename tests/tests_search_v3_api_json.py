# -*- coding: utf-8 -*-

import pytest

from icons8_api.api_logic import json_parse
from context.search_v3_context_json import ContextCategoryv3ApiJson


@pytest.fixture(scope="function", params=[
    (ContextCategoryv3ApiJson.response_root),
    (ContextCategoryv3ApiJson.response_root_auth)
])
def param_test(request):
    return request.param

# Test icon API https://demoapi.icons8.com/api/iconsets/v2/icon
class TestSearchv3ApiJson(ContextCategoryv3ApiJson):

    # Test parameters object
    def test_parameters(self, param_test):
        (json) = param_test

        assert json_parse(json, ["parameters", "amount"]) == str(ContextCategoryv3ApiJson.amount)
        assert json_parse(json, ["parameters", "term"]) == str(ContextCategoryv3ApiJson.term)
        assert int(json_parse(json, ["parameters", "offset"])) == 10
        assert json_parse(json, ["parameters", "platform"]) == ContextCategoryv3ApiJson.platform
        assert json_parse(json, ["parameters", "impresser_preview"]) == False
        assert json_parse(json, ["parameters", "language"]) == None

    # Test description object
    def test_description(self, param_test):
        (json) = param_test
        try:
            assert len(json_parse(json, ["result", "description"])) > 5
            assert len(json_parse(json, ["result", "description"])) >= 0
        except KeyError:
            pass

    search_number = []
    search_count = len(json_parse(ContextCategoryv3ApiJson.response_root_auth, ["result", "search"]))
    for search_num in range(search_count):
        search_number.append(search_num)

    @pytest.mark.parametrize("search_number", search_number)
    @pytest.mark.parametrize("json", [ContextCategoryv3ApiJson.response_root,
                                      ContextCategoryv3ApiJson.response_root_auth])
    # Test search object
    def test_icons(self, search_number, json):
        assert json_parse(json, ["result", "search", search_number, "id"]) > 1
        assert len(json_parse(json, ["result", "search", search_number, "name"])) > 1
        assert ContextCategoryv3ApiJson.platform_code_list.index\
                   (json_parse(json, ["result", "search", search_number, "platform_code"])) >= 0
        assert len(json_parse(json, ["result", "search", search_number, "created"])) > 23
        assert json_parse(json, ["result", "search", search_number, "url"])[:9] == '/web-app/'
        assert json_parse(json, ["result", "search", search_number, "common_icon_id"]) > 1
        assert len(json_parse(json, ["result", "search", search_number, "category"])) > 1
        try:
            assert len(json_parse(json, ["result", "search", search_number, "related"])) > 1
            assert len(json_parse(json, ["result", "search", search_number, "related-by-term"])) > 1
            assert len(json_parse(json, ["result", "search", search_number, "svg"])) > 30
        except KeyError:
            pass
        try:
            assert len(json_parse(json, ["result", "search", search_number, "subcategory", "name"])) > 1
            assert len(json_parse(json, ["result", "search", search_number, "subcategory", "api_code"])) > 1
        except KeyError:
            pass


    @pytest.mark.parametrize("search_number", search_number)
    @pytest.mark.parametrize("json", [ContextCategoryv3ApiJson.response_root,
                                      ContextCategoryv3ApiJson.response_root_auth])
    # Test features object
    def test_features(self, search_number, json):
        for features in ["bitmap", "vector", "nolink"]:
            assert json_parse(json, ["result", "search", search_number, "features", features]) == 0 or 1

    @pytest.mark.parametrize("search_number", search_number)
    @pytest.mark.parametrize("json", [ContextCategoryv3ApiJson.response_root,
                                      ContextCategoryv3ApiJson.response_root_auth])
    # Test share object
    def test_share(self, search_number, json):
        assert json_parse(json, ["result", "search", search_number, "share", "url"])[:20] == 'http://demo.ic8.link'
        assert json_parse(json, ["result", "search", search_number, "share", "png", 0, "link"])[:25] == 'https://demost.icons8.com'
        try:
            assert json_parse(json, ["result", "search", search_number, "share", "png", 1, "link"])[:25] == 'https://demost.icons8.com'
            assert json_parse(json, ["result", "search", search_number, "share", "png", 2, "link"])[:25] == 'https://demost.icons8.com'
            assert json_parse(json, ["result", "search", search_number, "share", "png", 1, "type"])[:25] == 'twitter'
            assert json_parse(json, ["result", "search", search_number, "share", "png", 2, "social"])[:25] == 'social'
        except:
            pass














