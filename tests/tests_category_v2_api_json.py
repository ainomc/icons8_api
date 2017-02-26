# -*- coding: utf-8 -*-

import pytest

from icons8_api.api_logic import json_parse, word_count
from context.category_v2_context_json import ContextCategoryApiJson


@pytest.fixture(scope="function", params=[
    (ContextCategoryApiJson.response_root),
    (ContextCategoryApiJson.response_root_auth)
])
def param_test(request):
    return request.param

# Test icon API https://demoapi.icons8.com/api/iconsets/v2/icon
class TestCategoryApiJson(ContextCategoryApiJson):

    # Test parameters object
    def test_parameters(self, param_test):
        (json) = param_test

        category = json_parse(json, ["parameters", "category"])
        assert category == ContextCategoryApiJson.category, \
            '>>> %s - "category" in response, %s - in request<<<' % (category, ContextCategoryApiJson.category)

        amount = json_parse(json, ["parameters", "amount"])
        assert amount == str(ContextCategoryApiJson.amount), \
            '>>> %s - "category" in response, %s - in request <<<' % (amount, ContextCategoryApiJson.amount)
        assert json_parse(json, ["parameters", "offset"]) == 0

        platform = json_parse(json, ["parameters", "platform"])
        assert platform == ContextCategoryApiJson.platform, \
            '>>> %s - "platform" in response, %s - in request <<<' % (platform, ContextCategoryApiJson.platform)

        attributes = json_parse(json, ["parameters", "attributes"])
        assert attributes == ContextCategoryApiJson.attributes, \
            '>>> %s - "category" in response, %s - in request <<<' % (attributes, ContextCategoryApiJson.attributes)
        assert json_parse(json, ["parameters", "impresser_preview"]) == False

    # Test category object
    def test_category(self, param_test):
        (json) = param_test

        name = json_parse(json, ["result", "category", "name"])
        assert name == ContextCategoryApiJson.category, \
            '>>>  %s - "name" in response, %s - in request <<<' % (name, ContextCategoryApiJson.category)
        assert json_parse(json, ["result", "category", "description"]) == '' or str
        assert json_parse(json, ["result", "category", "usage_story"]) == '' or str

    # Test story object
    def test_story(self, param_test):
        (json) = param_test

        assert len(json_parse(json, ["result", "category", "story", "text"])) > 15
        assert len(json_parse(json, ["result", "category", "story", "author_name"])) >= 2
        for story in ["author_photo", "author_link", "date"]:
            assert json_parse(json, ["result", "category", "story",
                                     story]) == '' or str

    # Test share object
    def test_share(self, param_test):
        (json) = param_test

        response_url = json_parse(json, ["result", "category", "share", "url"])
        test_url = 'http://demo.ic8.link/%s' % ContextCategoryApiJson.category.lower()
        assert response_url == test_url

        response_share_preview = json_parse(json, ["result", "category", "share", "share_preview"])
        test_share_preview = 'https://demost.icons8.com/Share/category/%s.png' % ContextCategoryApiJson.category
        assert response_share_preview == test_share_preview

        response_icons_preview = json_parse(json, ["result", "category", "share", "icons_preview"])
        assert response_icons_preview.find(ContextCategoryApiJson.category.lower()), \
            '>>> %s - in response, %s - in request <<<' % (response_icons_preview, ContextCategoryApiJson.category)

    icon_numbers = []
    icon_count = len(json_parse(ContextCategoryApiJson.response_root_auth, ["result", "category", "icons"]))
    for icon_num in range(icon_count):
        icon_numbers.append(icon_num)

    @pytest.mark.parametrize("icon_number", icon_numbers)
    @pytest.mark.parametrize("json", [ContextCategoryApiJson.response_root, ContextCategoryApiJson.response_root_auth])
    # Test isons object
    def test_icons(self, icon_number, json):
        assert len(json_parse(json, ["result", "category", "icons", icon_number, "id"])) > 0
        assert len(json_parse(json, ["result", "category", "icons", icon_number, "name"])) > 2
        assert ContextCategoryApiJson.platform_list.count \
                   (json_parse(json, ["result", "category", "icons", icon_number, "platform"])) == 1
        assert ContextCategoryApiJson.platform_code_list.count \
                   (json_parse(json, ["result", "category", "icons", icon_number, "platform_code"])) == 1
        assert json_parse(json, ["result", "category", "icons", icon_number, "created"])[:2] == "20"
        assert len(json_parse(json, ["result", "category", "icons", icon_number, "created"])) > 15
        assert json_parse(json, ["result", "category", "icons", icon_number, "copyright"]) == False
        assert json_parse(json, ["result", "category", "icons", icon_number, "filled"]) == False or True
        assert json_parse(json, ["result", "category", "icons", icon_number, "disqus_url"])[
               :32] == 'https://demo.icons8.com/web-app/'
        assert len(json_parse(json, ["result", "category", "icons", icon_number, "common_icon_id"])) > 0
        assert len(json_parse(json, ["result", "category", "icons", icon_number, "categories", 0])) >= 2
        assert json_parse(json, ["result", "category", "icons", icon_number, "category"]) \
               == ContextCategoryApiJson.category
        assert json_parse(json, ["result", "category", "icons", icon_number, "category_api_code"]) \
               == ContextCategoryApiJson.category
        assert len(json_parse(json, ["result", "category", "icons", icon_number, "svg"])) > 40

    @pytest.mark.parametrize("icon_number", icon_numbers)
    @pytest.mark.parametrize("json", [ContextCategoryApiJson.response_root, ContextCategoryApiJson.response_root_auth])
    # Test isons subcategory object
    def test_icons_subcategory(self, icon_number, json):
        try:
            assert len(json_parse(json, ["result", "category", "icons", icon_number, "subcategory", "name"])) >= 2
            assert len(json_parse(json, ["result", "category", "icons", icon_number, "subcategory", "api_code"])) >= 2
        except KeyError:
            pass

    @pytest.mark.parametrize("icon_number", icon_numbers)
    @pytest.mark.parametrize("json", [ContextCategoryApiJson.response_root, ContextCategoryApiJson.response_root_auth])
    # Test isons png object
    def test_icons_png(self, icon_number, json):
        png_count = json_parse(json, ["result", "category", "icons", icon_number, "png"])
        for png in range(len(png_count)):
            assert json_parse(json, ["result", "category", "icons", icon_number, "png", png, "width"]) > 20
            assert json_parse(json, ["result", "category", "icons", icon_number, "png", png, "height"]) > 20
            link = json_parse(json, ["result", "category", "icons", icon_number, "png", png, "link"])
            assert link.find(ContextCategoryApiJson.category), \
                '>>> %s - in response, %s - in request <<<' % (link, ContextCategoryApiJson.category)

    @pytest.mark.parametrize("icon_number", icon_numbers)
    @pytest.mark.parametrize("json", [ContextCategoryApiJson.response_root, ContextCategoryApiJson.response_root_auth])
    # Test isons features object
    def test_icons_features(self, icon_number, json):
        for features in ["bitmap", "vector", "nolink"]:
            assert json_parse(json, ["result", "category", "icons", icon_number, "features", features]) == 0 or 1


    @pytest.mark.parametrize("icon_number", icon_numbers)
    @pytest.mark.parametrize("json", [ContextCategoryApiJson.response_root, ContextCategoryApiJson.response_root_auth])
    # Test share share object
    def test_icons_share(self, icon_number, json):
        assert json_parse(json, ["result", "category", "icons", icon_number, "share", "url"])[:20] == 'http://demo.ic8.link'
        try:
            assert json_parse(json, ["result", "category", "icons", icon_number, "share", "png",  1, "type"]) == 'twitter'
            assert json_parse(json, ["result", "category", "icons", icon_number, "share", "png", 2, "type"]) == 'social'
        except IndexError:
            pass
        link_count = len(json_parse(json, ["result", "category", "icons", icon_number, "share", "png"]))

        for link in range(link_count):
            assert json_parse(json, ["result", "category", "icons", icon_number, "share", "png", link, "link"])[:25] == 'https://demost.icons8.com'

