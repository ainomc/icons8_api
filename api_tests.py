# -*- coding: utf-8 -*-

import pytest
import paramiko

from api_logic import tag_value, attrib_value, all_tag_attrib, all_tag_attrib_with_icon_number, tag_value_with_icon_number
from api_logic import word_count, check_all_categories, random_list_value, request, random_between_values
from api_context import ContextIconApi, ContextSearchDefaultApi, ContextSearchMaxApi, ContextSearchMinApi


"""
api_context - file with fixtures and settings
api_logic - file with main logic of tests
One class - tested one response with some values
One test method - test one xml tag and in one tag can be 2+ attributes

python -m pytest -v api_tests.py -s     --   runner

"""



# Test icon API https://demoapi.icons8.com/manual/icon
class TestIconApi(ContextIconApi):


    # Test 'resuilt' tag
    def test_resuilt_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'result', '1')
        value_of_attrib = attrib_value(tag_attribs, 'id')
        assert value_of_attrib == TestIconApi.icon_id

    # Test 'icon' tag
    def test_icon_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'icon', '1')
        value_of_attrib = attrib_value(tag_attribs, 'id')
        assert word_count(value_of_attrib) >= 1

        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert check_all_categories(value_of_attrib) == True

        value_of_attrib = attrib_value(tag_attribs, 'created')
        assert value_of_attrib[:2] == '20'

        value_of_attrib = attrib_value(tag_attribs, 'attributes')
        assert word_count(value_of_attrib) >= 0

        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert value_of_attrib[:9] == "/web-app/"

    # Test 'svg' tag
    def test_svg_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'svg', '1')
        assert word_count(value_of_tag) > 1

    # Test icon 26 tag
    def test_png_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'png/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'width')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'height')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'

    # Test 'bitmap' tag
    def test_bitmap_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'bitmap', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'vector' test
    def test_vector_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'features/vector', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'nolink' test
    def test_nolink_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'nolink', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'categories/category' test
    def test_categorychild_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'categories/category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'category' test
    def test_category_tag(self):
        value_of_tag = tag_value(TestIconApi.response_root, 'category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'share' tag
    def test_share_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'share', '1')
        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert value_of_attrib[:16] == "http://ic8.link/"

    # Test 'share/png' 1 tag
    def test_share_png_tag(self):
        tag_attribs = all_tag_attrib(TestIconApi.response_root, 'share/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'




# Test Search Api with Default values. https://demoapi.icons8.com/manual/search
class TestSearchDefaultApi(ContextSearchDefaultApi):


    # Check icons count in response.
    def test_icons_count(self):
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
                print (str(icons_current_count) + '<<< count icons in response')
                assert TestSearchDefaultApi.icon_count == icons_current_count


    # Test 'icon' tag
    def test_icon_tag(self):
        tag_attribs = all_tag_attrib(TestSearchDefaultApi.response_root,
                                     'icon', TestSearchDefaultApi.icon_number)
        value_of_attrib = attrib_value(tag_attribs, 'id')
        print (value_of_attrib + ' icon id what checked')
        assert word_count(value_of_attrib) >= 1

        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert check_all_categories(value_of_attrib) == True

        value_of_attrib = attrib_value(tag_attribs, 'created')
        assert value_of_attrib[:2] == '20'

        value_of_attrib = attrib_value(tag_attribs, 'attributes')
        assert word_count(value_of_attrib) >= 0

        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert value_of_attrib[:9] == "/web-app/"

    # Test 'svg' tag
    def test_svg_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchDefaultApi.response_root,
                                                  TestSearchDefaultApi.icon_number, 'svg', '1')
        assert word_count(value_of_tag) > 1

    # Test icon 26 tag
    def test_png_tag(self):
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchDefaultApi.response_root,
                                                      TestSearchDefaultApi.icon_number, 'png/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'width')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'height')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'

    # Test 'bitmap' tag
    def test_bitmap_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchDefaultApi.response_root,
                                                  TestSearchDefaultApi.icon_number, 'features/bitmap', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'vector' test
    def test_vector_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchDefaultApi.response_root,
                                                  TestSearchDefaultApi.icon_number, 'features/vector', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'nolink' test
    def test_nolink_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchDefaultApi.response_root,
                                                  TestSearchDefaultApi.icon_number, 'features/nolink', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'categories/category' test
    def test_categorychild_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchDefaultApi.response_root,
                                                  TestSearchDefaultApi.icon_number, 'categories/category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'category' test
    def test_category_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchDefaultApi.response_root,
                                                  TestSearchDefaultApi.icon_number, 'category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'share' tag
    def test_share_tag(self):
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchDefaultApi.response_root,
                                                      TestSearchDefaultApi.icon_number, 'share', '1')
        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert value_of_attrib[:16] == "http://ic8.link/"

    # Test 'share/png' 1 tag
    def test_share_png_tag(self):
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchDefaultApi.response_root,
                                                      TestSearchDefaultApi.icon_number, 'share/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'



