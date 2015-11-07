#!/usr/bin/env python
# -*- coding: utf-8 -*-

from croutera.cli import Cli
import argparse

def main():
    print("Croutera...")

    description = 'Simple terminal cli to manage modem / routers admin actions'

    parser = argparse.ArgumentParser(description = description,
                                     argument_default=argparse.SUPPRESS)

    parser.add_argument(
        'model',
        nargs = '?',help = 'Router model (see: --list-model)')

    parser.add_argument(
        'username',
        nargs = '?', help = 'User name to access admin page')
    parser.add_argument(
        'password',
        nargs = '?',help = 'Password to access admin page')

    parser.add_argument(
        '-restart', dest = 'restart',
        action = 'store_true', default=False,
        help = 'Reset router by model.'
    )

    parser.add_argument(
        '-list-models', dest = 'list_models',
        action = 'store_true',  default=False,
        help = 'Shows models available'
    )

    args = parser.parse_args()
    Cli.command(args).execute()

if __name__ == '__main__':
    main()
