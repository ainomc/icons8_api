# -*- coding: utf-8 -*-

import pytest

from api_logic import random_between_values, request, random_list_value


class ContextCategoryApiJson(object):

    # icon id what will be in request
    category = random_list_value(["Animals", "Sports", "Food", "Cinema","Cultures"])
    attributes = 'filled'
    amount = 10
    platform = random_list_value(["win8", "ios7", "android", "androidL","color", "win10", "office"])

    print ('''Category Json tests: category - %s, attributes - %s, amount - %s, platform - %s'''
           % (category, attributes, amount, platform))

    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'
    payload = {'category': category, 'attributes': attributes, 'amount': amount,
               'platform': platform}
    payload_auth = {'category': category, 'attributes': attributes, 'amount': amount,
                    'platform': platform, 'auth-id': auth_id}

    # Do Request and return response root
    response_root = request('category', payload, "v2", "json")
    response_root_auth = request('category', payload_auth, "v2", "json")

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