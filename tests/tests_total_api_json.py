# -*- coding: utf-8 -*-

import pytest

from icons8_api.api_logic import json_parse
from context.total_context_json import ContextTotalApiJson



"""
api_context - file with fixtures and settings
api_logic - file with main logic of tests
One class - tested one response with some values
One test method - test one xml tag and in one tag can be 2+ attributes

python -m pytest -v tests_icon_api.py -s     --   runner

"""

@pytest.fixture(scope="function", params=[
    (ContextTotalApiJson.response_root),
    (ContextTotalApiJson.response_root_auth)
])
def param_test(request):
    return request.param

# Test icon API https://demoapi.icons8.com/api/iconsets/v3/total
class TestTotaltpiJson(ContextTotalApiJson):

    # Test total object
    def test_parameters(self, param_test):
        (json) = param_test
        assert json_parse(json, ["parameters", "since"]) == ContextTotalApiJson.since

    total_numbers = []
    total_count = len(json_parse(ContextTotalApiJson.response_root_auth, ["result", "total"]))
    for total_num in range(total_count):
        total_numbers.append(total_num)

    @pytest.mark.parametrize("total_numbers", total_numbers)
    @pytest.mark.parametrize("json", [ContextTotalApiJson.response_root, ContextTotalApiJson.response_root_auth])
    # Test total object
    def test_total(self, total_numbers, json):
        assert ContextTotalApiJson.platform_list.count(
            json_parse(json, ["result", "total", total_numbers, "name"])) == 1
        assert ContextTotalApiJson.platform_code_list.count(
            json_parse(json, ["result", "total", total_numbers, "api_code"])) == 1
        assert json_parse(json, ["result", "total", total_numbers, "total"]) >= 0

