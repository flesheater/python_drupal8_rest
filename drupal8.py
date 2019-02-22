#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import requests
import pprint
import simplejson

from pprint import pprint


class DrupalRest:
	host = ''
	user = {}
	login_response = {}
	auth_header = {}

	def __init__(self, host, endpoint, user):
		self.host = host
		self.endpoint = endpoint
		self.user = user

	def drupalLogin(self):
		login_request_url = self.host + 'oauth/token'
		r = requests.post(login_request_url, data=self.user, headers={})
		self.login_response = simplejson.loads(r.text)
		self.auth_header = {'Authorization': self.login_response['token_type'] + ' ' + self.login_response['access_token']}

	def retrieveNode(self, nid):
		request_url = self.host + 'node/' + str(nid) + '?_format=json'
		r = requests.get(request_url, data={}, headers=self.auth_header)
		return simplejson.loads(r.text)

	def createNode(self, node):
		request_url = self.host + 'node?_format=hal_json'
		r = requests.post(request_url, data=simplejson.dumps(node), headers=self.auth_header.update({'Content-type': 'application/hal+json', 'Accept': 'application/hal+json'}))
		return r.text

	def createFile(self, file):
		request_url = self.host + 'entity/file?_format=hal_json'
		r = requests.post(request_url, data=simplejson.dumps(file), headers=self.auth_header.update({'Content-type': 'application/hal+json', 'Accept': 'application/hal+json'}))
		return r.text
