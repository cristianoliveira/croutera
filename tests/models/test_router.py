#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Tests for Cli module
"""

import unittest
import argparse

import mock
from croutera.models.routers import Routers
from croutera.exceptions import ModelNotFoundError

class RoutersTest(unittest.TestCase):

    def setUp(self):
        self.model1 = mock.Mock({'description' : 'manufacturer model 1'})
        self.model2 = mock.Mock({'description' : 'manufacturer model 2'})
        self.model3 = mock.Mock({'description' : 'manufacturer2 model 1'})
        self.model4 = mock.Mock({'description' : 'manufacturer2 model 2'})
        self.models = {
           'manufacturer' : {
                'model1' : self.model1,
                'model2' : self.model2
           },
           'manufacturer2' : {
                'model3' : self.model3,
                'model4' : self.model4
           }
        }
        Routers.MANUFACTURER_MODELS = self.models

    def test_it_returns_all_models_from_manufacturer(self):
        self.assertEqual(self.models.get('manufacturer'),
                         Routers.from_manufacturer('manufacturer'))

    def test_it_returns_model_from_manufacturer(self):
        self.assertEqual(self.model1, Routers.get('manufacturer', 'model1'))

    def test_it_raise_model_not_found_error(self):
        self.assertRaises(ModelNotFoundError, Routers.get, 'manufacturer', 'model_invalid')

    def test_it_returns_models_available(self):
        self.assertEqual(Routers.list(), [
                                            'manufacturer2-model3',
                                            'manufacturer2-model4',
                                            'manufacturer-model2',
                                            'manufacturer-model1'
                                        ])
