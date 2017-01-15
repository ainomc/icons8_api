# -*- coding: utf-8 -*-

import paramiko

from api_logic import random_between_values, random_list_value, request, all_tag_attrib, word_count, attrib_value


class ContextSearchDefaultApi(object):

    #settings
    api_type = 'search'

    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'

    term = random_list_value(['google', 'facebook', 'space',
                              'ball', 'car', 'word'])

    payload = {'term': term, 'amount': '', 'offset': '', 'platform': ''}

    payload_auth = {'term': term, 'amount': '', 'offset': '', 'platform': '', 'auth-id': auth_id}

    print ('''Search default tests: term - %s, amount - %s , offset - %s, platform - %s'''
           % (term, '', '', ''))

    icon_count = 25

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
            #print (str(icons_current_count) + '<<< count icons in response')
            assert icons_current_count > 0
    #print (str(icons_current_count) + ' <<< current count of icons')

    # Choose random icon between min and max
    icon_number = str(random_between_values(1, icon_count))

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")



class ContextSearchMaxApi(object):


    #settings
    api_type = 'search'

    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'

    search_text = random_list_value(['google', 'facebook', 'space',
                                     'ball', 'car', 'word'])

    search_amount = '20'

    search_offset = '20'

    search_platform = random_list_value(["win8", "ios7", "android", "androidL",
                                         "color", "win10", "office"])

    search_language = ''

    payload = {
        'term': search_text, 'amount': search_amount,
        'offset': search_offset, 'platform': search_platform
    }

    payload_auth = {
        'term': search_text, 'amount': search_amount,
        'offset': search_offset, 'platform': search_platform, 'auth-id': auth_id
    }

    print ('''Search max tests: term - %s, amount - %s , offset - %s, platform - %s'''
           % (search_text, search_amount, search_offset, search_platform))

    icon_count = 20

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
            print (str(icons_current_count) + '<<< count icons in response (IconTests)')
            assert icons_current_count > 0
    print (str(icons_current_count) + ' <<< current count of icons (IconTests)')

    # Choose random icon between min and max
    if icons_current_count == 2:
        icon_number = icons_current_count
    else:
        icon_number = str(random_between_values(1, icons_current_count))

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")


class ContextSearchMinApi(object):

    #settings
    api_type = 'search'

    search_text = random_list_value(['google', 'facebook', 'space',
                                     'ball', 'car', 'word'])
    search_amount = '5'

    search_offset = '5'

    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'

    search_platform = random_list_value(["win8", "ios7", "android", "androidL",
                                         "color", "win10", "office"])
    search_language = ''

    payload = {
        'term': search_text, 'amount': search_amount,
        'offset': search_offset, 'platform': search_platform
    }

    payload_auth = {
        'term': search_text, 'amount': search_amount,
        'offset': search_offset, 'platform': search_platform, 'auth-id': auth_id
    }

    print ('''Search min tests: term - %s, amount - %s , offset - %s, platform - %s'''
           % (search_text, search_amount, search_offset, search_platform))

    icon_count = 5

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
            #print (str(icons_current_count) + '<<< count icons in response')
            assert icons_current_count > 0
    #print (str(icons_current_count) + ' <<< current count of icons')

    # Choose random icon between min and max
    icon_number = str(random_between_values(1, icon_count))

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")