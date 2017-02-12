# -*- coding: utf-8 -*-

import pytest

from api_logic import random_between_values, request, random_list_value


class ContextCategoriesApiJson(object):

    # icon id what will be in request



    platform = random_list_value(["win8", "ios7", "android", "androidL","color", "win10", "office"])

    print ('''Category Json tests: latform - %s'''
           % (platform))

    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'
    payload = {'platform': platform}
    payload_auth = {'platform': platform, 'auth-id': auth_id}

    # Do Request and return response root
    response_root = request('categories', payload, "v2", "json")
    response_root_auth = request('categories', payload_auth, "v2", "json")

    platform_list = ["Windows 8/Metro", "iPhone/iOS 10", "Android 4", "Android L",
                     "Color", "Windows 10/Threshold", "Office", "Material", "1em", "Gradient"]

    platform_code_list = ["win8", "ios7", "android",
                          "androidL","color", "win10", "office"]

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")