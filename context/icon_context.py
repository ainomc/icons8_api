# -*- coding: utf-8 -*-

import pytest

from api_logic import random_between_values, request


class ContextIconApi(object):

    # Settings
    # icon id what will be in request
    while True:
        icon_id = str(random_between_values(100, 20000))
        if icon_id > 7500 and icon_id < 9500:
            pass
        else:
            break
    print ('''Icon tests: id - %s'''
           % icon_id)

    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'

    payload = {'id': icon_id}
    payload_auth = {'id': icon_id, 'auth-id': auth_id}

    # Do Request and return response root
    response_root = request('icon', payload, "v1", "xml")
    response_root_auth = request('icon', payload_auth, "v1", "xml")

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")