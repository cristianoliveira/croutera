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

    manufacturer = 'dlink'
    model = 'dir610'

    config = {
        'ip': '192.168.100.1',
        'uris': {
            'login': 'login.cgi',
            'reboot': 'form2Reboot.cgi',
            'wifi_settings': 'wlan_basic.htm'
        }
    }

    def login(self, username, password):
        data = {
            'username': username,
            'password': password,
            'submit.htm%3Flogin.htm': 'Send'
        }

        self.session = requests.Session()
        response = self.session.post(self.endpoint('login'), data = data)

        return response.ok

    def restart(self):
        data = {
            'reboot': 'Reboot',
            'submit.htm%3Freboot.htm': 'Send'
        }

        response = self.session.post(self.endpoint('reboot'), data = data)
        return response.ok

    def wifi_pass(self):
        response = self.session.get(self.endpoint('wifi_settings'))
        soup = BeautifulSoup(response.content, 'html.parser')

        return soup.find('input', {'name': 'pskValue'}).get('value')


