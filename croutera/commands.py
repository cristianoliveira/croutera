#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .version import version
from .models.routers import Routers


class Command(object):

    def valid(self):
        """ Implement logic for command validation """
        return True

    def execute(self):
        """ Command process """
        raise NotImplementedError('Command not implemented')


class ModelListCommand(Command):
    """ List all router models available """

    def execute(self):
        print("Models list: \n")
        for model in Routers.list():
            print(model+"\n")

        print("For more models open an issue on: \n ")
        print("https://github.com/CristianOliveira/croutera")

        return True


class AuthenticatedCommand(Command):
    """  Commands which require login

    Args:
        :data (hash): contains
            model (string): Router model name
            username (string): Admin user name
            password (string): Admin password
            ip (string): Optional Router IP
    """
    def __init__(self, data):
        self.manuf = data['manufacturer']
        self.model = data['model']
        self.router = Routers.get(self.manuf, self.model)()
        self.router.ip = data.get('ip')
        self.router.login(data['username'], data.get('password'))


class RestartCommand(AuthenticatedCommand):

    def execute(self):
        print('Router restarting...')
        return self.router.restart()


class ShowWifiPassCommand(AuthenticatedCommand):

    def execute(self):
        print("Current Wifi Pass: " + self.router.wifi_pass())
        return True


class VersionCommand(Command):
    """ Show current version installed """

    def execute(self):
        print('Croutera Version: ' + version())
        return True
