"""
  Tests for Command module
"""

import unittest
import argparse

from croutera.cli import Cli, ParserBuilder
from croutera.commands import *

class RestartCommandTest(unittest.TestCase):

    def test_it_is_invalid(self):
        command = RestartCommand('manufacturer_model','user','pass')
        self.assertFalse(command.valid())

    def test_it_is_valid(self):
        command = RestartCommand('manufacturer-model','user','pass')
        self.assertTrue(command.valid())
