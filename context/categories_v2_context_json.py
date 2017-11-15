# -*- coding: utf-8 -*-

from api_logic import random_between_values, request, random_list_value, auth_id


class ContextCategoriesApiJson(object):

    # icon id what will be in request



    platform = random_list_value(["win8", "ios7", "android", "androidL","color", "win10", "office"])

    print ('''Categories v2 Json tests: platform - %s'''
           % (platform))

    payload = {'platform': platform}
    payload_auth = {'platform': platform, 'auth-id': auth_id}

    # Do Request and return response root
    response_root = request('categories', payload, "v2", "json")
    response_root_auth = request('categories', payload_auth, "v2", "json")

    platform_list = ["Windows 8/Metro", "iPhone/iOS 10", "Android 4",
                     "Android L", "Color", "Windows 10/Threshold", "Office",
                     "Material", "Gradient", "Ultraviolet", "Nolan",
                     "DottyDots", "Red Short Lines", "iPhone/iOS 11",
                     "iPhone/iOS", "Metro", "1em", "Dusk_Wired", "ios11"]
    platform_code_list = ["win8", "ios7", "android", "androidL", "color",
                          "win10", "office", "p1em", "gradient", "ultraviolet",
                          "red_lines", "nolan", "dotty", "1em", "dusk",
                          "wired", "Dusk_Wired", "cotton", "ios11"]

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")