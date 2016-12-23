# -*- coding: utf-8 -*-

import paramiko

from api_logic import random_between_values, random_list_value, request


class ContextTotalApi(object):


    # settings
    api_type = 'total'

    year = random_list_value(["14", "15", "16"])
    month =  random_between_values(1, 12)
    day = random_between_values(1, 31)

    since = '20%s-%s-%s' % (year, month, day)
    auth_id = '07cb0f621e742888b888d7630c1f0b37bdae536b'

    payload = {'since': since}
    payload_auth = {'since': since, 'auth-id': auth_id}

    print ('''Total  tests: since - %s'''
           % (since))

    icon_count = 100

    # Do Request and return response root
    response_root = request(api_type, payload)
    response_root_auth = request(api_type, payload_auth)

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")