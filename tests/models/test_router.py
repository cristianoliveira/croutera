#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Tests for Cli module
"""

import unittest
import argparse

import mock
from croutera.models.base import Router
from croutera.models.routers import Routers
from croutera.exceptions import ModelNotFoundError

class RoutersTest(unittest.TestCase):

    def test_it_returns_all_models_from_manufacturer(self):
        manufacturer = AStubRouter.manufacturer
        routers = Routers.from_manufacturer(manufacturer)
        self.assertTrue(AStubRouter in routers)
        self.assertFalse(ZStubRouter in routers)

    def test_it_returns_model_from_manufacturer(self):
        manufacturer = AStubRouter.manufacturer
        model = AStubRouter.model
        router = Routers.get(manufacturer, model)
        self.assertIsInstance(router, AStubRouter)

    def test_it_raise_model_not_found_error(self):
        self.assertRaises(ModelNotFoundError, Routers.get, 'manufacturer', 'model_invalid')

    def test_it_returns_sorted_models_available(self):
        self.assertEqual(AStubRouter.as_str(), Routers.list()[0])
        self.assertEqual(ZStubRouter.as_str(), Routers.list()[-1])

class AStubRouter(Router):
    manufacturer = 'aaaaa'
    model = 'aaaaa'

    def login(self, user, passw):
        return True

class ZStubRouter(Router):
    manufacturer = 'zzzzz'
    model = 'zzzzz'
    pass
