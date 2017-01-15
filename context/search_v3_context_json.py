# -*- coding: utf-8 -*-

import pytest

from api_logic import random_between_values, request, random_list_value


class ContextCategoryv3ApiJson(object):

    # icon id what will be in request
    term = random_list_value(["Animals", "Sports", "Food", "Cinema","Cultures"])
    amount = 10
    platform = random_list_value(["win8", "ios7", "android", "androidL","color", "win10", "office"])
    offset = 10

    print ('''Category Json tests: term - %s, amount - %s, platform - %s, offset - %s'''
           % (term, amount, platform, offset))

    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'
    payload = {'term': term, 'amount': amount,
               'platform': platform, 'offset': offset}
    payload_auth = {'term': term, 'amount': amount, 'platform': platform,
                    'offset': offset, 'auth-id': auth_id}

    # Do Request and return response root
    response_root = request('search', payload, "v3", "json")
    response_root_auth = request('search', payload_auth, "v3", "json")

    platform_list = ["Windows 8/Metro", "iPhone/iOS 7", "Android", "Android L",
                     "Color", "Windows 10/Threshold", "Office"]

    platform_code_list = ["win8", "ios7", "android",
                          "androidL","color", "win10", "office"]

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")