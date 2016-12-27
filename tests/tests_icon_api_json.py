# -*- coding: utf-8 -*-

import pytest

from icons8_api.api_logic import json_parse, word_count
from context.icon_context_json import ContextIconApiJson



"""
api_context - file with fixtures and settings
api_logic - file with main logic of tests
One class - tested one response with some values
One test method - test one xml tag and in one tag can be 2+ attributes

python -m pytest -v tests_icon_api.py -s     --   runner

"""

@pytest.fixture(scope="function", params=[
    (ContextIconApiJson.response_root),
    (ContextIconApiJson.response_root_auth)
])
def param_test(request):
    return request.param

# Test icon API https://demoapi.icons8.com/api/iconsets/v2/icon
class TestIconApiJson(ContextIconApiJson):

    # Test parameters object
    def test_parameters_object(self, param_test):
        (json) = param_test

        assert json_parse(json, ["parameters", "id"]) == ContextIconApiJson.icon_id
        assert json_parse(json, ["parameters", "format"]) == ContextIconApiJson.format
        assert json_parse(json, ["parameters", "files"]) == ContextIconApiJson.files
        assert json_parse(json, ["parameters", "variants"]) == True
        assert json_parse(json, ["parameters", "info"]) == True
        assert json_parse(json, ["parameters", "impresser_preview"]) == False
        assert json_parse(json, ["parameters", "language"]) == None

    # Test result/icon object
    def test_result_icon_object(self, param_test):
        (json) = param_test

        #assert json_parse(json, ["result", "icons", 0, "id"]) == ContextIconApiJson.icon_id
        assert len(json_parse(json, ["result", "icons", 0, "name"])) > 2
        assert ContextIconApiJson.platform_list.count\
                   (json_parse(json, ["result", "icons", 0, "platform"])) == 1
        assert ContextIconApiJson.platform_code_list.count\
                   (json_parse(json, ["result", "icons", 0, "platform_code"])) == 1
        assert json_parse(json, ["result", "icons", 0, "created"])[:2] == "20"
        assert len(json_parse(json, ["result", "icons", 0, "created"])) > 15
        assert json_parse(json, ["result", "icons", 0, "copyright"]) == False
        assert json_parse(json, ["result", "icons", 0, "filled"]) == False or True
        #assert json_parse(json, ["result", "icons", 0, "url"]).find(ContextIconApiJson.icon_id) > 0
        #assert json_parse(json, ["result", "icons", 0, "disqus_url"]).find(ContextIconApiJson.icon_id) > 0
        assert json_parse(json, ["result", "icons", 0, "disqus_url"])[:32] == 'https://demo.icons8.com/web-app/'
        #assert len(json_parse(json, ["result", "icons", 0, "transcription"])) > 15
        assert len(json_parse(json, ["result", "icons", 0, "category"])) > 2
        assert len(json_parse(json, ["result", "icons", 0, "svg"])) > 40

    # Test subcategory object
    def test_subcategory_object(self, param_test):
        (json) = param_test
        try:
            assert len(json_parse(json, ["result", "icons", 0, "subcategory", "name"])) > 1
            assert len(json_parse(json, ["result", "icons", 0, "subcategory", "api_code"])) > 1
        except KeyError:
            pass


    # Test png object
    def test_png_object(self, param_test):
        (json) = param_test
        png_count = json_parse(json, ["result", "icons", 0, "png"])
        for png in range(len(png_count)):
            assert json_parse(json, ["result", "icons", 0, "png", png, "width"]) > 15
            assert json_parse(json, ["result", "icons", 0, "png", png, "height"]) > 15
            assert json_parse(json, ["result", "icons", 0, "png", png, "link"])[:12] == 'https://demo'

    # Test features object
    def test_features_object(self, param_test):
        (json) = param_test
        assert json_parse(json, ["result", "icons", 0, "features", "bitmap"]) == 0 or 1
        assert json_parse(json, ["result", "icons", 0, "features", "vector"]) == 0 or 1
        assert json_parse(json, ["result", "icons", 0, "features", "nolink"]) == 0 or 1

    # Test tags object
    def test_tags_object(self, param_test):
        (json) = param_test
        tags_count = json_parse(json, ["result", "icons", 0, "tags"])
        for tag in range(len(tags_count)):
            assert len(json_parse(json, ["result", "icons", 0, "tags", tag])) > 2

    # Test share object
    def test_share_object(self, param_test):
        (json) = param_test
        assert json_parse(json, ["result", "icons", 0, "share", "url"])[:20] == 'http://demo.ic8.link'





















