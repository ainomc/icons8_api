# -*- coding: utf-8 -*-

import pytest

from api_logic import tag_value, attrib_value, all_tag_attrib, word_count
from context.icon_context import ContextIconApi


@pytest.fixture(scope="function", params=[
    (ContextIconApi.response_root),
    (ContextIconApi.response_root_auth)
])
def param_test(request):
    return request.param

# Test icon API https://demoapi.icons8.com/manual/icon
class TestIconApi(ContextIconApi):

    # Test 'resuilt' tag
    def test_resuilt_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'result', '1')
        value_of_attrib = attrib_value(tag_attribs, 'id')
        assert value_of_attrib == TestIconApi.icon_id, '>>> 1rs - id in response, 2rs - in request <<<'

    # Test 'icon' tag
    def test_icon_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'icon', '1')
        value_of_attrib = attrib_value(tag_attribs, 'id')
        assert word_count(value_of_attrib) >= 1, '>>> word count of id = 0 <<<'

        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert word_count(value_of_attrib) > 0, '>>> word count of name = 0 <<<'

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert len(value_of_attrib) > 0

        value_of_attrib = attrib_value(tag_attribs, 'created')
        assert value_of_attrib[:2] == '20', '>>> "created" not start from "20" <<<'

        value_of_attrib = attrib_value(tag_attribs, 'attributes')
        assert word_count(value_of_attrib) >= 0

        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert "/icon/" in value_of_attrib, '>>> "url" not start from "/icon/" <<<'

    # Test 'svg' tag
    def test_svg_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value(root, 'svg', '1')
        assert word_count(value_of_tag) > 1, '>>> word count of "svg" < 1 <<<'

    # Test icon 26 tag
    def test_png_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'png/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'width')
        assert word_count(value_of_attrib) > 1, '>>> word count of "width" < 1 <<<'

        value_of_attrib = attrib_value(tag_attribs, 'height')
        assert word_count(value_of_attrib) > 1, '>>> word count of "height" < 1 <<<'

        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png', '>>> link not end of ".png" <<<'

    # Test 'bitmap' tag
    def test_bitmap_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value(root, 'bitmap', '1')
        assert word_count(value_of_tag) >= 1, '>>> word count of "bitmap" == 0  <<<'

    # Test 'vector' test
    def test_vector_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value(root, 'features/vector', '1')
        assert word_count(value_of_tag) >= 1, '>>> word count of "features/vector" == 0 <<<'

    # Test 'nolink' test
    def test_nolink_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value(root, 'nolink', '1')
        assert word_count(value_of_tag) >= 1, '>>> word count of "nolink" == 0 <<<'

    # Test 'categories/category' test
    def test_categorychild_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value(root, 'categories/category', '1')
        assert word_count(value_of_tag) > 1, '>>> word count of "categories/category" < 1 <<<'

    # Test 'category' test
    def test_category_tag(self, param_test):
        (root) = param_test
        value_of_tag = tag_value(root, 'category', '1')
        assert word_count(value_of_tag) > 1, '>>> word count of "category" < 1 <<<'

    # Test 'share' tag
    def test_share_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'share', '1')
        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert ".ic8." in value_of_attrib, '>>> "url" not start from "http://demo.ic8." <<<'

    # Test 'share/png' 1 tag
    def test_share_png_tag(self, param_test):
        (root) = param_test
        tag_attribs = all_tag_attrib(root, 'share/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert '.png' in value_of_attrib, '>>> "link" not start from ".png" <<<'




