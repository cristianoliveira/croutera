#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import base64
import requests

from croutera.models.base import Router


class TplinkWR720N(Router):
    """ Implementation for TpLink WR720N
    see: http://www.tp-link.com.br/products/details/?model=TL-WR720N
    """

    HOST = 'http://192.168.0.1'

    LOGIN_URI = '/'
    REBOOT_URI = '/userRpm/SysRebootRpm.htm?Reboot=Reboot'

    def login(self, username, password):
        self.username = username
        self.password = password

        url = self.HOST + self.LOGIN_URI
        response = requests.get(url, auth = (username, password))

        return response.ok

    def restart(self):
        url = self.HOST + self.REBOOT_URI
        response = requests.get(url, auth = (self.username, self.password))

        return response.ok
