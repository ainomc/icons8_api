# -*- coding: utf-8 -*-

import paramiko

from api_logic import random_between_values, request


class ContextIconApi(object):


    # Settings
    # icon id what will be in request
    icon_id = str(random_between_values(100, 20000))
    print ('''Icon tests: id - %s'''
           % icon_id)

    payload = {'id': icon_id}

    # Do Request and return response root
    response_root = request('icon', payload)

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")