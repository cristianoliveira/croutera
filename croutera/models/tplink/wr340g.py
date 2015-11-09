#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import base64

from croutera.models.base import Router
from croutera.http import header, request


class TplinkWR340(Router):
    """ Implementation for TpLink WR340G and WR340GD
    see: http://www.tp-link.com.br/products/details/?model=TL-WR340G
    """

    HOST = 'http://192.168.1.1'

    LOGIN_URI = '/'
    REBOOT_URI = '/userRpm/SysRebootRpm.htm?Reboot=Reboot'

    AUTH_FORMAT = "Basic %s"

    def login(self, username, password):
        self.username = username
        self.password = password

        url = self.HOST + self.LOGIN_URI
        response = request.Post(url, headers = self._headers(url)).execute()

        return response.code == request.RESPONSE_OK

    def restart(self):
        url = self.HOST + self.REBOOT_URI
        response = request.Post(url, headers = self._headers(url)).execute()

        return response.code == request.RESPONSE_OK

    def _headers(self, url):
        auth_header = header.basic_base64_auth(self.username,
                                               self.password)
        return {
            'Accept-Encoding' : 'gzip,deflate',
            'Referer' : url,
            'Authorization' : auth_header
        }
