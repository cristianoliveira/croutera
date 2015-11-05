"""
  Cli terminal module
"""

from auth import Auth

class Cli(object):

    @staticmethod
    def execute_with(args):
        """ Handle execution of args commands """

        auth = Auth()
        auth.login(args.user, args.password)

        print("execute ", args)

