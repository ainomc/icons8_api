# -*- coding: utf-8 -*-

import pytest

from icons8_api.api_logic import json_parse
from context.latest_context_json import ContextLatestApiJson


@pytest.fixture(scope="function", params=[
    (ContextLatestApiJson.response_root),
    (ContextLatestApiJson.response_root_auth)
])
def param_test(request):
    return request.param

# Test icon API https://demoapi.icons8.com/api/iconsets/v3/latest
class TestLatestpiJson(ContextLatestApiJson):

    # Test parameters object
    def test_parameters(self, param_test):
        (json) = param_test
        assert json_parse(json, ["parameters", "amount"]) == ContextLatestApiJson.amount
        assert json_parse(json, ["parameters", "offset"]) == ContextLatestApiJson.offset
        assert json_parse(json, ["parameters", "platform"]) == ContextLatestApiJson.platform
        assert json_parse(json, ["parameters", "impresser_preview"]) == str(ContextLatestApiJson.impresser_preview)
        assert json_parse(json, ["parameters", "language"]) == 'en'

    latest_numbers = []
    latest_count = len(json_parse(ContextLatestApiJson.response_root_auth, ["result", "latest"]))
    for latest_num in range(latest_count):
        latest_numbers.append(latest_num)

    @pytest.mark.parametrize("latest_numbers", latest_numbers)
    @pytest.mark.parametrize("json", [ContextLatestApiJson.response_root, ContextLatestApiJson.response_root_auth])
    # Test latest object
    def test_latest(self, latest_numbers, json):
        assert json_parse(json, ["result", "latest", latest_numbers, "id"]) >= 1
        assert len(json_parse(json, ["result", "latest", latest_numbers, "id"])) > 1
        assert json_parse(json, ["result", "latest", latest_numbers, "platform_code"]) == ContextLatestApiJson.platform
        assert json_parse(json, ["result", "latest", latest_numbers, "created"])[:2] == '20'
        assert len(json_parse(json, ["result", "latest", latest_numbers, "created"])) >= 25
        assert json_parse(json, ["result", "latest", latest_numbers, "url"])[:9] == '/web-app/'
        assert len(json_parse(json, ["result", "latest", latest_numbers, "common_icon_id"])) > 0
        assert len(json_parse(json, ["result", "latest", latest_numbers, "svg"])) > 20

    @pytest.mark.parametrize("latest_numbers", latest_numbers)
    @pytest.mark.parametrize("json", [ContextLatestApiJson.response_root, ContextLatestApiJson.response_root_auth])
    # Test latest png_preview object
    def test_latest_png_preview(self, latest_numbers, json):
        assert json_parse(json, ["result", "latest", latest_numbers, "png_preview", '50'])[:25] == 'https://demost.icons8.com'

    @pytest.mark.parametrize("latest_numbers", latest_numbers)
    @pytest.mark.parametrize("json", [ContextLatestApiJson.response_root, ContextLatestApiJson.response_root_auth])
    # Test latest features object
    def test_latest_features(self, latest_numbers, json):
        json_parse(json, ["result", "latest", latest_numbers, "features", 'bitmap']) == 1 or 0
        json_parse(json, ["result", "latest", latest_numbers, "features", 'vector']) == 1 or 0
        json_parse(json, ["result", "latest", latest_numbers, "features", 'nolink']) == 1 or 0

    @pytest.mark.parametrize("latest_numbers", latest_numbers)
    @pytest.mark.parametrize("json", [ContextLatestApiJson.response_root, ContextLatestApiJson.response_root_auth])
    # Test latest features object
    def test_latest_features(self, latest_numbers, json):
        assert json_parse(json, ["result", "latest", latest_numbers, "share", 'url'])[:20] == 'http://demo.ic8.link'
        for png in range(len(json_parse(json, ["result", "latest", latest_numbers, "share", 'png']))):
            assert json_parse(json, ["result", "latest", latest_numbers, "share", 'png', png, 'link'])[:25]\
                   == 'https://demost.icons8.com'
            if png > 1:
                json_parse(json, ["result", "latest", latest_numbers, "share", 'png', png, 'type']) == 'twitter' or 'social'







