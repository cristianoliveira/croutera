#!/usr/bin/env python
# -*- coding: utf-8 -*-

from croutera.models.base import Router
import requests
from bs4 import BeautifulSoup


class CiscoDPC3928S(Router):

    manufacturer = 'cisco'
    model = 'dpc3928s'

    config = {
        'ip': '192.168.0.1',
        'uris': {
            'login': 'goform/Docsis_system',
            'reboot': 'goform/Devicerestart',
            'wifi_settings': 'Quick_setup.asp'
        }
    }

    def login(self, username, password):
        data = {
            'username_login': username,
            'password_login': password,
            'LanguageSelect': 'en',
            'Language_Submit' :'0',
            'login' :'Log In'
        }

        self.password = password

        self.session = requests.Session()
        self.session.post(self.endpoint('login'), data = self.login_data)

    def restart(self):
        data = {
            'devicerestrat_Password_check': self.password,
            'mtenRestore': 'Device Restart',
            'devicerestart':1,
            'devicerestrat_getUsercheck': ''
        }

        res = self.session.post(self.endpoint('reboot'), data = data)
        return res.ok

    def wifi_pass(self):
        response = self.session.get(self.endpoint('wifi_settings'))
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.find('input', {'id':'wl5g_wpa_psk_key'}).get('value')


