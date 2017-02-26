# -*- coding: utf-8 -*-

import pytest

from icons8_api.api_logic import attrib_value, tag_value, all_tag_attrib, word_count
from context.suggest_context import ContextSuggestApi


@pytest.fixture(scope="function", params=[
    (ContextSuggestApi.response_root),
    (ContextSuggestApi.response_root_auth)
])
def param_test(request):
    return request.param


# Test Search Api with Default values. https://demoapi.icons8.com/manual/suggest
class TestSuggestApi(ContextSuggestApi):

    # Test 'search' tag
    def test_search_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root,
                                     'search', '1')
        value_of_attrib = attrib_value(tag_attribs, 'term')
        assert value_of_attrib == ContextSuggestApi.term

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert value_of_attrib == ContextSuggestApi.platform

        value_of_attrib = attrib_value(tag_attribs, 'amount')
        if ContextSuggestApi.amount == '':
            ContextSuggestApi.amount = '25'
        assert value_of_attrib == ContextSuggestApi.amount

    # Test 'term' first tag
    def test_term_first_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'term', ContextSuggestApi.term_number)
        value_of_attrib = attrib_value(tag_attribs, 'count')
        assert word_count(value_of_attrib) >= 1

        value_of_tag = tag_value(root, 'term', ContextSuggestApi.term_number)
        assert value_of_tag.lower().startswith(ContextSuggestApi.term)

    # Test 'term' random tag
    def test_term_random_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'term', ContextSuggestApi.term_number)
        value_of_attrib = attrib_value(tag_attribs, 'count')
        assert word_count(value_of_attrib) >= 1

        value_of_tag = tag_value(root, 'term', ContextSuggestApi.term_number)
        assert value_of_tag.lower().startswith(ContextSuggestApi.term)
