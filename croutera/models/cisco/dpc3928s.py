#!/usr/bin/env python
# -*- coding: utf-8 -*-

from croutera.models.base import Router
import requests
from bs4 import BeautifulSoup


class CiscoDPC3928S(Router):

    HOST = 'http://192.168.0.1'

    LOGIN_URI = '/goform/Docsis_system'
    RESTART_URI = '/goform/Devicerestart'
    WIFI_PASS_URI = '/Quick_setup.asp'

    login_data = {
        'username_login': '',
        'password_login': '',
        'LanguageSelect': 'en',
        'Language_Submit' :'0',
        'login' :'Log In'
    }

    restart_data = {
        'devicerestrat_Password_check':'',
        'mtenRestore': 'Device Restart',
        'devicerestart':1,
        'devicerestrat_getUsercheck': ''
    }

    def login(self, username, password):
        self.login_data['username_login'] = username
        self.login_data['password_login'] = password
        self.session = requests.Session()
        self.session.post(self.HOST + self.LOGIN_URI, data = self.login_data)

    def restart(self):
        self.restart_data['devicerestrat_Password_check'] = self.login_data['password_login']
        res = self.session.post(self.HOST + self.RESTART_URI,
                                data = self.restart_data)
        return res.ok

    def wifi_pass(self):
        url = self.HOST + self.WIFI_PASS_URI
        response = self.session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.find('input', {'id':'wl5g_wpa_psk_key'}).get('value')


