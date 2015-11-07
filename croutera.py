#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from croutera.cli import Cli, ParserBuilder

def main():
    print("Croutera...")
    args = ParserBuilder.build().parse_args()
    Cli.command(args).execute()

if __name__ == '__main__':
    main()
