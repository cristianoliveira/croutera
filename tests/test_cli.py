#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Tests for Cli module
"""

import mock
import argparse

from unittest import TestCase
from croutera.cli import Cli, ArgsParserBuilder
from croutera.commands import *
from croutera.exceptions import ModelNotFoundError


class CliTest(TestCase):

    def setUp(self):
        router = mock.Mock()
        router.login.return_value = True
        self.models = {
           'manufacturer' : {
                'model1' : router
           }
        }
        Routers.MANUFACTURER_MODELS = self.models

    def test_it_returns_model_list_command(self):
        args = ArgsParserBuilder.build(self.cmd('-list-models'))
        command = Cli.command(args)
        self.assertTrue(command, ModelListCommand)

    def test_it_returns_version_command(self):
        args = ArgsParserBuilder.build(self.cmd('-v'))
        self.assertIsInstance(
            Cli.command(ArgsParserBuilder.build(self.cmd('-v'))),
            VersionCommand
        )
        self.assertIsInstance(
            Cli.command(ArgsParserBuilder.build(self.cmd('--version'))),
            VersionCommand
        )

    def test_it_returns_chain_command(self):
        args = ArgsParserBuilder.build(self.cmd('-restart manufacturer-model1 usr pas'))

        command = Cli.command(args)
        self.assertIsInstance(command, ChainCommand)

    def test_it_returns_at_first_authorize_command(self):
        args = ArgsParserBuilder.build(self.cmd('-restart manufacturer-model1 usr pas'))

        command = Cli.command(args)
        self.assertTrue(command.commands[0], AuthorizeCommand)

    def test_it_returns_at_end_restart_command(self):
        args = ArgsParserBuilder.build(self.cmd('-restart manufacturer-model1 usr pas'))

        command = Cli.command(args)
        self.assertTrue(command.commands[1], RestartCommand)

    def test_it_returns_at_end_show_wifi_command(self):
        args = ArgsParserBuilder.build(self.cmd('-wifi-pass manufacturer-model1 usr pas'))

        command = Cli.command(args)
        self.assertIsInstance(command.commands[1], ShowWifiPassCommand)

    def cmd(self, terminal_args):
        return terminal_args.split()
