#!/usr/bin/env python3

"""Contains main functions who greets user."""

from brain_games import cli


def main():
    """
    Print welcome message then call welcome_user func.

    Returns:
            username (str): name choiced by user.
    """
    print('Welcome to the Brain Games!')
    username = cli.welcome_user()
    print('Hello', username, '!')
    return username


if __name__ == '__main__':
    main()
