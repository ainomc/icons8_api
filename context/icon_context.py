# -*- coding: utf-8 -*-

import random

from api_logic import random_between_values, request, auth_id


class ContextIconApi(object):

    # Settings
    # icon id what will be in request
    icon_id = random.choice([str(random_between_values(1, 7500)),
                             str(random_between_values(9500, 20000))])

    print ('''Icon v1 tests: id - %s'''
           % icon_id)

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