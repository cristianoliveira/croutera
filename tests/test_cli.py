#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Tests for Cli module
"""

import unittest
import argparse

from croutera.cli import Cli, ParserBuilder
from croutera.commands import *

class CliTest(unittest.TestCase):

    def setUp(self):
        self.parser = ParserBuilder.build()

    def test_it_returns_no_command(self):
        args = self.parser.parse_args(self.cmd('-'))
        command = Cli.command(args)
        self.assertTrue(command is None)

    def test_it_returns_model_list_command(self):
        args = self.parser.parse_args(self.cmd('-list-models'))
        command = Cli.command(args)
        self.assertIsInstance(command, ModelListCommand)

    def test_it_returns_restart_command(self):
        args = self.parser.parse_args(self.cmd('-restart mdl usr pas'))
        command = Cli.command(args)
        self.assertIsInstance(command, RestartCommand)

    def test_it_returns_version_command(self):
        args = self.parser.parse_args(self.cmd('-v'))
        command = Cli.command(self.parser.parse_args(self.cmd('-v')))
        command2 = Cli.command(self.parser.parse_args(self.cmd('--version')))
        self.assertIsInstance(command, VersionCommand)
        self.assertIsInstance(command2, VersionCommand)

    def cmd(self, terminal_args):
        return terminal_args.split()
