#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Models routers implementations
"""

import urllib2
import base64

from croutera.models.tplink import *
from croutera.models.dlink import *

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
