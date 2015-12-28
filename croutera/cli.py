#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Cli terminal module
"""

import os
import argparse

from croutera import extractor
from croutera.commands import VersionCommand, RestartCommand, \
     ModelListCommand, ShowWifiPassCommand, ChainCommand, \
     AuthorizeCommand
from croutera.exceptions import InvalidCommandArgs
from croutera.models import Routers


class Cli(object):

    @staticmethod
    def command(args):
        """ Retrive command by args """

        if not Cli.validate(args):
            raise InvalidCommandArgs()

        if args.version:
            return VersionCommand()

        if args.list_models:
            return ModelListCommand()

        manufacturer = extractor.extract_manufacturer(args.model)
        model = extractor.extract_model(args.model)
        router = Routers.get(manufacturer, model)

        chain = ChainCommand()
        chain.add(AuthorizeCommand(router, args.username, args.password))

        if args.wifi_pass:
            chain.add(ShowWifiPassCommand(router))
            return chain

        if args.restart:
            chain.add(RestartCommand(router))
            return chain

    @staticmethod
    def validate(args):
        if args.version or args.list_models:
            return True

        if not args.model:
            print('Model was not informed.')
            return False

        if not '-' in args.model or len(args.model) < 3:
            print('Invalid model format.')
            return False

        return True

class ArgsParserBuilder(object):
    """
       Implement logic to parse args.
    """

    @staticmethod
    def build(args):
        ' Compose a parsers '

        description = """Simple terminal cli to manage modem 
        / routers admin actions"""

        parser = argparse.ArgumentParser(description=description,
                                         argument_default=argparse.SUPPRESS)

        parser.add_argument(
            'model',
            nargs='?', default=os.getenv('ROUTER_USERNAME'),
            help='Router model. format: manufacturer-model (see --list-model)'
        )

        parser.add_argument(
            'username', default=os.getenv('ROUTER_USERNAME'),
            nargs='?', help='User name to access admin page.')
        parser.add_argument(
            'password', default=os.getenv('ROUTER_PASSWORD'),
            nargs='?', help='Password to access admin page.')

        # Commands
        parser.add_argument(
            '-restart', dest='restart',
            action='store_true', default=False,
            help='Reset router by model.'
        )

        parser.add_argument(
            '-wifi-pass', dest='wifi_pass',
            action='store_true', default=False,
            help='Reset router by model.'
        )

        parser.add_argument(
            '-list-models', dest='list_models',
            action='store_true', default=False,
            help='Shows models available.'
        )

        # Aux
        parser.add_argument(
            '-ip', dest='ip', default=os.getenv('ROUTER_IP'),
            help='Provide router ip.'
        )

        parser.add_argument(
            '-v', '--version', dest='version',
            action='store_true', default=False,
            help='Shows current version.'
        )

        return parser.parse_args(args)

    @staticmethod
    def build_help():
        return ArgsParserBuilder.build(['-h'])



