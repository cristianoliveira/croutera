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
        args.model.return_value = 'man-model'
        ArgsParserBuilder.build.return_value = args

        self.assertTrue(runner.run())

    @patch('croutera.runner.Cli')
    @patch('croutera.runner.ArgsParserBuilder')
    def test_it_shows_help_when_doesnt_found_command(self, ArgsParserBuilder, Cli):
        Cli.command.return_value = None

        runner.run()

        ArgsParserBuilder.build_help.assert_called_with()
