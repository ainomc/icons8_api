# -*- coding: utf-8 -*-

from api_logic import random_between_values, random_list_value, request, \
    all_tag_attrib, word_count, attrib_value, auth_id


class ContextCategoryApi(object):

    # settings
    api_type = 'category'

    category = random_list_value(["City", "Food", "Travel",
                                  "Transport", "Weather"])
    amount = random_list_value(["", "5", "10", "15", "20"])
    offset = random_list_value(["", "5", "10", "15", "20"])
    platform = random_list_value(["win8", "ios7", "android", "androidL",
                                  "color", "win10", "office"])
    attributes = ''

    payload = {'category': category, 'amount': amount,
               'offset': offset, 'platform': platform, 'attributes': attributes}
    payload_auth = {'category': category, 'amount': amount,
                          'offset': offset, 'platform': platform, 'attributes': attributes, 'auth-id': auth_id}

    print ('''Category v1 tests: category - %s, amount - %s , offset - %s, platform - %s, attributes - %s'''
           % (category, amount, offset, platform, attributes))

    icon_count = 100

    # Do Request and return response root
    response_root = request(api_type, payload, "v1", "xml")
    response_root_auth = request(api_type, payload_auth, "v1", "xml")

    icons_current_count = 0
    x = True
    while x == True:
        try:
            icons_current_count += 1
            tag_attribs = all_tag_attrib(response_root,
                                         'icon', str(icons_current_count))
            value_of_attrib = attrib_value(tag_attribs, 'id')
            assert word_count(value_of_attrib) >= 1
            assert icons_current_count <= icon_count
        except AttributeError:
            x = False
            icons_current_count -= 1
            assert icons_current_count > 0

    # Choose random icon between min and max
    icon_number = str(random_between_values(1, icons_current_count))

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")