#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Cli terminal module
"""

from models.routers import Routers
from commands import ModelListCommand, RestartCommand

class Cli(object):

    @staticmethod
    def command(args):
        """ Retrive command by args """
        if args.list_models:
            return ModelListCommand()

        if args.restart:
            return RestartCommand(args.model, args.username, args.password)

