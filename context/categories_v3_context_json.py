# -*- coding: utf-8 -*-

from api_logic import random_between_values, request, random_list_value, auth_id


class ContextCategories3vApiJson(object):

    # icon id what will be in request

    platform = random_list_value(["win8", "ios7", "android", "androidL","color", "win10", "office"])

    print ('''Categories v3 Json tests: platform - %s'''
           % (platform))

    payload = {'platform': platform}
    payload_auth = {'platform': platform, 'auth-id': auth_id}

    # Do Request and return response root
    response_root = request('categories', payload, "v3", "json")
    response_root_auth = request('categories', payload_auth, "v3", "json")

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")