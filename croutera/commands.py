#!/usr/bin/env python
# -*- coding: utf-8 -*-

from croutera.version import version
from croutera.models import Routers


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

class VersionCommand(Command):
    """ Show current version installed """

    def execute(self):
        print('Croutera Version: ' + version())
        return True


class AuthorizeCommand(Command):

    def __init__(self, router, user, password):
        self.router = router
        self.user = user
        self.password = password

    def execute(self):
        print('Authorizing...')
        return self.router.login(self.user, self.password)

class RestartCommand(Command):

    def __init__(self, router):
        self.router = router

    def execute(self):
        print('Router restarting...')
        return self.router.restart()


class ShowWifiPassCommand(Command):

    def __init__(self, router):
        self.router = router

    def execute(self):
        print("Current Wifi Pass: " + self.router.wifi_pass())
        return True

class ChainCommand(Command):
    """ Compose a chain of commands
    to be executed in a roll.
    """
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            if not command.execute():
                return False
        return True

