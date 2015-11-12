#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import base64

from croutera.models.base import Router
import requests


class DLinkDir610(Router):
    """ Implementation for D-link DR610
    see: http://www.dlink.com.br/produto/dir-610-a1
    """
    HOST = 'http://192.168.100.1'

    # URIs
    LOGIN_URI = '/login.cgi'
    REBOOT_URI = '/form2Reboot.cgi'

    LOGIN_DATA_FORMAT = 'username={0}&password={1}&submit.htm%3Flogin.htm=Send'

    def login(self, username, password):
        data = str.format(self.LOGIN_DATA_FORMAT, username, password)
        url = self.HOST + self.LOGIN_URI
        response = requests.post(url, data = data)

        return response.ok

    def restart(self):
        data = 'reboot=Reboot&submit.htm%3Freboot.htm=Send'
        url = self.HOST + self.REBOOT_URI
        response = requests.post(url, data = data)

        return response.ok
