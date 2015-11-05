"""
  Models routers implementations
"""

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

class DLinkDir610(Router):
    """
    Implementation for D-link DR610
    see: http://www.dlink.com.br/produto/dir-610-a1
    """

    def login(self, user, password):
        pass


