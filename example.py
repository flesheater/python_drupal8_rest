#! /usr/local/bin/python

from drupal8 import DrupalRest
from pprint import pprint
import json 

d = DrupalRest('http://drupal8.dev/', '', 'app_user', 'pass_of_app_user')
d.drupalLogin()

# Retrieving a node with nid 2
node = d.retrieveNode(2)
pprint(node)


#base64 = open('cat.jpg').read(100000).encode('base64')
#file_cat = {'filename': 'cat.jpg', 'file': base64}

#file = d.createFile(file_cat)


#new_node_array = {'title': 'last test 66', 'type': 'article', 'field_image[und][0][fid]':file['fid']}
#
#new_node_array = {'values[title]': 'last test 66', 'values[type]': 'article'}
#new_node = d.createNode(new_node_array)
#pprint(new_node)

