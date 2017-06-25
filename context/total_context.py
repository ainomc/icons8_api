# -*- coding: utf-8 -*-

from api_logic import random_between_values, random_list_value, request, auth_id


class ContextTotalApi(object):

    # settings
    api_type = 'total'

    year = random_list_value(["14", "15", "16"])
    month =  random_between_values(1, 12)
    day = random_between_values(1, 31)
    since = '20%s-%s-%s' % (year, month, day)
    payload = {'since': since}
    payload_auth = {'since': since, 'auth-id': auth_id}

    print ('''Total v1 tests: since - %s'''
           % (since))

    icon_count = 100

    # Do Request and return response root
    response_root = request(api_type, payload, "v1", "xml")
    response_root_auth = request(api_type, payload_auth, "v1", "xml")

    platform_list = ["Windows 8/Metro", "iPhone/iOS 10", "Android 4", "Android L",
                     "Color", "Windows 10/Threshold", "Office", "Material", "Gradient",
                     "Ultraviolet", "Nolan", "DottyDots", "Red Short Lines",
                     "iPhone/iOS 11", "cotton"]
    platform_code_list = ["win8", "ios7", "android", "androidL", "color",
                          "win10", "office", "p1em", "gradient", "ultraviolet",
                          "red_lines", "nolan", "dotty", "cotton"]

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")