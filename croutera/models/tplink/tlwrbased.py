#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import requests
import re

from croutera.models.base import Router
from bs4 import BeautifulSoup


class TplinkTLWRBased(Router):
    """Implementation for TpLink WR based models.

    For more details see all them:
    http://www.tp-link.com.br/search/?q=wr    """
    config = {
        'ip': '192.168.1.1',
        'uris': {
            'login': '',
            'reboot': 'userRpm/SysRebootRpm.htm?Reboot=Reboot',
            'wifi_settings': 'userRpm/WlanNetworkRpm.htm'
        }
    }

    def login(self, username, password):
        self.username = username
        self.password = password

        self.session = requests.Session()
        response = self.session.get(self.endpoint('login'),
                                    auth = (username, password))

        return response.ok

    def restart(self):
        response = self.session.get(self.endpoint('restart'),
                                    auth = (self.username, self.password))

        return response.ok

    def wifi_pass(self):
        import ipdb; ipdb.set_trace()
        response = self.session.get(self.endpoint('wifi_settings'),
                                    auth = (self.username, self.password))
        soup = BeautifulSoup(response.content, 'html.parser')
        wifi_data = re.findall("(.*?),", soup.find('script').text)
        return wifi_data[26]
