#!/usr/bin/env python
# -*- coding: utf-8 -*-

from croutera.cli import Cli
import argparse

def main():
    print("Croutera...")

    description = 'Simple terminal cli to manage modem / routers admin actions'

    parser = argparse.ArgumentParser(description = description)

    parser.add_argument(
        '-l', '--models-list', action='store_true',
        help = 'Shows models available')

    # parser.add_argument(
    #     '-m', '--model',
    #     help = 'Define router model. (--model-list to show models available)')
    #
    # parser.add_argument(
    #     '--ip',
    #     help = 'Router ip address (ex: 192.168.100.1)')
    #
    # parser.add_argument(
    #     'user',
    #     help = 'Admin user of router interface.')
    #
    # parser.add_argument(
    #     'password',
    #     help = 'Admin user password of router interface.')
    #
    # parser.add_argument(
    #     '-l',
    #     help = 'Show list of model available.')

    args = parser.parse_args()
    Cli().execute(args)


if __name__ == '__main__':
    main()
