# -*- coding: utf-8 -*-

import pytest
import paramiko

from icons8_api.api_logic import attrib_value, tag_value, all_tag_attrib, word_count
from context.categories_context import ContextCategoriesApi


"""
python -m pytest -v tests_list_api.py -s     --   runner

"""

@pytest.fixture(scope="function", params=[
    (ContextCategoriesApi.response_root),
    (ContextCategoriesApi.response_root_auth)
])
def param_test(request):
    return request.param

# Test Search Api with Default values. https://demoapi.icons8.com/manual/suggest
class TestCategoriesApi(ContextCategoriesApi):

    # Test categories tag
    def test_categories_tag(self, param_test):
        (root) = param_test

        print(ContextCategoriesApi.search_platform + ' - platform')

        tag_attribs = all_tag_attrib(root,
                                            'categories', "1")

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert value_of_attrib == ContextCategoriesApi.search_platform


    # Test share tag
    def test_share_tag(self, param_test):
        (root) = param_test

        number = 1

        while True:
            try:
                tag_attribs = all_tag_attrib(root, 'category[%s]/share' % str(number), "1")

                value_of_attrib = attrib_value(tag_attribs, 'url')
                assert value_of_attrib[:20] == "http://demo.ic8.link"
                """
                value_of_attrib = attrib_value(tag_attribs, 'share_preview')
                assert value_of_attrib[:40] == 'https://demost.icons8.com/Share/category'

                value_of_attrib = attrib_value(tag_attribs, 'icons_preview')
                assert value_of_attrib[:46] == "https://demost.icons8.com/Share/category_icons"
                """
            except AttributeError or TypeError:
                break
            number += 1
        assert number > 30


    # Test category tag
    def test_category_tag(self, param_test):
        (root) = param_test
        number = 1
        while True:
            try:
                tag_attribs = all_tag_attrib(root,
                                         'category', str(number))
            except AttributeError:
                break
            value_of_attrib = attrib_value(tag_attribs, 'name')
            assert len(value_of_attrib) > 2
            number += 1
        assert number > 30

