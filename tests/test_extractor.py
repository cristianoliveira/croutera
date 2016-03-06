#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from croutera import extractor

class A(object):
    'Stub classes for test pourposes'
    pass


class B(A):
    'Stub classes for test pourposes'
    pass


class C(B):
    'Stub classes for test pourposes'
    pass


class TestExtract(TestCase):

    def setUp(self):
        self.args_model = 'manufacturer-model'

    def test_it_extract_manufacturer(self):
        self.assertEqual('manufacturer',
                         extractor.extract_manufacturer(self.args_model))

    def test_it_extract_model(self):
        self.assertEqual('model',
                         extractor.extract_model(self.args_model))

    def test_it_extract_all_subclasses_inclusive_derived(self):
        subclasses = extractor.extract_subclasses(A)
        self.assertTrue(B in subclasses)
        self.assertTrue(C in subclasses)
