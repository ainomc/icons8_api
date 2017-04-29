# -*- coding: utf-8 -*-

from api_logic import random_between_values, request, random_list_value, auth_id


class ContextCategoryv3ApiJson(object):

    # icon id what will be in request
    term = random_list_value(["Animals", "Sports", "Food", "Cinema","Cultures"])
    amount = 10
    platform = random_list_value(["win8", "ios7", "android", "gradient",
                                         "color", "win10", "office", "p1em"])
    offset = 10

    print ('''Search v3 Json tests: term - %s, amount - %s, platform - %s, offset - %s'''
           % (term, amount, platform, offset))

    payload = {'term': term, 'amount': amount,
               'platform': platform, 'offset': offset}
    payload_auth = {'term': term, 'amount': amount, 'platform': platform,
                    'offset': offset, 'auth-id': auth_id}

    # Do Request and return response root
    response_root = request('search', payload, "v3", "json")
    response_root_auth = request('search', payload_auth, "v3", "json")

    platform_list = ["Windows 8/Metro", "iPhone/iOS 10", "Android 4", "Android L",
                     "Color", "Windows 10/Threshold", "Office", "Material", "Gradient",
                     "Ultraviolet", "Nolan", "DottyDots", "Red Short Lines"]

    platform_code_list = ["win8", "ios7", "android", "androidL", "color",
                          "win10", "office", "p1em", "gradient", "ultraviolet",
                          "red_lines", "nolan", "dotty"]

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")