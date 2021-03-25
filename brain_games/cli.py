"""Use func welcome to ask username."""

import prompt


def welcome_user():
    """
    Ask from user his name then print welcome string.

    Returns:
            name (str): user name.
    """
    name = prompt.string('May I have your name? \n', empty=False)

    return name
