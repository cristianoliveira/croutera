
from abc import ABCMeta, abstractmethod

class Router(object):
    __metaclass__ = ABCMeta

    config = {
        'ip': '192.168.0.1',
        'uris': {
            'login': '',
            'reboot': '',
            'wifi_settings': ''
        }
    }

    @abstractmethod
    def login(self, user, password):
        """ Provide logic to auth into router admin page """
        pass

    def restart(self):
        """ Provide logic to restart the router (logged action) """
        self._command_not_implemented()
        return False 

    def wifi_pass(self):
        """ Provide logic to show the wifi password """
        self._command_not_implemented()
        return ""

    def _command_not_implemented(self):
        print('This command was not implemented for this model.')

    def endpoint(self, uri):
        ' provide a url to reach a given endpoint '
        return "http://%s/%s" % (self.config['ip'], self.config['uris'][uri])
