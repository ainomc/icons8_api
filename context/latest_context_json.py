# -*- coding: utf-8 -*-

import pytest

from api_logic import random_between_values, request, random_list_value


class ContextLatestApiJson(object):

    # icon id what will be in request

    amount = random_list_value(["5", "10", "20"])
    platform = random_list_value(["win8", "ios7", "android", "gradient",
                                         "color", "win10", "office", "p1em"])
    offset = random_list_value(["5", "10", "15", "20"])
    impresser_preview = True
    language = 'en-US'

    print ('''Latest Json tests: latform - %s, platform - %s, offset - %s, impresser_preview - %s, language - %s'''
           % (amount, platform, offset, impresser_preview, language))

    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'
    payload = {'amount': amount, 'platform': platform, 'offset': offset,
               'impresser_preview': impresser_preview, 'language': language}
    payload_auth = {'amount': amount, 'platform': platform, 'offset': offset,
                    'impresser_preview': impresser_preview, 'language': language, 'auth-id': auth_id}

    # Do Request and return response root
    response_root = request('latest', payload, "v3", "json")
    response_root_auth = request('latest', payload_auth, "v3", "json")

    platform_list = ["Windows 8/Metro", "iPhone/iOS 10", "Android 4", "Android L",
                     "Color", "Windows 10/Threshold", "Office", "Material", "Gradient"]

    platform_code_list = ["win8", "ios7", "android", "gradient",
                                         "color", "win10", "office", ""]

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")