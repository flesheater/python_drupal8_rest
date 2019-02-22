#! /usr/local/bin/python3

from drupal8 import DrupalRest
from pprint import pprint
import base64


d = DrupalRest('http://localhost/dashboard/web/', {'username': 'test', 'password': 'test', 'client_secret': 'abc123', 'grant_type': 'password', 'client_id': 'b27f3a91-c033-4fa5-adf2-dd06050dcf4b', 'scope': 'rest'})
d.drupalLogin()

# Retrieving a node with nid 2
#node = d.retrieveNode(1)
#pprint(node)


#cat_file = open('cat.jpg', "rb").read()
#file_cat = {"_links":{"type":{"href":"http://localhost/dashboard/web/rest/type/file/image"},},
#"filename":[{"value":"cat.jpg"}],
#"filemime":[{"value":"image/jpeg"}],
#"type": [{"target_id": "image"}],
#"data":[{"value": base64.b64encode(cat_file)}]}

#file = d.createFile(file_cat)
#pprint(file)


new_node_array = {"_links": {"type": {"href":"http://localhost/dashboard/web/rest/type/node/post"}}, "type": [{"target_id":"post"}], "title":[{"value":"The rolley, the dimond, the basel"}]}
new_node = d.createNode(new_node_array)
pprint(new_node)
