#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import requests

from croutera.models.tplink.tlwrbased import TplinkTLWRBased


class TplinkWR720N(TplinkTLWRBased):
    """ Implementation for TpLink WR720N
    see: http://www.tp-link.com.br/products/details/?model=TL-WR720N
    """

    def __init__(self):
        super(TplinkTLWRBased, self).__init__()
        self.config['ip'] = '192.168.0.1'

