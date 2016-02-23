#! /usr/local/bin/python
# -*- coding: utf-8 -*-

import pycurl
import json
import cStringIO
import urllib
import string

from pprint import pprint


class DrupalRest:
	host = ''
	endpoint = ''
	username = ''
	password = ''
	session = ''
	csrf_token = ''
	
	def __init__(self, host, endpoint, username, password):
		self.host = host
		self.endpoint = endpoint
		self.username = username
		self.password = password
	
	def drupalLogin(self):
		user = {'name': self.username, 'pass': self.password, 'form_id': 'user_login_form'}
		postData =  urllib.urlencode(user)
		
		response = cStringIO.StringIO()
		login_request_url = self.host + self.endpoint + 'user/login?_format=json'
		
		c = pycurl.Curl()
		c.setopt(pycurl.URL, login_request_url)
		
		c.setopt(pycurl.AUTOREFERER, 1)
		c.setopt(pycurl.FOLLOWLOCATION, True)
		c.setopt(pycurl.COOKIEFILE, '')
		c.setopt(pycurl.COOKIEJAR, 'cookies.txt')
		c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
		c.setopt(pycurl.HTTPHEADER, ['Content-type: application/x-www-form-urlencoded'])
		c.setopt(pycurl.WRITEFUNCTION, response.write)
		c.setopt(pycurl.POST, 1)
		c.setopt(pycurl.POSTFIELDS, postData)
		c.perform()
		c.close()

		csrf_token_str = cStringIO.StringIO()
		#very important is that here the URL is without the endpoint
		csrf_token_request_url = self.host + 'rest/session/token'
		
		z = pycurl.Curl()
		z.setopt(pycurl.URL, csrf_token_request_url)
		z.setopt(pycurl.WRITEFUNCTION, csrf_token_str.write)
		z.setopt(pycurl.COOKIEFILE, 'cookies.txt')
		z.perform()
		z.close()
		self.csrf_token = str(csrf_token_str.getvalue())

	def retrieveNode(self, nid):
		response = cStringIO.StringIO()
		
		c = pycurl.Curl()
		node_request_url = self.host + self.endpoint + 'node/' + str(nid) + '?_format=json'
		c.setopt(pycurl.URL, node_request_url)
		c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
		c.setopt(pycurl.COOKIEFILE, 'cookies.txt')
		c.setopt(pycurl.WRITEFUNCTION, response.write)
		c.perform()
		c.close()
		
		result_json = response.getvalue()
		pprint(result_json)
		result = json.loads(response.getvalue())
		return result

