# -*- coding: utf-8 -*-

import paramiko

from api_logic import random_between_values, random_list_value, request, all_tag_attrib, word_count, attrib_value


class ContextSuggestApi(object):

    #settings
    api_type = 'suggest'

    term = random_list_value(['google', 'facebook', 'space',
                              'ball', 'car'])

    amount = random_list_value(["", "5", "10", "15", "20"])

    platform = random_list_value(["win8", "ios7", "android", "androidL",
                                  "color", "win10", "office"])

    payload = {'term': term, 'amount': amount, 'platform': platform}

    print ('''Suggest tests: term - %s, amount - %s, platform - %s'''
           % (term, amount, platform))

    term_count = 25

    # Do Request and return response root
    response_root = request(api_type, payload)

    term_current_count = 0
    x = True
    while x == True:
        try:
            term_current_count += 1
            tag_attribs = all_tag_attrib(response_root,
                                         'suggests/term', str(term_current_count))
            value_of_attrib = attrib_value(tag_attribs, 'count')
            assert word_count(value_of_attrib) >= 1
            assert term_current_count <= term_count
        except AttributeError:
            x = False
            term_current_count -= 1
            assert term_current_count > 0
    # Choose random icon between min and max
    if term_current_count == 2:
        term_number = term_current_count
    else:
        term_number = str(random_between_values(2, term_current_count))

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")