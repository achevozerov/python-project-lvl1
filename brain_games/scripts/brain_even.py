"""Contains play-even function who launch even game."""

from random import randint

import prompt
from brain_games import cli


def generate_number():
    """
    Generate random between 1 and 100.

    Returns:
        randint(1, 100): random integer 1 of 100.
    """
    return randint(1, 100)


def check_right(question_num, answer):
    """
    Check rightly answer.

    Parameters:
        question_num (int): question number
        answer (int): answer receiver from the user

    Returns:
        result (bool): checker answer.
    """
    answer_is_right = False
    if question_num % 2 == 0 and answer == 'yes':
        answer_is_right = True
    elif question_num % 2 != 0 and answer == 'no':
        answer_is_right = True
    return answer_is_right


def generate_answer(name, right_answer_count=0):
    """
    Generate answer and check his right.

    Parameters:
        name (str): user name
        right_answer_count (int): integer number meaning right answer count
    """
    if right_answer_count == 3:
        print('Congratulations,', name, '!')
        return
    question_num = generate_number()
    print('Question:', question_num)
    answer = prompt.string('Your answer? ', empty=False)
    answer_is_right = check_right(question_num, answer)
    if answer_is_right:
        print('Correct!')
        right_answer_count += 1
        generate_answer(name, right_answer_count)
    else:
        print('Try again', name, '!')


def play_even():
    """Launch even game."""
    # Greets user
    name = cli.welcome_user()
    # Rules
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # First question
    generate_answer(name)


if __name__ == '__main__':
    play_even()
