#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from croutera import extractor

class TestExtract(TestCase):

    def setUp(self):
        self.args_model = 'manufacturer-model'

    def test_it_extract_manufacturer(self):
        self.assertEqual('manufacturer',
                         extractor.extract_manufacturer(self.args_model))

    def test_it_extract_model(self):
        self.assertEqual('model',
                         extractor.extract_model(self.args_model))
