
from abc import ABCMeta, abstractmethod

class Router(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def login(self, user, password):
        """ Provide logic to auth into router admin page """
        pass

    @abstractmethod
    def restart(self):
        """ Provide logic to restart the router (logged action) """
        pass

