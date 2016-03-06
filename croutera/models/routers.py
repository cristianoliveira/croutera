#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Models routers implementations
"""

import base64

from croutera.models.base import Router
from croutera.models.cisco import CiscoDPC3928S
from croutera.models.tplink import TplinkWR340, TplinkWR720N, tlwrbased
from croutera.models.dlink import DLinkDir610
from croutera.exceptions import ModelNotFoundError
from croutera.extractor import extract_subclasses

class Routers(object):
    """ Provide Router.class instances """

    @staticmethod
    def get(manufacturer, model):
        models = Routers.from_manufacturer(manufacturer)
        router = [r for r in models if r.model == model]
        if not router:
            raise ModelNotFoundError('Model not found for this manufacturer.')

        return router[0]()

    @staticmethod
    def from_manufacturer(manufacturer):
        models = [r for r in extract_subclasses(Router)
                    if r.manufacturer == manufacturer]

        if not models:
            raise ModelNotFoundError('Manufacturer not found.')

        return models

    @staticmethod
    def list():
        available = [r.as_str() for r in extract_subclasses(Router)]
        return sorted(available)
