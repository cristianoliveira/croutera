#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .cli import ParserBuilder, Cli


def run():
    print("Croutera...")
    args = ParserBuilder.build().parse_args()
    cmd = Cli.command(args)
    if cmd and cmd.valid():
        cmd.execute()
    else:
        print('--------HELP-------')
        ParserBuilder.build_help()

    return True


if __name__ == '__main__':
    run()
