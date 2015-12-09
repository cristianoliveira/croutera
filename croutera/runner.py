#!/usr/bin/env python
# -*- coding: utf-8 -*-

from croutera.cli import ArgsParserBuilder, Cli


def run():
    print("Croutera...")
    argsparser = ArgsParserBuilder.build()
    cmd = Cli.command(argsparser.parse_args())
    if cmd and cmd.valid():
        cmd.execute()
    else:
        print('--------HELP-------')
        ArgsParserBuilder.build_help()

    return True


if __name__ == '__main__':
    run()