class TestSearchMaxAPI(ContextSearchMaxApi):



    def test_search_tag(self):
        #print(TestSearchMaxAPI.icon_number + ' <<< icon number')
        tag_attribs = all_tag_attrib(TestSearchMaxAPI.response_root,
                                     'search', '1')
        value_of_attrib = attrib_value(tag_attribs, 'term')
        assert value_of_attrib == TestSearchMaxAPI.search_text

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert value_of_attrib == TestSearchMaxAPI.search_platform

        value_of_attrib = attrib_value(tag_attribs, 'amount')
        assert value_of_attrib == TestSearchMaxAPI.search_amount

        value_of_attrib = attrib_value(tag_attribs, 'offset')
        assert value_of_attrib == TestSearchMaxAPI.search_offset

        value_of_attrib = attrib_value(tag_attribs, 'language')
        assert value_of_attrib == TestSearchMaxAPI.search_language


    # Test 'icon' tag
    def test_icon_tag(self):
        tag_attribs = all_tag_attrib(TestSearchMaxAPI.response_root,
                                     'icon', TestSearchMaxAPI.icon_number)
        value_of_attrib = attrib_value(tag_attribs, 'id')
        print (value_of_attrib + ' icon id what checked')
        assert word_count(value_of_attrib) >= 1

        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert check_all_categories(value_of_attrib) == True

        value_of_attrib = attrib_value(tag_attribs, 'created')
        assert value_of_attrib[:2] == '20'

        value_of_attrib = attrib_value(tag_attribs, 'attributes')
        assert word_count(value_of_attrib) >= 0

        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert value_of_attrib[:9] == "/web-app/"

    # Test 'svg' tag
    def test_svg_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchMaxAPI.response_root,
                                                  TestSearchMaxAPI.icon_number, 'svg', '1')
        assert word_count(value_of_tag) > 1

    # Test icon 26 tag
    def test_png_tag(self):
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchMaxAPI.response_root,
                                                      TestSearchMaxAPI.icon_number, 'png/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'width')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'height')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'

    # Test 'bitmap' tag
    def test_bitmap_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchMaxAPI.response_root,
                                                  TestSearchMaxAPI.icon_number, 'features/bitmap', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'vector' test
    def test_vector_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchMaxAPI.response_root,
                                                  TestSearchMaxAPI.icon_number, 'features/vector', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'nolink' test
    def test_nolink_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchMaxAPI.response_root,
                                                  TestSearchMaxAPI.icons_current_count, 'features/nolink', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'categories/category' test
    def test_categorychild_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchMaxAPI.response_root,
                                                  TestSearchMaxAPI.icon_number, 'categories/category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'category' test
    def test_category_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchMaxAPI.response_root,
                                                  TestSearchMaxAPI.icon_number, 'category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'share' tag
    def test_share_tag(self):
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchMaxAPI.response_root,
                                                      TestSearchMaxAPI.icon_number, 'share', '1')
        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert value_of_attrib[:16] == "http://ic8.link/"

    # Test 'share/png' 1 tag
    def test_share_png_tag(self):
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchMaxAPI.response_root,
                                                      TestSearchMaxAPI.icon_number, 'share/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'



