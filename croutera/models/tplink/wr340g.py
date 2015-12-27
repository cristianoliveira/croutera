#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import requests
import re

from croutera.models.tplink.tlwrbased import TplinkTLWRBased
from bs4 import BeautifulSoup


class TplinkWR340(TplinkTLWRBased):
    """ Implementation for TpLink WR340G and WR340GD
    see: http://www.tp-link.com.br/products/details/?model=TL-WR340G
    """

    def __init__(self):
        self.config['ip'] = '192.168.1.1'
