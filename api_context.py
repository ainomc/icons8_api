# -*- coding: utf-8 -*-
from api_logic import *
import paramiko
# Fixture settings fo Tests class
class Context(object):

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

        host = 'https://demoapi.icons8.com/'
        user = 'ainomc@gmail.com'
        secret = '123'
        port = 22

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")

