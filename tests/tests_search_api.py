# -*- coding: utf-8 -*-

import pytest

from api_logic import attrib_value, all_tag_attrib, all_tag_attrib_with_icon_number, \
    tag_value_with_icon_number, word_count
from context.search_context import ContextSearchDefaultApi, ContextSearchMaxApi, ContextSearchMinApi


@pytest.fixture(scope="function", params=[
    (ContextSearchDefaultApi.response_root),
    (ContextSearchDefaultApi.response_root_auth)
])
def param_test(request):
    return request.param

# Test Search Api with Default values. https://demoapi.icons8.com/manual/search
class TestSearchDefaultApi(ContextSearchDefaultApi):


    # Check icons count in response.
    def test_icons_count(self, param_test):
        (root) = param_test
        icons_current_count = 0
        x = True
        while x ==True:
            try:
                icons_current_count += 1
                tag_attribs = all_tag_attrib(TestSearchDefaultApi.response_root,
                                             'icon', str(icons_current_count))
                value_of_attrib = attrib_value(tag_attribs, 'id')
                assert word_count(value_of_attrib) >= 1
                assert icons_current_count <= TestSearchDefaultApi.icon_count
            except AttributeError:
                x = False
                icons_current_count -= 1
                assert TestSearchDefaultApi.icon_count == icons_current_count


    # Test 'icon' tag
    def test_icon_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(TestSearchDefaultApi.response_root,
                                     'icon', TestSearchDefaultApi.icon_number)
        value_of_attrib = attrib_value(tag_attribs, 'id')
        assert word_count(value_of_attrib) >= 1

        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert len(value_of_attrib) > 0

        value_of_attrib = attrib_value(tag_attribs, 'created')
        assert value_of_attrib[:2] == '20'

        value_of_attrib = attrib_value(tag_attribs, 'attributes')
        assert word_count(value_of_attrib) >= 0

        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert "/icon/" in value_of_attrib

    # Test 'svg' tag
    def test_svg_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(TestSearchDefaultApi.response_root,
                                                  TestSearchDefaultApi.icon_number, 'svg', '1')
        assert word_count(value_of_tag) > 1

    # Test icon 26 tag
    def test_png_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchDefaultApi.response_root,
                                                      TestSearchDefaultApi.icon_number, 'png/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'width')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'height')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'

    # Test 'bitmap' tag
    def test_bitmap_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(TestSearchDefaultApi.response_root,
                                                  TestSearchDefaultApi.icon_number, 'features/bitmap', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'vector' test
    def test_vector_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(TestSearchDefaultApi.response_root,
                                                  TestSearchDefaultApi.icon_number, 'features/vector', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'nolink' test
    def test_nolink_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(TestSearchDefaultApi.response_root,
                                                  TestSearchDefaultApi.icon_number, 'features/nolink', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'categories/category' test
    def test_categorychild_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(TestSearchDefaultApi.response_root,
                                                  TestSearchDefaultApi.icon_number, 'categories/category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'category' test
    def test_category_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(TestSearchDefaultApi.response_root,
                                                  TestSearchDefaultApi.icon_number, 'category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'share' tag
    def test_share_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchDefaultApi.response_root,
                                                      TestSearchDefaultApi.icon_number, 'share', '1')
        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert "ic8" in value_of_attrib

    # Test 'share/png' 1 tag
    def test_share_png_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchDefaultApi.response_root,
                                                      TestSearchDefaultApi.icon_number, 'share/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'


@pytest.fixture(scope="function", params=[
    (ContextSearchMaxApi.response_root),
    (ContextSearchMaxApi.response_root_auth)
])
def param_test(request):
    return request.param


class TestSearchMaxAPI(ContextSearchMaxApi):



    def test_search_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(TestSearchMaxAPI.response_root,
                                     'search', '1')
        value_of_attrib = attrib_value(tag_attribs, 'term')
        assert value_of_attrib == TestSearchMaxAPI.search_text, \
            '>>> 1rst - in response, 2nd - in request <<<'

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert value_of_attrib == TestSearchMaxAPI.search_platform, \
            '>>> 1rst - in response, 2nd - in request <<<'

        value_of_attrib = attrib_value(tag_attribs, 'amount')
        assert value_of_attrib == TestSearchMaxAPI.search_amount, \
            '>>> 1rst - in response, 2nd - in request <<<'

        value_of_attrib = attrib_value(tag_attribs, 'offset')
        assert value_of_attrib == TestSearchMaxAPI.search_offset, \
            '>>> 1rst - in response, 2nd - in request <<<'

        value_of_attrib = attrib_value(tag_attribs, 'language')
        assert value_of_attrib == TestSearchMaxAPI.search_language, \
            '>>> 1rst - in response, 2nd - in request <<<'


    # Test 'icon' tag
    def test_icon_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(TestSearchMaxAPI.response_root,
                                     'icon', TestSearchMaxAPI.icon_number)
        value_of_attrib = attrib_value(tag_attribs, 'id')
        assert word_count(value_of_attrib) >= 1

        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert len(value_of_attrib) > 0

        value_of_attrib = attrib_value(tag_attribs, 'created')
        assert value_of_attrib[:2] == '20'

        value_of_attrib = attrib_value(tag_attribs, 'attributes')
        assert word_count(value_of_attrib) >= 0

        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert "/icon/" in value_of_attrib

    # Test 'svg' tag
    def test_svg_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(TestSearchMaxAPI.response_root,
                                                  TestSearchMaxAPI.icon_number, 'svg', '1')
        assert word_count(value_of_tag) > 1

    # Test icon 26 tag
    def test_png_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchMaxAPI.response_root,
                                                      TestSearchMaxAPI.icon_number, 'png/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'width')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'height')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'

    # Test 'bitmap' tag
    def test_bitmap_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(TestSearchMaxAPI.response_root,
                                                  TestSearchMaxAPI.icon_number, 'features/bitmap', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'vector' test
    def test_vector_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(TestSearchMaxAPI.response_root,
                                                  TestSearchMaxAPI.icon_number, 'features/vector', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'nolink' test
    def test_nolink_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(TestSearchMaxAPI.response_root,
                                                  TestSearchMaxAPI.icons_current_count, 'features/nolink', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'categories/category' test
    def test_categorychild_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(TestSearchMaxAPI.response_root,
                                                  TestSearchMaxAPI.icon_number, 'categories/category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'category' test
    def test_category_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(TestSearchMaxAPI.response_root,
                                                  TestSearchMaxAPI.icon_number, 'category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'share' tag
    @pytest.mark.xfail
    def test_share_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchMaxAPI.response_root,
                                                      TestSearchMaxAPI.icon_number, 'share', '1')
        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert "ic8" in value_of_attrib

    # Test 'share/png' 1 tag
    @pytest.mark.xfail
    def test_share_png_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchMaxAPI.response_root,
                                                      TestSearchMaxAPI.icon_number, 'share/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'


@pytest.fixture(scope="function", params=[
    (ContextSearchMinApi.response_root),
    (ContextSearchMinApi.response_root_auth)
])
def param_test(request):
    return request.param

class TestSearchMinAPI(ContextSearchMinApi):


    # Check icons count in response.
    def test_icons_count(self, param_test):
        (root) = param_test
        icons_current_count = 0
        x = True
        while x == True:
            try:
                icons_current_count += 1
                tag_attribs = all_tag_attrib(ContextSearchMinApi.response_root,
                                             'icon', str(icons_current_count))
                value_of_attrib = attrib_value(tag_attribs, 'id')
                assert word_count(value_of_attrib) >= 1
                assert icons_current_count <= TestSearchMinAPI.icon_count
            except AttributeError:
                x = False
                icons_current_count -= 1
                assert TestSearchMinAPI.icon_count >= icons_current_count
                assert icons_current_count > 0


    def test_search_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(ContextSearchMinApi.response_root, 'search', '1')
        value_of_attrib = attrib_value(tag_attribs, 'term')
        assert value_of_attrib == TestSearchMinAPI.search_text, \
            '>>> 1rst - in ersponse, 2nd - in request <<<'

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert value_of_attrib == TestSearchMinAPI.search_platform, \
            '>>> 1rst - in ersponse, 2nd - in request <<<'

        value_of_attrib = attrib_value(tag_attribs, 'amount')
        assert value_of_attrib == TestSearchMinAPI.search_amount, \
            '>>> 1rst - in ersponse, 2nd - in request <<<'

        value_of_attrib = attrib_value(tag_attribs, 'offset')
        assert value_of_attrib == TestSearchMinAPI.search_offset, \
            '>>> 1rst - in ersponse, 2nd - in request <<<'

        value_of_attrib = attrib_value(tag_attribs, 'language')
        assert value_of_attrib == TestSearchMinAPI.search_language, \
            '>>> 1rst - in ersponse, 2nd - in request <<<'


    # Test 'icon' tag
    def test_icon_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(ContextSearchMinApi.response_root, 'icon',
                                     TestSearchMinAPI.icon_number)
        value_of_attrib = attrib_value(tag_attribs, 'id')
        assert word_count(value_of_attrib) >= 1

        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert len(value_of_attrib) > 0

        value_of_attrib = attrib_value(tag_attribs, 'created')
        assert value_of_attrib[:2] == '20'

        value_of_attrib = attrib_value(tag_attribs, 'attributes')
        assert word_count(value_of_attrib) >= 0

        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert "/icon/" in value_of_attrib

    # Test 'svg' tag
    def test_svg_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(ContextSearchMinApi.response_root,
                                                  TestSearchMinAPI.icon_number, 'svg', '1')
        assert word_count(value_of_tag) > 1

    # Test icon 26 tag
    def test_png_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib_with_icon_number(ContextSearchMinApi.response_root,
                                                      TestSearchMinAPI.icon_number, 'png/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'width')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'height')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'

    # Test 'bitmap' tag
    def test_bitmap_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(ContextSearchMinApi.response_root,
                                                  TestSearchMinAPI.icon_number, 'features/bitmap', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'vector' test
    def test_vector_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(ContextSearchMinApi.response_root,
                                                  TestSearchMinAPI.icon_number, 'features/vector', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'nolink' test
    def test_nolink_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(ContextSearchMinApi.response_root,
                                                  TestSearchMinAPI.icon_number, 'features/nolink', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'categories/category' test
    def test_categorychild_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(ContextSearchMinApi.response_root,
                                                  TestSearchMinAPI.icon_number, 'categories/category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'category' test
    def test_category_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value_with_icon_number(ContextSearchMinApi.response_root,
                                                  TestSearchMinAPI.icon_number, 'category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'share' tag
    def test_share_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib_with_icon_number(ContextSearchMinApi.response_root,
                                                      TestSearchMinAPI.icon_number, 'share', '1')
        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert "ic8" in value_of_attrib

    # Test 'share/png' 1 tag
    def test_share_png_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib_with_icon_number(ContextSearchMinApi.response_root,
                                                      TestSearchMinAPI.icon_number, 'share/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert '.png' in value_of_attrib[-4:]

