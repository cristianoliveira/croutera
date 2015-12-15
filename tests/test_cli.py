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
from croutera.exceptions import InvalidCommandArgs


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
        self.assertIsInstance(command, ModelListCommand)

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

    def test_it_returns_restart_command(self):
        args = ArgsParserBuilder.build(self.cmd('-restart manufacturer-model1 usr pas'))

        command = Cli.command(args)
        self.assertIsInstance(command, RestartCommand)

    def test_it_returns_show_wifi_command(self):
        args = ArgsParserBuilder.build(self.cmd('-wifi-pass manufacturer-model1 usr pas'))

        command = Cli.command(args)
        self.assertIsInstance(command, ShowWifiPassCommand)

    def test_it_raises_invalid_argument_when_model_has_wrong_format(self):
        self.assertRaises(
            InvalidCommandArgs,
            Cli.command, ArgsParserBuilder.build(self.cmd('-wifi-pass ciscomodel1'))
        )


    def test_it_raises_invalid_argument_error_without_model(self):
        self.assertRaises(InvalidCommandArgs,
                          Cli.command,
                          ArgsParserBuilder.build(self.cmd('-')))
        self.assertRaises(InvalidCommandArgs,
                          Cli.command,
                          ArgsParserBuilder.build(self.cmd('-restart')))
        self.assertRaises(InvalidCommandArgs,
                          Cli.command,
                          ArgsParserBuilder.build(self.cmd('-wifi-pass')))

    def cmd(self, terminal_args):
        return terminal_args.split()
