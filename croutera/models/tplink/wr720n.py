#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import base64

from croutera.models.base import Router
from croutera.http import header, request
import roscraco


class TplinkWR720N(Router):
    """ Implementation for TpLink WR720N
    see: http://www.tp-link.com.br/products/details/?model=TL-WR720N
    """

    HOST = '192.168.1.1'
    AUTH_FORMAT = "Basic %s"

    def __init__(self):
        self.controller = None

    def login(self, username, password):
        self.controller = roscraco.create_controller(
            roscraco.ROUTER_TP_LINK, 'WR720N',
            HOST, 80, username, password
        )


    def restart(self):
        if not self.controller:
            print('Not loged in.')
            return False
        self.controller.restart()
        return True
