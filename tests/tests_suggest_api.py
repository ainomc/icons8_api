# -*- coding: utf-8 -*-

import pytest
import paramiko

from icons8_api.api_logic import attrib_value, tag_value, all_tag_attrib, word_count
from icons8_api.api_context import ContextSuggestApi


"""
python -m pytest -v tests_suggest_api.py -s     --   runner

"""


# Test Search Api with Default values. https://demoapi.icons8.com/manual/suggest
class TestSuggestApi(ContextSuggestApi):


    # Test 'search' tag
    def test_search_tag(self):

        print(ContextSuggestApi.term + ' - term')
        print(ContextSuggestApi.amount + ' - amount')
        print(ContextSuggestApi.platform + ' - platform')

        tag_attribs = all_tag_attrib(ContextSuggestApi.response_root,
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
    def test_term_first_tag(self):
        tag_attribs = all_tag_attrib(ContextSuggestApi.response_root, 'term', ContextSuggestApi.term_number)
        value_of_attrib = attrib_value(tag_attribs, 'count')
        assert word_count(value_of_attrib) >= 1

        value_of_tag = tag_value(ContextSuggestApi.response_root, 'term', ContextSuggestApi.term_number)
        assert value_of_tag.lower().startswith(ContextSuggestApi.term)

    # Test 'term' random tag
    def test_term_random_tag(self):
        tag_attribs = all_tag_attrib(ContextSuggestApi.response_root, 'term', ContextSuggestApi.term_number)
        value_of_attrib = attrib_value(tag_attribs, 'count')
        assert word_count(value_of_attrib) >= 1

        value_of_tag = tag_value(ContextSuggestApi.response_root, 'term', ContextSuggestApi.term_number)
        assert value_of_tag.lower().startswith(ContextSuggestApi.term)
