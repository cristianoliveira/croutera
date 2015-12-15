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


class RouterCommand(Command):
    """ Commands executed in the given router

    Args:
        router (base.Router)
    """
    def __init__(self, router):
       self.router = router


class RestartCommand(RouterCommand):

    def execute(self):
        print('Router restarting...')
        return self.router.restart()


class ShowWifiPassCommand(RouterCommand):

    def execute(self):
        print("Current Wifi Pass: " + self.router.wifi_pass())
        return True
