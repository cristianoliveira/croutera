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
        args = self.parser.parse_args(self.cmd('-restart manufacturer-model1 usr pas'))
        command = Cli.command(args)
        self.assertIsInstance(command, RestartCommand)

    def test_it_returns_show_wifi_command(self):
        args = self.parser.parse_args(self.cmd('-wifi-pass manufacturer-model1 usr pas'))
        command = Cli.command(args)
        self.assertIsInstance(command, ShowWifiPassCommand)

    def test_it_returns_version_command(self):
        args = self.parser.parse_args(self.cmd('-v'))
        self.assertIsInstance(
            Cli.command(self.parser.parse_args(self.cmd('-v'))),
            VersionCommand
        )
        self.assertIsInstance(
            Cli.command(self.parser.parse_args(self.cmd('--version'))),
            VersionCommand
        )

    def cmd(self, terminal_args):
        return terminal_args.split()
