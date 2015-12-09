#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Tests for Runner module
"""

import unittest

from mock import Mock, patch
from croutera import runner


class RunnerTest(unittest.TestCase):

    @patch('croutera.runner.ArgsParserBuilder')
    def test_it_runs_with_no_argument(self, ArgsParserBuilder):
        args = Mock()
        parser = Mock(**{'parse_args': args})
        ArgsParserBuilder.build.return_value = parser

        self.assertTrue(runner.run())

    @patch('croutera.runner.Cli')
    @patch('croutera.runner.ArgsParserBuilder')
    def test_it_shows_help_when_doesnt_found_command(self, ArgsParserBuilder, Cli):
        Cli.command.return_value = None

        runner.run()

        ArgsParserBuilder.build_help.assert_called_with()
