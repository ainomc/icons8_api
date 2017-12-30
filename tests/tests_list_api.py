# -*- coding: utf-8 -*-

import pytest

from api_logic import attrib_value, all_tag_attrib
from context.list_context import ContextListApi


# Test Search Api with Default values. https://demoapi.icons8.com/manual/suggest
class TestListApi(ContextListApi):
    if ContextListApi.search_platform == "":
        @pytest.mark.parametrize("num_tag",  range(1, 8))
        def test_list_tag(self, num_tag):
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', str(num_tag))
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert len(value_of_attrib) > 0

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"

    else:
        def test_list_tag(self):
            tag_attribs = all_tag_attrib(ContextListApi.response_root,
                                         'list/list', '1')
            value_of_attrib = attrib_value(tag_attribs, 'platform')
            assert len(value_of_attrib) > 0

            value_of_attrib = attrib_value(tag_attribs, 'format')
            assert value_of_attrib == "json"

            value_of_attrib = attrib_value(tag_attribs, 'link')
            assert value_of_attrib[-5:] == ".json"