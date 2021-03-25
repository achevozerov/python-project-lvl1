#!/usr/bin/env python3

"""Contains main functions who manage all game."""

from brain_games import cli


def main():
    """Print welcome message then call welcome_user func."""
    print('Welcome to the Brain Games!')
    username = cli.welcome_user()
    print('Hello', username, '!')


if __name__ == '__main__':
    main()
