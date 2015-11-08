#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Models routers implementations
"""

import urllib2
import base64

from urllib2 import URLError
from abc import ABCMeta, abstractmethod
from croutera.http import Header

class Router(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def login(self, user, password):
        """ Provide logic to auth into router admin page """
        pass

    @abstractmethod
    def restart(self):
        """ Provide logic to restart the router (logged action) """
        pass


class DLinkDir610(Router):
    """
    Implementation for D-link DR610
    see: http://www.dlink.com.br/produto/dir-610-a1
    """
    HOST = 'http://192.168.100.1'

    # URIs
    LOGIN_URI = '/login.cgi'
    REBOOT_URI = '/form2Reboot.cgi'

    LOGIN_DATA_FORMAT = 'username={0}&password={1}&submit.htm%3Flogin.htm=Send'

    def login(self, username, password):
        data = str.format(self.LOGIN_DATA_FORMAT, username, password)
        urllib2.urlopen(self.HOST + self.LOGIN_URI, data)
        return "User logged!"

    def restart(self):
        data = 'reboot=Reboot&submit.htm%3Freboot.htm=Send'
        try:
            urllib2.urlopen(self.HOST + self.REBOOT_URI, data)
        except URLError:
            print("Network is unreachable. Router is on? or is correct IP?")
            return
        print("Restarting the router")


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

        request = self._prepare_request(self.HOST + self.LOGIN_URI)

        try:
            urllib2.urlopen(request)
        except URLError:
            print("Network is unreachable. Is Router on? or is IP correct?")
            return

        print("User logged!")

    def restart(self):
        urllib2.urlopen(self._prepare_request(self.HOST + self.REBOOT_URI))
        print("Restarting the router")

    def _prepare_request(self, url):
        request = urllib2.Request(url)
        auth_header = Header.prepare_base64_auth(self.username,
                                                 self.password)

        request.add_header('Authorization', "Basic %s" % auth_header)
        request.add_header('Accept-Encoding', 'gzip,deflate')
        request.add_header('Referer', url)

        return request


class Routers(object):
    """ Provide Router.class instances """

    MODELS = {
        'dlink-dir610' : DLinkDir610,
        'tplink-wr340g' : TplinkWR340
    }

    @staticmethod
    def get(model):
        model = Routers.MODELS.get(model)
        return model()

    @staticmethod
    def list():
        return Routers.MODELS.keys()
