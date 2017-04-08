# -*- coding: utf-8 -*-

import pytest

from api_logic import json_parse, word_count
from context.icon_context_json import ContextIconApiJson


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

        assert json_parse(json, ["parameters", "id"]) == ContextIconApiJson.icon_id\
            , ">>> 1rs - 'id' in response, 2rs - in request <<<"
        assert json_parse(json, ["parameters", "format"]) == ContextIconApiJson.format, \
            ">>> 1rs - 'format' in response, 2rs - in request <<<"
        assert json_parse(json, ["parameters", "files"]) == ContextIconApiJson.files, \
            ">>> 1rs - 'files' in response, 2rs - in request <<<"
        assert json_parse(json, ["parameters", "variants"]) == True, \
            ">>> 1rs - 'variants' in response, 2rs - in request <<<"
        assert json_parse(json, ["parameters", "info"]) == True, \
            ">>> 1rs - 'info' in response, 2rs - in request <<<"
        assert json_parse(json, ["parameters", "impresser_preview"]) == False, \
            ">>> 1rs - 'impresser_preview' in response, 2rs - in request <<<"
        assert json_parse(json, ["parameters", "language"]) == None, \
            ">>> 1rs - 'language' in response, 2rs - in request <<<"

    # Test result/icon object
    def test_result_icon_object(self, param_test):
        (json) = param_test

        assert len(json_parse(json, ["result", "icons", 0, "name"])) > 1, ">>> word count of 'name' > 1 <<<"

        platform = json_parse(json, ["result", "icons", 0, "platform"])
        assert ContextIconApiJson.platform_list.count(platform) == 1\
            , ">>> %s - not know this platform <<<" % platform

        platform_code = json_parse(json, ["result", "icons", 0, "platform_code"])
        assert ContextIconApiJson.platform_code_list.count(platform_code) == 1, \
            ">>> %s - not know this platform_code <<<" % platform_code

        assert json_parse(json, ["result", "icons", 0, "created"])[:2] == "20"
        assert len(json_parse(json, ["result", "icons", 0, "created"])) > 15
        assert json_parse(json, ["result", "icons", 0, "copyright"]) == False
        assert "icons8.com/web-app/" in json_parse(json, ["result", "icons", 0, "disqus_url"])
        assert len(json_parse(json, ["result", "icons", 0, "category"])) > 2
        assert len(json_parse(json, ["result", "icons", 0, "svg"])) > 40

    # Test subcategory object
    def test_subcategory_object(self, param_test):
        (json) = param_test
        try:
            assert len(json_parse(json, ["result", "icons", 0, "subcategory", "name"])) > 0
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
            assert 'https://' in json_parse(json, ["result", "icons", 0, "png", png, "link"])

    # Test features object
    def test_features_object(self, param_test):
        (json) = param_test
        for features in ["bitmap", "vector", "nolink"]:
            assert json_parse(json, ["result", "icons", 0, "features", features]) == 0 or 1

    # Test tags object
    def test_tags_object(self, param_test):
        (json) = param_test
        try:
            for tag in range(len(json_parse(json, ["result", "icons", 0, "tags"]))):
                assert len(json_parse(json, ["result", "icons", 0, "tags", tag])) > 0
        except KeyError:
            pass

    # Test share object
    def test_share_object(self, param_test):
        (json) = param_test
        assert ".ic8.link" in json_parse(json, ["result", "icons", 0, "share", "url"])
        assert "icons" in json_parse(json, ["result", "icons", 0, "share", "png", 0, "link"])
        for share in range(1, len(json_parse(json, ["result", "icons", 0, "share"]))):
            assert json_parse(json, ["result", "icons", 0, "share", "png", share, "type"]) == 'twitter' or 'social'
            assert "icons" in json_parse(json, ["result", "icons", 0, "share", "png", share, "link"])

    # Test request object
    def test_request_object(self, param_test):
        (json) = param_test
        try:
            assert len(json_parse(json, ["result", "icons", 0, "request", "text"])) > 1
            assert json_parse(json, ["result", "icons", 0, "request", "link"])[:22] == 'http://buzz.icons8.com'
            assert len(json_parse(json, ["result", "icons", 0, "request", "author"])) > 1
            assert json_parse(json, ["result", "icons", 0, "request", "created"])[:2] == '20'
            assert json_parse(json, ["result", "icons", 0, "request", "competed"])[:2] == '20'
        except KeyError:
            pass

    list_variants = []
    try:
        variants = len(json_parse(ContextIconApiJson.response_root,
                                 ["result", "icons", 0, "variants"]))
        variants_auth = len(json_parse(ContextIconApiJson.response_root_auth,
                                      ["result", "icons", 0, "variants"]))
        assert variants == variants_auth, ">>>  <<<"
        for variant in range(variants):
            list_variants.append(variant)
    except KeyError:
        pass
    if len(list_variants) > 0:

        @pytest.mark.parametrize("variant", list_variants)
        @pytest.mark.parametrize("json", [ContextIconApiJson.response_root, ContextIconApiJson.response_root_auth])

        # Test result/icon object
        def test_variants_icon(self, variant, json):

            assert len(json_parse(json, ["result", "icons", 0, "variants", variant, "name"])) > 0, ">>>  <<<"

            platform = json_parse(json, ["result", "icons", 0, "variants", variant, "platform"])
            assert ContextIconApiJson.platform_list.count(platform) == 1, \
                ">>> %s - not know this platform <<<" % platform

            platform_code = json_parse(json, ["result", "icons", 0, "variants", variant, "platform_code"])
            assert ContextIconApiJson.platform_code_list.count(platform_code) == 1,\
                ">>> %s - not know this platform <<<" % platform

            assert json_parse(json, ["result", "icons", 0, "variants", variant, "created"])[:2] == "20"
            assert len(json_parse(json, ["result", "icons", 0, "variants", variant, "created"])) > 15
            assert json_parse(json, ["result", "icons", 0, "variants", variant, "copyright"]) == False
            assert json_parse(json, ["result", "icons", 0, "variants", variant, "filled"]) == False or True
            assert ".icons8.com/web-app/" in json_parse(json, ["result", "icons", 0, "variants", variant, "disqus_url"])
            assert len(json_parse(json, ["result", "icons", 0, "variants", variant, "category"])) > 2
            assert len(json_parse(json, ["result", "icons", 0, "variants", variant, "svg"])) > 40

        @pytest.mark.parametrize("variant", list_variants)
        @pytest.mark.parametrize("json", [ContextIconApiJson.response_root, ContextIconApiJson.response_root_auth])
        # Test subcategory object
        def test_var_subcategory(self, variant, json):
            try:
                assert len(json_parse(json, ["result", "icons", 0, "variants", variant, "subcategory", "name"])) > 0
                assert len(json_parse(json, ["result", "icons", 0, "variants", variant, "subcategory", "api_code"])) > 1
            except KeyError:
                pass

        @pytest.mark.parametrize("variant", list_variants)
        @pytest.mark.parametrize("json", [ContextIconApiJson.response_root, ContextIconApiJson.response_root_auth])
        # Test png object
        def test_var_png(self, variant, json):
            png_count = json_parse(json, ["result", "icons", 0, "variants", variant, "png"])
            for png in range(len(png_count)):
                assert json_parse(json, ["result", "icons", 0, "variants", variant, "png", png, "width"]) > 15, ">>>  <<<"
                assert json_parse(json, ["result", "icons", 0, "variants", variant, "png", png, "height"]) > 15, ">>>  <<<"
                assert 'https://' in json_parse(json, ["result", "icons", 0, "variants", variant, "png", png, "link"])

        @pytest.mark.parametrize("variant", list_variants)
        @pytest.mark.parametrize("json", [ContextIconApiJson.response_root, ContextIconApiJson.response_root_auth])
        # Test features object
        def test_var_features(self, variant, json):
            for features in ["bitmap", "vector", "nolink"]:
                assert json_parse(json, ["result", "icons", 0, "variants", variant, "features", features]) == 0 or 1

        @pytest.mark.parametrize("variant", list_variants)
        @pytest.mark.parametrize("json", [ContextIconApiJson.response_root, ContextIconApiJson.response_root_auth])
        # Test tags object
        def test_var_tags(self, variant, json):
            try:
                for tag in range(len(json_parse(json, ["result", "icons", 0, "variants", variant, "tags"]))):
                    assert len(json_parse(json, ["result", "icons", 0, "variants", variant, "tags", tag])) > 0
            except KeyError:
                pass

        @pytest.mark.parametrize("variant", list_variants)
        @pytest.mark.parametrize("json", [ContextIconApiJson.response_root, ContextIconApiJson.response_root_auth])
        # Test share object
        def test_var_share(self, variant, json):
            assert ".ic8.link" in json_parse(json, ["result", "icons", 0, "variants", variant, "share", "url"])
            assert "icons" in json_parse(json, ["result", "icons", 0, "variants", variant, "share", "png", 0, "link"])
            for share in range(1, len(json_parse(json, ["result", "icons", 0, "variants", variant, "share"]))):
                try:
                    assert json_parse(json, ["result", "icons", 0, "variants", variant,
                                             "share", "png", share, "type"]) == 'twitter' or 'social'
                    assert "icons" in json_parse(json, ["result", "icons", 0, "variants", variant,
                                             "png", share, "link"])
                except IndexError:
                    pass

        @pytest.mark.parametrize("variant", list_variants)
        @pytest.mark.parametrize("json", [ContextIconApiJson.response_root, ContextIconApiJson.response_root_auth])
        # Test request object
        def test_var_request(self, variant, json):
            try:
                assert len(json_parse(json, ["result", "icons", 0, "variants", variant,
                                             "request", "text"])) > 10, ">>>  <<<"
                assert json_parse(json, ["result", "icons", 0, "variants", variant,
                                         "request", "link"])[:22] == 'http://buzz.icons8.com'
                assert len(json_parse(json, ["result", "icons", 0, "request", "author"])) > 1
                assert json_parse(json, ["result", "icons", 0, "variants", variant,
                                         "request", "created"])[:2] == '20'
                assert json_parse(json, ["result", "icons", 0, "variants", variant,
                                         "request", "competed"])[:2] == '20'
            except KeyError:
                pass






















