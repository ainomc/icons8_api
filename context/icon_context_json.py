# -*- coding: utf-8 -*-

import pytest

from api_logic import random_between_values, request


class ContextIconApiJson(object):

    # Settings
    # icon id what will be in request
    while True:
        icon_id = str(random_between_values(100, 20000))
        if icon_id > 7500 and icon_id < 9500:
            pass
        else:
            break
    format = "json"
    files = "eps,svg"
    variants = "enabled"
    info = "enabled"

    print ('''Icon Json tests: id - %s, files - %s, variants - %s, info - %s''' % (icon_id, files, variants, info))

    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'

    payload = {'id': icon_id, 'format': format, 'files': files,
               'variants': variants, 'info': info}
    payload_auth = {'id': icon_id, 'format': format, 'files': files,
                    'variants': variants, 'info': info, 'auth-id': auth_id}

    # Do Request and return response root
    response_root = request('icon', payload, "v2", "json")
    response_root_auth = request('icon', payload_auth, "v2", "json")

    platform_list = ["Windows 8/Metro", "iPhone/iOS 7", "Android", "Android L",
                     "Color", "Windows 10/Threshold", "Office"]

    platform_code_list = ["win8", "ios7", "android",
                     "androidL","color", "win10", "office"]

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")