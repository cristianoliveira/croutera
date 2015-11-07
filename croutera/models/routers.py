#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Models routers implementations
"""

import urllib2

from urllib2 import URLError
from abc import ABCMeta, abstractmethod


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


class Routers(object):
    """ Provide Router.class instances """

    MODELS = {
        'dlink-dir610' : DLinkDir610
    }

    @staticmethod
    def get(model):
        model = Routers.MODELS.get(model)
        return model()

    @staticmethod
    def list():
        return Routers.MODELS.keys()
