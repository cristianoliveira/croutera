#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from croutera.cli import ArgsParserBuilder, Cli


def run():
    print("Croutera...")

    args = ArgsParserBuilder.build(sys.argv[1:])
    cmd = Cli.command(args)

    if not cmd:
        print('--------HELP-------')
        ArgsParserBuilder.build_help()
        return False

    if cmd.valid() and cmd.execute():
        print('Command executed.')
        return True
    else:
        print('Command was not executed.')
        return False


if __name__ == '__main__':
    run()
