#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Models routers implementations
"""

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

    def login(self, user, password):
        data = str.format(LOGIN_DATA_FORMAT, username, password)
        urllib2.urlopen(HOST + LOGIN_URI, data)
        return "User logged!"

    def restart(self):
        data = 'reboot=Reboot&submit.htm%3Freboot.htm=Send'
        urllib2.urlopen(HOST + REBOOT_URI, data)
        return 'Restarting router'

class RouterFactory:
    """ Provide Router.class instances """

    ROUTERS = {
        'dlink-dir610' : DLinkDir610
    }

    @staticmethod
    def get(model):
        return RouterFactory.ROUTERS.get(model)()

    @staticmethod
    def list():
        return RouterFactory.ROUTERS.keys()
