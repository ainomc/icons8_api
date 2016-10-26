# -*- coding: utf-8 -*-
#from api_logic import *
from api_settings import *
import pytest
BaseApiLogic = BaseApiLogic()

# python -m pytest -v api_tests.py -s     --   runner

# Test icon API https://demoapi.icons8.com/manual/icon
class TestIconApi(IconSettings):

    # Do Request and return response root
    payload = {'id': '941'}
    responseRoot = BaseApiLogic.request('icon', payload)

    # Test resuilt tag
    def test_resuiltTag(self):
        tagAllAttrib = BaseApiLogic.tagAllAttrib(TestIconApi.responseRoot, 'result', '1')
        AttribValue = BaseApiLogic.AtrbValue (tagAllAttrib, 'id')
        BaseApiLogic.assertEqual(AttribValue, '941')

    # Test icon tag
    def test_iconTag(self):
        tagAllAttrib = BaseApiLogic.tagAllAttrib(TestIconApi.responseRoot, 'icon', '1')
        AttribValue = BaseApiLogic.AtrbValue (tagAllAttrib, 'id')
        BaseApiLogic.assertEqual(AttribValue, '941')

        AttribValue = BaseApiLogic.AtrbValue(tagAllAttrib, 'name')
        BaseApiLogic.assertEqual(AttribValue, "Rabbit")

        AttribValue = BaseApiLogic.AtrbValue(tagAllAttrib, 'platform')
        BaseApiLogic.assertEqual(AttribValue, "Windows 8/Metro")

        AttribValue = BaseApiLogic.AtrbValue(tagAllAttrib, 'created')
        BaseApiLogic.assertEqual(AttribValue, '2012-06-19T03:45:02+00:00')

        AttribValue = BaseApiLogic.AtrbValue(tagAllAttrib, 'url')
        BaseApiLogic.assertEqual(AttribValue, "/web-app/941/rabbit")

    # Test category test
    def test_categoryTag(self):
        tagValue = BaseApiLogic.tagValue(TestIconApi.responseRoot, 'category', '1')
        BaseApiLogic.assertEqual(tagValue, 'Animals')
