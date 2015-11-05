"""
  Authentication module
"""

class Auth(object):

    def login(self, username, password):
        """ Handle the router authentication into admin page. """
        print(username, password)
        return True
