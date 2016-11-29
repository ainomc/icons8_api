# -*- coding: utf-8 -*-

import paramiko

from api_logic import random_between_values, random_list_value, request, all_tag_attrib, word_count, attrib_value

# Fixture settings fo Tests class
class ContextIconApi(object):


    # Settings
    # icon id what will be in request
    icon_id = str(random_between_values(100, 20000))
    print (icon_id + ' test icon')

    payload = {'id': icon_id}

    # Do Request and return response root
    response_root = request('icon', payload)

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")



class ContextSearchDefaultApi(object):

    #settings
    api_type = 'search'

    term = random_list_value(['google', 'facebook', 'space',
                              'ball', 'car', 'word'])

    payload = {'term': term, 'amount': '',
               'offset': '', 'platform': ''}

    icon_count = 25

    # Do Request and return response root
    response_root = request(api_type, payload)

    icons_current_count = 0
    x = True
    while x == True:
        try:
            icons_current_count += 1
            tag_attribs = all_tag_attrib(response_root,
                                         'icon', str(icons_current_count))
            value_of_attrib = attrib_value(tag_attribs, 'id')
            assert word_count(value_of_attrib) >= 1
            assert icons_current_count <= icon_count
        except AttributeError:
            x = False
            icons_current_count -= 1
            #print (str(icons_current_count) + '<<< count icons in response')
            assert icons_current_count > 0
    #print (str(icons_current_count) + ' <<< current count of icons')

    # Choose random icon between min and max
    icon_number = str(random_between_values(1, icon_count))

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")



class ContextSearchMaxApi(object):


    #settings
    api_type = 'search'

    search_text = random_list_value(['google', 'facebook', 'space',
                                     'ball', 'car', 'word'])

    search_amount = '20'

    search_offset = '20'

    search_platform = random_list_value(["win8", "ios7", "android", "androidL",
                                         "color", "win10", "office"])

    search_language = ''

    payload = {
        'term': search_text, 'amount': search_amount,
        'offset': search_offset, 'platform': search_platform
    }

    icon_count = 20

    # Do Request and return response root
    response_root = request(api_type, payload)


    icons_current_count = 0
    x = True
    while x == True:
        try:
            icons_current_count += 1
            tag_attribs = all_tag_attrib(response_root,
                                         'icon', str(icons_current_count))
            value_of_attrib = attrib_value(tag_attribs, 'id')
            assert word_count(value_of_attrib) >= 1
            assert icons_current_count <= icon_count
        except AttributeError:
            x = False
            icons_current_count -= 1
            print (str(icons_current_count) + '<<< count icons in response (IconTests)')
            assert icons_current_count > 0
    print (str(icons_current_count) + ' <<< current count of icons (IconTests)')

    # Choose random icon between min and max
    if icons_current_count == 2:
        icon_number = icons_current_count
    else:
        icon_number = str(random_between_values(1, icons_current_count))

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")



class ContextSearchMinApi(object):

    #settings
    api_type = 'search'

    search_text = random_list_value(['google', 'facebook', 'space',
                                     'ball', 'car', 'word'])
    search_amount = '5'

    search_offset = '5'

    search_platform = random_list_value(["win8", "ios7", "android", "androidL",
                                         "color", "win10", "office"])
    search_language = ''

    payload = {
        'term': search_text, 'amount': search_amount,
        'offset': search_offset, 'platform': search_platform
    }

    icon_count = 5

    # Do Request and return response root
    response_root = request(api_type, payload)

    icons_current_count = 0
    x = True
    while x == True:
        try:
            icons_current_count += 1
            tag_attribs = all_tag_attrib(response_root,
                                         'icon', str(icons_current_count))
            value_of_attrib = attrib_value(tag_attribs, 'id')
            assert word_count(value_of_attrib) >= 1
            assert icons_current_count <= icon_count
        except AttributeError:
            x = False
            icons_current_count -= 1
            #print (str(icons_current_count) + '<<< count icons in response')
            assert icons_current_count > 0
    #print (str(icons_current_count) + ' <<< current count of icons')

    # Choose random icon between min and max
    icon_number = str(random_between_values(1, icon_count))

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")



class ContextLatestApi(object):


    # settings
    api_type = 'latest'

    amount = random_list_value(["", "5", "10", "15", "20"])

    offset = random_list_value(["", "5", "10", "15", "20"])

    search_platform = random_list_value(["win8", "ios7", "android", "androidL",
                                         "color", "win10", "office", ""])

    payload = {'amount': amount, 'offset': offset, 'platform': search_platform}

    icon_count = 100

    # Do Request and return response root
    response_root = request(api_type, payload)

    icons_current_count = 0
    x = True
    while x == True:
        try:
            icons_current_count += 1
            tag_attribs = all_tag_attrib(response_root,
                                         'icon', str(icons_current_count))
            value_of_attrib = attrib_value(tag_attribs, 'id')
            assert word_count(value_of_attrib) >= 1
            assert icons_current_count <= icon_count
        except AttributeError:
            x = False
            icons_current_count -= 1
            #print (str(icons_current_count) + '<<< count icons in response')
            assert icons_current_count > 0
    #print (str(icons_current_count) + ' <<< current count of icons')

    # Choose random icon between min and max
    icon_number = str(random_between_values(1, icons_current_count))

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")


