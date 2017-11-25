# -*- coding: utf-8 -*-

from api_logic import random_between_values, request, random_list_value, auth_id

class ContextCategoryv3ApiJson(object):

    # icon id what will be in request
    category = random_list_value(["Animals", "Sports", "Food", "Cinema"])
    amount = 10
    platform = random_list_value(["win8", "ios7", "android", "androidL",
                                  "color", "win10", "office"])

    print ('''Category v3 Json tests: category - %s, amount - %s, platform - %s'''
           % (category, amount, platform))

    payload = {'category': category, 'amount': amount,
               'platform': platform}
    payload_auth = {'category': category, 'amount': amount,
                    'platform': platform, 'auth-id': auth_id}

    # Do Request and return response root
    response_root = request('category', payload, "v3", "json")
    response_root_auth = request('category', payload_auth, "v3", "json")

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")