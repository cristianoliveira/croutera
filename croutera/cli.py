#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Cli terminal module
"""

import argparse

from croutera.commands import *

class ParserBuilder(object):
    """
       Implement logic to parse args.
    """

    @staticmethod
    def build():
        ' Compose a parsers '

        description = 'Simple terminal cli to manage modem ' \
                                      '/ routers admin actions'

        parser = argparse.ArgumentParser(description=description,
                                         argument_default=argparse.SUPPRESS)

        parser.add_argument(
            'model',
            nargs='?',
            help='Router model. format: manufacturer-model (see --list-model)'
        )

        parser.add_argument(
            'username',
            nargs='?', help='User name to access admin page')
        parser.add_argument(
            'password',
            nargs='?', help='Password to access admin page')

        parser.add_argument(
            '-restart', dest='restart',
            action='store_true', default=False,
            help='Reset router by model.'
        )

        parser.add_argument(
            '-list-models', dest='list_models',
            action='store_true', default=False,
            help='Shows models available'
        )

        parser.add_argument(
            '-v', '--version', dest='version',
            action='store_true', default=False,
            help='Shows current version.'
        )

        return parser


class Cli(object):

    @staticmethod
    def command(args):
        """ Retrive command by args """

        if args.version:
            return VersionCommand()

        if args.list_models:
            return ModelListCommand()

        if args.restart:
            return RestartCommand(args.model, args.username, args.password)
