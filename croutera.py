from courtera.cli import Cli
import argparse

def main():
    print("Croutera...")

    description = 'Simple terminal cli to manage modem / routers admin actions'

    parser = argparse.ArgumentParser(description = description)

    parser.add_argument(
        'model',
        help = 'Define router model. (--model-list to show models available)')

    parser.add_argument(
        'ip',
        help = 'Router ip address (ex: 192.168.100.1)')

    parser.add_argument(
        'user',
        help = 'Admin user of router interface.')

    parser.add_argument(
        'password',
        help = 'Admin user password of router interface.')

    args = parser.parse_args()

    print(args)

    Cli.execute_with(args)


if __name__ == '__main__':
    main()
