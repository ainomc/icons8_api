# -*- coding: utf-8 -*-

from api_logic import random_between_values, random_list_value, request, \
    all_tag_attrib, word_count, attrib_value, auth_id


class ContextListApi(object):

    # settings
    api_type = 'list'

    search_platform = random_list_value(["win8", "ios7", "android", "gradient",
                                         "color", "win10", "office", "p1em", "", "ultraviolet"])
    platform_list = ["Windows 8/Metro", "iPhone/iOS 10", "iPhone/iOS 7", "Android", "Android L",
                     "Color", "Windows 10/Threshold", "Office", "Material", "Gradient",
                     "Ultraviolet", "Nolan", "DottyDots", "Red Short Lines",
                     "iPhone/iOS 11", "1em"]
    platform_code_list = ["win8", "ios7", "android", "androidL", "color",
                          "win10", "office", "p1em", "gradient", "ultraviolet",
                          "red_lines", "nolan", "dotty", "1em"]

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