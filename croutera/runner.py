#!/usr/bin/env python
# -*- coding: utf-8 -*-

from croutera.cli import ParserBuilder, Cli

def run():
    print("Croutera...")
    args = ParserBuilder.build().parse_args()
    cmd = Cli.command(args)
    if cmd and cmd.valid():
        cmd.execute()
    else:
        ParserBuilder.build().parse_args(['-h'])

    return True


if __name__ == '__main__':
    run()
