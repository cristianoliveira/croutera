#!/usr/bin/env python
# -*- coding: utf-8 -*-

from croutera import version
from models.routers import Routers

class Command(object):

    def valid(self):
        """ Implement logic for command validation """
        return True

    def execute(self):
        """ Command process """
        raise NotImplemented('Command not implemented')

class ModelListCommand(Command):
    """ List all router models available """

    def execute(self):
        print("Models list: \n")
        for model in Routers.list():
            print(model+"\n")

        print("For more models open an issue on: \n ")
        print("https://github.com/CristianOliveiraDaRosa/croutera")

        return True

class RestartCommand(Command):
    """ Restart modem / router

    params:
        +model+ Router model name
        +username+ Admin user name
        +password+ Admin password
    """

    def __init__(self, model, username, password):
        self.model = model
        self.username = username
        self.password = password

    def valid(self):
        if self.model.find('-') < 0:
            print('Invalid model format')
            return False
        return True

    def execute(self):
        router = Routers.get(*self.model.split('-'))()

        print('User login...')
        router.login(self.username, self.password)

        print('Router restarting...')
        return router.restart()

class VersionCommand(Command):
    """ Show current version installed """

    def execute(self):
        print('Croutera Version: ' + version())
        return True
