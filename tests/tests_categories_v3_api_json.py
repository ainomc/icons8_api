# -*- coding: utf-8 -*-

import pytest

from icons8_api.api_logic import json_parse
from context.categories_v3_context_json import ContextCategories3vApiJson


@pytest.fixture(scope="function", params=[
    (ContextCategories3vApiJson.response_root),
    (ContextCategories3vApiJson.response_root_auth)
])
def param_test(request):
    return request.param

# Test icon API https://demoapi.icons8.com/api/iconsets/v2/icon
class TestCategoryApiJson(ContextCategories3vApiJson):

    # Test parameters object
    def test_parameters(self, param_test):
        (json) = param_test
        platform = json_parse(json, ["parameters", "platform"])
        assert platform == ContextCategories3vApiJson.platform, \
            '>>> %s - "platform" in response, %s - in request<<<' % (platform, ContextCategories3vApiJson.platform)
        language = json_parse(json, ["parameters", "language"])
        assert language == None, '>>> %s - "language" in response, None- in request <<<' % language

    # Test category object
    def test_categories(self, param_test):
        (json) = param_test
        categories_count = len(json_parse(json, ["result", "categories"]))
        for categories_num in range(categories_count):
            assert len(json_parse(json, ["result", "categories", categories_num, "name"])) > 1
            assert len(json_parse(json, ["result", "categories", categories_num, "api_code"])) > 1