class TestSearchMinAPI(ContextSearchMinApi):


    # Check icons count in response.
    def test_icons_count(self):
        icons_current_count = 0
        x = True
        while x ==True:
            try:
                icons_current_count += 1
                tag_attribs = all_tag_attrib(TestSearchMinAPI.response_root,
                                             'icon', str(icons_current_count))
                value_of_attrib = attrib_value(tag_attribs, 'id')
                assert word_count(value_of_attrib) >= 1
                assert icons_current_count <= TestSearchMinAPI.icon_count
            except AttributeError:
                x = False
                icons_current_count -= 1
                print (str(icons_current_count) + '<<< count icons in response')
                assert TestSearchMinAPI.icon_count == icons_current_count

    def test_search_tag(self):
        tag_attribs = all_tag_attrib(TestSearchMinAPI.response_root,
                                     'search', '1')
        value_of_attrib = attrib_value(tag_attribs, 'term')
        assert value_of_attrib == TestSearchMinAPI.search_text

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert value_of_attrib == TestSearchMinAPI.search_platform

        value_of_attrib = attrib_value(tag_attribs, 'amount')
        assert value_of_attrib == TestSearchMinAPI.search_amount

        value_of_attrib = attrib_value(tag_attribs, 'offset')
        assert value_of_attrib == TestSearchMinAPI.search_offset

        value_of_attrib = attrib_value(tag_attribs, 'language')
        assert value_of_attrib == TestSearchMinAPI.search_language


    # Test 'icon' tag
    def test_icon_tag(self):
        tag_attribs = all_tag_attrib(TestSearchMinAPI.response_root,
                                     'icon', TestSearchMinAPI.icon_number)
        value_of_attrib = attrib_value(tag_attribs, 'id')
        print (value_of_attrib + ' icon id what checked')
        assert word_count(value_of_attrib) >= 1

        value_of_attrib = attrib_value(tag_attribs, 'name')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'platform')
        assert check_all_categories(value_of_attrib) == True

        value_of_attrib = attrib_value(tag_attribs, 'created')
        assert value_of_attrib[:2] == '20'

        value_of_attrib = attrib_value(tag_attribs, 'attributes')
        assert word_count(value_of_attrib) >= 0

        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert value_of_attrib[:9] == "/web-app/"

    # Test 'svg' tag
    def test_svg_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchMinAPI.response_root,
                                                  TestSearchMinAPI.icon_number, 'svg', '1')
        assert word_count(value_of_tag) > 1

    # Test icon 26 tag
    def test_png_tag(self):
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchMinAPI.response_root,
                                                      TestSearchMinAPI.icon_number, 'png/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'width')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'height')
        assert word_count(value_of_attrib) > 1

        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'

    # Test 'bitmap' tag
    def test_bitmap_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchMinAPI.response_root,
                                                  TestSearchMinAPI.icon_number, 'features/bitmap', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'vector' test
    def test_vector_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchMinAPI.response_root,
                                                  TestSearchMinAPI.icon_number, 'features/vector', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'nolink' test
    def test_nolink_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchMinAPI.response_root,
                                                  TestSearchMinAPI.icon_number, 'features/nolink', '1')
        assert word_count(value_of_tag) >= 1

    # Test 'categories/category' test
    def test_categorychild_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchMinAPI.response_root,
                                                  TestSearchMinAPI.icon_number, 'categories/category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'category' test
    def test_category_tag(self):
        value_of_tag = tag_value_with_icon_number(TestSearchMinAPI.response_root,
                                                  TestSearchMinAPI.icon_number, 'category', '1')
        assert word_count(value_of_tag) > 1

    # Test 'share' tag
    def test_share_tag(self):
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchMinAPI.response_root,
                                                      TestSearchMinAPI.icon_number, 'share', '1')
        value_of_attrib = attrib_value(tag_attribs, 'url')
        assert value_of_attrib[:16] == "http://ic8.link/"

    # Test 'share/png' 1 tag
    def test_share_png_tag(self):
        tag_attribs = all_tag_attrib_with_icon_number(TestSearchMinAPI.response_root,
                                                      TestSearchMinAPI.icon_number, 'share/png', '1')
        value_of_attrib = attrib_value(tag_attribs, 'link')
        assert value_of_attrib[-4:] == '.png'


