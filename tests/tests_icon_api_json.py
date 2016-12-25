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

        assert json_parse(json, ["result", "icons", 0, "id"]) == ContextIconApiJson.icon_id
        assert len(json_parse(json, ["result", "icons", 0, "name"])) > 2
        assert len(json_parse(json, ["result", "icons", 0, "platform"])) > 2







