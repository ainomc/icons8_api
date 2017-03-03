# -*- coding: utf-8 -*-
import json
import os
import glob
import argparse
from sys import platform

#runner demo - python init.py -request_url demoapi -auth_id 07cb0f621e742888b888d7630c1f0b37bdae536b

parser = argparse.ArgumentParser()
parser.add_argument('-request_url', '--request_url', nargs='+', type=str)
parser.add_argument('-auth_id', '--auth_id', nargs='+', type=str)
args = parser.parse_args()


with open('param.json', 'r+') as outfile:
    json_data = json.load(outfile)
    json_data['request_url'] = args.request_url[0]
    json_data['auth_id'] = args.auth_id[0]
    outfile.seek(0)
    outfile.write(json.dumps(json_data))
    outfile.truncate()

list_test_fies = glob.glob(os.path.join(os.getcwd(), 'tests', 'tests_*')) # find all tests files
for file_num in range(len(list_test_fies)):
    list_test_fies[file_num] = os.path.join(os.getcwd(), 'tests', list_test_fies[file_num])

str_list = " ".join(str(x) for x in list_test_fies) # convert list to string

if "win" in platform:
    os.system(r'python -m pytest -v %s -s --showlocals' % str_list)
elif "linux" in platform:
    os.system(r'python -m pytest -v %s -s --showlocals --junitxml=/var/lib/jenkins/workspace/icons8api_tests/junitxml/' % str_list)








