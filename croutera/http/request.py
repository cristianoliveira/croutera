#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Http Requests module
"""

import urllib2

RESPONSE_OK = 200
RESPONSE_FORBIDDEN = 403
RESPONSE_NOT_FOUND = 404

class Post(object):
    """ Executes http requests """

    def __init__(self, url, data = "", headers = {}):
        self.url = url
        self.data = data
        self.headers = headers

    def execute(self):
        request = urllib2.Request(self.url, self.data)

        for k, v in self.headers.iteritems():
            request.add_header(k, v)

        return urllib2.urlopen(request)