"""
class ContextSimilarApi(object):
    # settings
    api_type = 'similar'

    # icon id what will be in request
    icon_id = str(random_between_values(100, 20000))
    print (icon_id + ' test icon')

    amount = random_list_value(["", "5", "10", "15", "20"])

    #offset = random_list_value(["", "5", "10", "15", "20"])
    offset = random_list_value(["", "5"])

    payload = {'id': icon_id, 'amount': amount, 'offset': offset}

    icon_count = 100

    # Do Request and return response root
    response_root = request(api_type, payload)

    similiar_icons_current_count = 0

    x = True
    while x == True:
        try:
            similiar_icons_current_count += 1
            tag_attribs = all_tag_attrib(response_root,
                                         'icon', str(similiar_icons_current_count))
            value_of_attrib = attrib_value(tag_attribs, 'id')
            assert word_count(value_of_attrib) >= 1
            assert similiar_icons_current_count <= icon_count
        except AttributeError:
            x = False
            similiar_icons_current_count -= 1
            #print (str(icons_current_count) + '<<< count icons in response')
            assert similiar_icons_current_count > 0
    #print (str(icons_current_count) + ' <<< current count of icons')

    # Choose random icon between min and max
    icon_number = str(random_between_values(1, similiar_icons_current_count))

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")

"""


class ContextCategoryApi(object):


    # settings
    api_type = 'category'

    category = random_list_value(["Arrows", "City", "Data", "Food", "Travel",
                                  "Transport", "Holidays", "Objects", "Printing", "Weather"])

    amount = random_list_value(["", "5", "10", "15", "20"])

    offset = random_list_value(["", "5", "10", "15", "20"])

    platform = random_list_value(["win8", "ios7", "android", "androidL",
                                  "color", "win10", "office"])

    attributes = ''

    payload = {'category': category, 'amount': amount, 'offset': offset, 'platform': platform, 'attributes': attributes}
    print (category + ' - category(Category tests)')
    print (amount + ' - amount(Category tests)')
    print (offset + ' - offset(Category tests)')
    print (platform + ' - platform(Category tests)')

    icon_count = 100

    # Do Request and return response root
    response_root = request(api_type, payload)

    icons_current_count = 0
    x = True
    while x == True:
        try:
            icons_current_count += 1
            tag_attribs = all_tag_attrib(response_root,
                                         'icon', str(icons_current_count))
            value_of_attrib = attrib_value(tag_attribs, 'id')
            assert word_count(value_of_attrib) >= 1
            assert icons_current_count <= icon_count
        except AttributeError:
            x = False
            icons_current_count -= 1
            #print (str(icons_current_count) + '<<< count icons in response')
            assert icons_current_count > 0
    #print (str(icons_current_count) + ' <<< current count of icons')

    # Choose random icon between min and max
    icon_number = str(random_between_values(1, icons_current_count))

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")



class ContextTotalApi(object):


    # settings
    api_type = 'total'

    year = random_list_value(["14", "15", "16"])
    month =  random_between_values(1, 12)
    day = random_between_values(1, 31)

    since = '20%s-%s-%s' % (year, month, day)

    payload = {'since': since}

    icon_count = 100

    # Do Request and return response root
    response_root = request(api_type, payload)

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")



class ContextSuggestApi(object):

    #settings
    api_type = 'suggest'

    term = random_list_value(['google', 'facebook', 'space',
                              'ball', 'car', 'word'])

    amount = random_list_value(["", "5", "10", "15", "20"])

    platform = random_list_value(["win8", "ios7", "android", "androidL",
                                  "color", "win10", "office"])

    payload = {'term': term, 'amount': amount, 'platform': platform}

    term_count = 25

    # Do Request and return response root
    response_root = request(api_type, payload)

    term_current_count = 0
    x = True
    while x == True:
        try:
            term_current_count += 1
            tag_attribs = all_tag_attrib(response_root,
                                         'suggests/term', str(term_current_count))
            value_of_attrib = attrib_value(tag_attribs, 'count')
            assert word_count(value_of_attrib) >= 1
            assert term_current_count <= term_count
        except AttributeError:
            x = False
            term_current_count -= 1
            assert term_current_count > 0
    # Choose random icon between min and max
    if term_current_count == 2:
        term_number = term_current_count
    else:
        term_number = str(random_between_values(2, term_current_count))

    # Action before class
    def setup_class(cls):
        print("\n>>> Class Setup")

    #  Action after class
    def teardown_class(cls):
        print("\n>>> Class Teardown")
