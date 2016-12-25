# -*- coding: utf-8 -*-

import pytest

from api_logic import random_between_values, request


class ContextIconApiJson(object):

    # Settings
    # icon id what will be in request
    icon_id = str(random_between_values(100, 20000))
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

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")