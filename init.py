# -*- coding: utf-8 -*-
import json
import os
import glob
import argparse
from sys import platform

# Parse parameters from command line
parser = argparse.ArgumentParser()
parser.add_argument('-request_url', '--request_url', nargs='+', type=str)
parser.add_argument('-auth_id', '--auth_id', nargs='+', type=str)
args = parser.parse_args()

# Write parameters to the params.json
with open('param.json', 'r+') as outfile:
    json_data = json.load(outfile)
    json_data['request_url'] = args.request_url[0]
    json_data['auth_id'] = args.auth_id[0]
    outfile.seek(0)
    outfile.write(json.dumps(json_data))
    outfile.truncate()

# Find all path to tests_* files and create list
list_test_fies = glob.glob(os.path.join(os.getcwd(), 'tests', 'tests_*'))

# Convert path to universal path what can be used in linux
for file_num in range(len(list_test_fies)):
    list_test_fies[file_num] = os.path.join(os.getcwd(), 'tests',
                                            list_test_fies[file_num])

# Convert list to one string with spaces (' ') between each path
str_list = " ".join(str(x) for x in list_test_fies)  # convert list to string

# Run tests with all tests files

if "win" in platform:  # tests_category_v2_api_json
    os.system('python -m pytest -v %s -s --showlocals --html=report/html/report.html' % str_list)
    #os.system(r'python -m pytest -v tests\tests_icon_api.py '
    # r'-s --showlocals --html=xml/report.html')
elif "linux" in platform:
    os.system('python -m pytest -v %s -s --showlocals' % str_list)
    #os.system('python -m pytest -v %s -s --showlocals --junitxml=/var/lib/jenkins/workspace/icons8api_tests/report/junitxml.xml --html=report/html/report.html' % str_list)