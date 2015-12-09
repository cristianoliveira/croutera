#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from croutera.cli import ArgsParserBuilder, Cli


def run():
    print("Croutera...")

    args = ArgsParserBuilder.build(sys.argv[1:])
    cmd = Cli.command(args)

    if cmd and cmd.valid():
        cmd.execute()
    else:
        print('--------HELP-------')
        ArgsParserBuilder.build_help()

    return True


if __name__ == '__main__':
    run()
