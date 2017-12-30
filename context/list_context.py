# -*- coding: utf-8 -*-

from api_logic import random_between_values, random_list_value, request, \
    all_tag_attrib, word_count, attrib_value, auth_id


class ContextListApi(object):

    # settings
    api_type = 'list'

    search_platform = random_list_value(["android", "gradient",
                                         "color", "win10", ""])

    print ('''List v1 tests: search_platform - %s'''
           % search_platform)
    payload = {'platform': search_platform, 'auth-id': auth_id}

    response_root = request(api_type, payload, "v1", "xml")

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")