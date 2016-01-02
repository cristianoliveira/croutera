#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from croutera.cli import ArgsParserBuilder, Cli


def run():
    print("Croutera...")

    args = ArgsParserBuilder.build(sys.argv[1:])
    if not Cli.validate(args):
        show_help()
        return

    cmd = Cli.command(args)
    if cmd.valid() and cmd.execute():
        print('Command executed.')
    else:
        print('Command was not executed.')

def show_help():
     print('--------HELP-------')
     ArgsParserBuilder.build_help()

if __name__ == '__main__':
    run()
