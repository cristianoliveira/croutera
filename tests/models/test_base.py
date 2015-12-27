#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import argparse
import mock

from croutera.models.base import Router

class TestBase(unittest.TestCase):

    def test_it_should_compose_endpoint(self):
        router = StubRouter()
        router.config['ip'] = '1.1.1.1'
        router.config['uris']['login'] = 'login.html'
        self.assertEqual('http://1.1.1.1/login.html',
                         router.endpoint('login'))


class StubRouter(Router):

    def login(self, user, password):
        return True
