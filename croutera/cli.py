#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Cli terminal module
"""

from models.routers import RouterFactory

class Cli(object):

    def execute(self, args):
        """ Handle execution of args commands """

        if args.models_list:
             print("List of models: \n")
             for model in RouterFactory.list():
                 print(model+"\n")
                 return

        print("execute ", args)
