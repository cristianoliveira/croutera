# -*- coding: utf-8 -*-

"""
  Tests for Cli module
"""

import unittest
import argparse

from croutera.cli import Cli, ParserBuilder
from croutera.commands import ModelListCommand, RestartCommand

class CliTest(unittest.TestCase):

    def setUp(self):
        self.parser = ParserBuilder.build()

    def test_it_returns_model_list_command(self):
        args = self.parser.parse_args(self.cmd('-list-models'))
        command = Cli.command(args)
        self.assertIsInstance(command, ModelListCommand)

    def test_it_returns_restart_command(self):
        args = self.parser.parse_args(self.cmd('-restart mdl usr pas'))
        command = Cli.command(args)
        self.assertIsInstance(command, RestartCommand)

    def cmd(self, terminal_args):
        return terminal_args.split()
