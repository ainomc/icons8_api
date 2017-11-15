# -*- coding: utf-8 -*-

from api_logic import random_between_values, request, random_list_value, auth_id


class ContextTotalApiJson(object):

    # icon id what will be in request
    year = random_list_value(["14", "15", "16"])
    month =  random_between_values(1, 12)
    day = random_between_values(1, 31)
    since = '20%s-%s-%s' % (year, month, day)
    print ('''Total v2 Json tests: since - %s'''
           % (since))
    payload = {'since': since}
    payload_auth = {'since': since, 'auth-id': auth_id}

    # Do Request and return response root
    response_root = request('total', payload, "v3", "json")
    response_root_auth = request('total', payload_auth, "v3", "json")
    platform_list = ["Windows 8/Metro", "iPhone/iOS 10", "Android 4",
                     "Android L", "Color", "Windows 10/Threshold", "Office",
                     "Material", "Gradient", "Ultraviolet", "Nolan",
                     "DottyDots", "Red Short Lines", "iPhone/iOS 11",
                     "iPhone/iOS", "Metro", "1em", "Dusk_Wired", "ios11",
                     "Ice Cream", "Dusk", "Dotty Dots", "Wired",
                     "iOS Tab Bar Icons (Glyphs)"]
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