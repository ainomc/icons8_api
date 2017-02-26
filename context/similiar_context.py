# -*- coding: utf-8 -*-

from api_logic import random_between_values, random_list_value, request, \
    all_tag_attrib, word_count, attrib_value, auth_id


class ContextSimilarApi(object):
    # settings
    api_type = 'similar'

    # icon id what will be in request
    icon_id = str(random_between_values(100, 20000))
    amount = random_list_value(["", "5"])
    offset = random_list_value(["", "5"])
    payload = {'id': icon_id, 'amount': amount, 'offset': offset}
    payload_auth = {'id': icon_id, 'amount': amount, 'offset': offset, 'auth-id': auth_id}

    print ('''Similiar v1 tests: id - %s, amount - %s , offset - %s'''
           % (icon_id, amount, offset))

    icon_count = 100

    # Do Request and return response root
    response_root = request(api_type, payload, "v1", "xml")
    response_root_auth = request(api_type, payload_auth, "v1", "xml")

    similiar_icons_current_count = 0

    x = True
    while x == True:
        try:
            similiar_icons_current_count += 1
            tag_attribs = all_tag_attrib(response_root,
                                         'icon', str(similiar_icons_current_count))
            value_of_attrib = attrib_value(tag_attribs, 'id')
            assert word_count(value_of_attrib) >= 1
            assert similiar_icons_current_count <= icon_count
        except AttributeError:
            x = False
            similiar_icons_current_count -= 1

    # Choose random icon between min and max
    if similiar_icons_current_count == 0:
        icon_number = 0
    else:
        icon_number = str(random_between_values(1, similiar_icons_current_count))

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")