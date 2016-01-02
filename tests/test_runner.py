#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Tests for Runner module
"""

import unittest
import sys

from mock import Mock, patch
from croutera import runner


class RunnerTest(unittest.TestCase):

    @patch('croutera.runner.show_help')
    def test_it_runs_with_no_argument(self, show_help):
        sys.args = []

        runner.run()

        show_help.assert_called_with()

    @patch('croutera.runner.Cli')
    @patch('croutera.runner.ArgsParserBuilder')
    def test_it_does_not_execute_invalid_commands(self, ArgsParserBuilder, Cli):
        command = Mock()
        command.valid.return_value = False
        Cli.command.return_value = command

        runner.run()

        assert not command.execute.called

    @patch('croutera.runner.Cli')
    @patch('croutera.runner.ArgsParserBuilder')
    def test_it_does_execute_valid_commands(self, ArgsParserBuilder, Cli):
        command = Mock()
        command.valid.return_value = True
        Cli.command.return_value = command

        runner.run()

        assert command.execute.called
