#!/usr/bin/env python

import urllib2, urllib

github_url = 'https://api.github.com/user/repos'

password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, github_url, 'BaltoRouberol', '***')

auth = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(auth)
urllib2.install_opener(opener)

request = urllib2.Request(github_url, urllib.urlencode({'name':'TEST', 'description': 'testtest'}))
handler = urllib2.urlopen(request)
print handler.read()