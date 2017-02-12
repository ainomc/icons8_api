# -*- coding: utf-8 -*-

import paramiko

from api_logic import random_between_values, random_list_value, request, all_tag_attrib, word_count, attrib_value


class ContextListApi(object):

    # settings
    api_type = 'list'

    search_platform = random_list_value(["win8", "ios7", "android", "gradient",
                                         "color", "win10", "office", "p1em", ""])
    #search_platform = random_list_value([""])

    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'

    payload = {'platform': search_platform, 'auth-id': auth_id}

    response_root = request(api_type, payload, "v1", "xml")

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")