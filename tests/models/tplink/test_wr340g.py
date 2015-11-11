# -*- coding: utf-8 -*-

"""
  Tests for TpLink WR340G
"""

import unittest
import mock

from croutera.models.tplink import TplinkWR340
from croutera.http import request

class TplinkWR340Test(unittest.TestCase):

    def setUp(self):
        self.router = TplinkWR340()

    @mock.patch('croutera.models.tplink.wr340g.request.Post')
    def test_it_accept_login(self, post):
        response = mock.Mock(**{ 'code' : request.RESPONSE_OK })
        request.Post('mocked', {}).execute.return_value = response

        self.assertTrue(self.router.login('valid','valid'))

    @mock.patch('croutera.models.tplink.wr340g.request.Post')
    def test_it_doesnt_accept_login(self, post):
        response = mock.Mock(**{ 'code' : request.RESPONSE_FORBIDDEN })
        request.Post('mocked', {}).execute.return_value = response

        self.assertFalse(self.router.login('invalid','invalid'))
