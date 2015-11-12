# -*- coding: utf-8 -*-

"""
  Tests for TpLink WR340G
"""

import unittest
import mock

from croutera.models.tplink import TplinkWR340
import requests

class TplinkWR340Test(unittest.TestCase):

    def setUp(self):
        self.router = TplinkWR340()

    @mock.patch('croutera.models.tplink.wr340g.requests')
    def test_it_accept_login(self, requests):
        response = mock.Mock(**{ 'ok' : True })
        requests.get.return_value = response

        self.assertTrue(self.router.login('valid','valid'))

    @mock.patch('croutera.models.tplink.wr340g.requests')
    def test_it_doesnt_accept_login(self, requests):
        response = mock.Mock(**{ 'ok' : False })
        requests.get.return_value = response

        self.assertFalse(self.router.login('invalid','invalid'))
