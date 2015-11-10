# -*- coding: utf-8 -*-

"""
  Tests for TpLink WR340G
"""

import unittest

from croutera.models.tplink import TplinkWR340

class TplinkWR340Test(unittest.TestCase):

    def setUp(self):
        self.router = TplinkWR340()

    def test_it_accept_login(self, request):
        self.assertTrue(True)
