# -*- coding: utf-8 -*-

import pytest

from api_logic import json_parse
from context.total_context_json import ContextTotalApiJson


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
        name = json_parse(json, ["result", "total", total_numbers, "name"])

        assert ContextTotalApiJson.platform_list.count(name) == 1, name
        assert ContextTotalApiJson.platform_code_list.count(
            json_parse(json, ["result", "total", total_numbers, "api_code"])) == 1
        assert json_parse(json, ["result", "total", total_numbers, "total"]) >= 0

