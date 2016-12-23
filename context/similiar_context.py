# -*- coding: utf-8 -*-

import paramiko

from api_logic import random_between_values, random_list_value, request, all_tag_attrib, word_count, attrib_value


class ContextSimilarApi(object):
    # settings
    api_type = 'similar'

    # icon id what will be in request
    icon_id = str(random_between_values(100, 20000))

    amount = random_list_value(["", "5"])

    #offset = random_list_value(["", "5", "10", "15", "20"])
    offset = random_list_value(["", "5"])
    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'

    payload = {'id': icon_id, 'amount': amount, 'offset': offset}
    payload_auth = {'id': icon_id, 'amount': amount, 'offset': offset, 'auth-id': auth_id}

    print ('''Similiar tests: id - %s, amount - %s , offset - %s'''
           % (icon_id, amount, offset))

    icon_count = 100

    # Do Request and return response root
    response_root = request(api_type, payload)
    response_root_auth = request(api_type, payload_auth)

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
            #print (str(icons_current_count) + '<<< count icons in response')
            if similiar_icons_current_count == 0:
                print (icon_id + " - has no any similiar icon")
    #print (str(icons_current_count) + ' <<< current count of icons')

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