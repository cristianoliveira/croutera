#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Croutera - The Cli Router Admin
"""

from croutera.cli import Cli, ParserBuilder

def main():
    """ Entry point """

    print("Croutera...")
    args = ParserBuilder.build().parse_args()
    Cli.command(args).execute()

if __name__ == '__main__':
    main()
