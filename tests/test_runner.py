#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Tests for Runner module
"""

import unittest
import argparse

from mock import Mock, patch, call
from croutera import runner

class RunnerTest(unittest.TestCase):

    @patch('croutera.runner.ParserBuilder')
    def test_it_runs_with_no_argument(self, ParserBuilder):
        args = Mock()
        parser = Mock(**{'parse_args' : args})
        ParserBuilder.build.return_value = parser

        self.assertTrue(runner.run())


    @patch('croutera.runner.Cli')
    @patch('croutera.runner.ParserBuilder')
    def test_it_shows_help_whit_no_args(self, ParserBuilder, Cli):
        Cli.command.return_value = None

        runner.run()

        ParserBuilder.build().parse_args.assert_called_with(['-h'])
