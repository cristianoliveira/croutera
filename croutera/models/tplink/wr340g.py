#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import requests
import re

from croutera.models.base import Router
from bs4 import BeautifulSoup


class TplinkWR340(Router):
    """ Implementation for TpLink WR340G and WR340GD
    see: http://www.tp-link.com.br/products/details/?model=TL-WR340G
    """

    HOST = 'http://192.168.1.1'

    LOGIN_URI = '/'
    REBOOT_URI = '/userRpm/SysRebootRpm.htm?Reboot=Reboot'
    WIFI_PASS_URI = '/userRpm/WlanNetworkRpm.htm'


    def login(self, username, password):
        self.username = username
        self.password = password

        url = self.HOST + self.LOGIN_URI
        self.session = requests.Session()
        response = self.session.get(url, auth = (username, password))

        return response.ok

    def restart(self):
        url = self.HOST + self.REBOOT_URI
        response = self.session.get(url, auth = (self.username, self.password))

        return response.ok

    def wifi_pass(self):
        url = self.HOST + self.WIFI_PASS_URI
        import ipdb; ipdb.set_trace()
        response = self.session.get(url, auth = (self.username, self.password))
        soup = BeautifulSoup(response.content, 'html.parser')
        wifi_data = re.findall("(.*?),", soup.find('script').text)
        return wifi_data[26]
