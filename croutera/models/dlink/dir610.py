#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

from croutera.models.base import Router
import requests
from bs4 import BeautifulSoup


class DLinkDir610(Router):
    """ Implementation for D-link DR610
    see: http://www.dlink.com.br/produto/dir-610-a1
    """
    HOST = 'http://192.168.100.1'

    # URIs
    LOGIN_URI = '/login.cgi'
    REBOOT_URI = '/form2Reboot.cgi'
    WIFI_PASS_URI = '/wlan_basic.htm'

    def login(self, username, password):
        data = {
            'username': username,
            'password': password,
            'submit.htm%3Flogin.htm': 'Send'
        }

        url = self.HOST + self.LOGIN_URI

        self.session = requests.Session()
        response = self.session.post(url, data = data)

        return response.ok

    def restart(self):
        data = {
            'reboot': 'Reboot',
            'submit.htm%3Freboot.htm': 'Send'
        }

        url = self.HOST + self.REBOOT_URI
        response = self.session.post(url, data = data)

        return response.ok

    def wifi_pass(self):
        url = self.HOST + self.WIFI_PASS_URI
        response = self.session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        return soup.find('input', {'name': 'pskValue'}).get('value')


