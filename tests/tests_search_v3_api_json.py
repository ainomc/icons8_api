# -*- coding: utf-8 -*-

import pytest

from api_logic import json_parse, platform_list, platform_code_list
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

        amount = json_parse(json, ["parameters", "amount"])
        assert amount == str(ContextCategoryv3ApiJson.amount), \
            '>>> %s - in response, %s - in request <<<' % (amount, ContextCategoryv3ApiJson.amount)

        term = json_parse(json, ["parameters", "term"])
        assert term == str(ContextCategoryv3ApiJson.term), \
            '>>> %s - in response, %s - in request <<<' % (term, ContextCategoryv3ApiJson.term)

        assert int(json_parse(json, ["parameters", "offset"])) == 10

        platform = json_parse(json, ["parameters", "platform"])
        assert platform == ContextCategoryv3ApiJson.platform, \
            '>>> %s - in response, %s - in request <<<' % (platform, ContextCategoryv3ApiJson.platform)
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
        assert platform_code_list.index\
                   (json_parse(json, ["result", "search", search_number, "platform_code"])) >= 0
        assert len(json_parse(json, ["result", "search", search_number, "created"])) > 23
        assert '/icon/' in json_parse(json, ["result", "search", search_number, "url"])[:9]
        assert json_parse(json, ["result", "search", search_number, "common_icon_id"]) > 1
        #assert len(json_parse(json, ["result", "search", search_number, "category"])) > 1
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

"""
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
        assert ".ic8.link" in json_parse(json, ["result", "search", search_number, "share", "url"])
        assert ".icons8.com" in json_parse(json, ["result", "search", search_number, "share", "png", 0, "link"])
        try:
            assert ".icons8.com" in json_parse(json, ["result", "search", search_number, "share", "png", 1, "link"])
            assert ".icons8.com" in json_parse(json, ["result", "search", search_number, "share", "png", 2, "link"])
            assert 'twitter' in json_parse(json, ["result", "search", search_number, "share", "png", 1, "type"])
            assert 'social' in json_parse(json, ["result", "search", search_number, "share", "png", 2, "social"])
        except:
            pass
"""













