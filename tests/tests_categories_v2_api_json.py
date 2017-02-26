# -*- coding: utf-8 -*-

import pytest

from api_logic import json_parse, word_count
from context.categories_v2_context_json import ContextCategoriesApiJson


@pytest.fixture(scope="function", params=[
    (ContextCategoriesApiJson.response_root),
    (ContextCategoriesApiJson.response_root_auth)
])
def param_test(request):
    return request.param

# Test icon API https://demoapi.icons8.com/api/iconsets/v2/icon
class TestCategoriesApiJson(ContextCategoriesApiJson):

    # Test parameters object
    def test_parameters(self, param_test):
        (json) = param_test
        platform = json_parse(json, ["parameters", "platform"])
        assert platform == ContextCategoriesApiJson.platform, \
            '>>> %s - not int the list - %s <<<' % (platform, ContextCategoriesApiJson.platform)
        assert json_parse(json, ["parameters", "format"]) == None, '>>> 1rst - in response, 2nd - in request <<<'

    categories_numbers = []
    categories_count = len(json_parse(ContextCategoriesApiJson.response_root_auth, ["result", "categories"]))
    for categories in range(categories_count):
        categories_numbers.append(categories)

    @pytest.mark.parametrize("categories_number", categories_numbers)
    @pytest.mark.parametrize("json", [ContextCategoriesApiJson.response_root, ContextCategoriesApiJson.response_root_auth])
    # Test categories object
    def test_categories(self, categories_number, json):
        assert len(json_parse(json, ["result", "categories", categories_number, "name"])) >= 2
        assert len(json_parse(json, ["result", "categories", categories_number, "description"])) >= 0


    @pytest.mark.parametrize("categories_number", categories_numbers)
    @pytest.mark.parametrize("json", [ContextCategoriesApiJson.response_root, ContextCategoriesApiJson.response_root_auth])
    # Test categories story object
    def test_categories_story(self, categories_number, json):
        for story in ["text", "author_name", "author_photo", "author_link", "date"]:
            assert len(json_parse(json, ["result", "categories",
                                         categories_number, "story", story]).encode('utf-8')) >= 0

    @pytest.mark.parametrize("categories_number", categories_numbers)
    @pytest.mark.parametrize("json", [ContextCategoriesApiJson.response_root, ContextCategoriesApiJson.response_root_auth])
    # Test categories share object
    def test_categories_share(self, categories_number, json):
        assert json_parse(json, ["result", "categories", categories_number, "share", "url"])[:20] == "http://demo.ic8.link"
        try:
            assert json_parse(json, ["result", "categories", categories_number, "share", "share_preview"])[:25] == "https://demost.icons8.com"
            assert json_parse(json, ["result", "categories", categories_number, "share", "icons_preview"])[:25] == "https://demost.icons8.com"
        except:
            pass





