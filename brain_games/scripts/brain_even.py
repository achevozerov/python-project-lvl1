"""Contains play-even function who launch even game."""

import prompt
from brain_games import cli
from random import randint


def generate_number():
    """
    Generate random between 1 and 100.
    
    Returns:
            randint(1, 100): random integer 1 of 100.
    """
    return randint(1, 100)

def check_right(q, answer):
    """
    Check rightly answer.
    
    Arguments:
            q (int): number in question.
            answer (int): answer receiver from the user.

    Returns:
            result (bool): checker answer.
    """
    result = False
    if q % 2 == 0 and answer == 'yes':
        result = True
    elif q % 2 != 0 and answer == 'no':
        result = True
    return result

def generate_answer(name, right_answer_count=0):
    """
    Generate answer and check his right.

    Arguments:
            name (str): user name.
            right_answer_count (int): integer number indicating right answer count.
    """
    if right_answer_count == 3:
        print('Congratulations,', name, '!')
        return 
    q = generate_number()
    print('Question:', q)
    answer = prompt.string('Your answer? ', empty=False)
    result = check_right(q, answer)
    if result:
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
    q = generate_number()
    generate_answer(name)

if __name__ == '__main__':
    play_even()