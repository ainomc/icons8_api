# -*- coding: utf-8 -*-

import paramiko

from api_logic import random_between_values, random_list_value, request, all_tag_attrib, word_count, attrib_value


class ContextCategoriesApi(object):


    # settings
    api_type = 'categories'

    search_platform = random_list_value(["win8", "ios7", "android", "androidL",
                                         "color", "win10", "office", ""])
    #search_platform = random_list_value([""])

    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'

    payload = {'platform': search_platform}
    payload_auth = {'platform': search_platform, 'auth-id': auth_id}

    response_root = request(api_type, payload)
    response_root_auth = request(api_type, payload)

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")