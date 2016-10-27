# -*- coding: utf-8 -*-
from api_logic import *
# Fixture settings fo Tests class
class IconSettings(object):

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")

