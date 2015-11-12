#!/usr/bin/env python
# -*- coding: utf-8 -*-

from croutera import version
from models.routers import Routers

class ModelListCommand(object):
    """ List all router models available """

    def valid(self):
        return True

    def execute(self):
        print("Models list: \n")
        for model in Routers.list():
            print(model+"\n")

        print("For more models open an issue on: \n ")
        print("https://github.com/CristianOliveiraDaRosa/croutera")

        return True

class RestartCommand(object):
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

class VersionCommand(object):
    """ Show current version installed """

    def valid(self):
        return True

    def execute(self):
        print('Croutera Version: ' + version())
        return True
