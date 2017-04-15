# -*- coding: utf-8 -*-

import random

from api_logic import random_between_values, request, auth_id


class ContextIconApiJson(object):

    # Settings
    # icon id what will be in request
    icon_id = random.choice([str(random_between_values(0, 7500)),
                             str(random_between_values(9500, 20000))])

    format = "json"
    files = "eps,svg"
    variants = "enabled"
    info = "enabled"

    print ('''Icon v2 Json tests: id - %s, files - %s, variants - %s, info - %s''' % (icon_id, files, variants, info))

    payload = {'id': icon_id, 'format': format, 'files': files,
               'variants': variants, 'info': info}
    payload_auth = {'id': icon_id, 'format': format, 'files': files,
                    'variants': variants, 'info': info, 'auth-id': auth_id}

    # Do Request and return response root
    response_root = request('icon', payload, "v2", "json")
    response_root_auth = request('icon', payload_auth, "v2", "json")

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