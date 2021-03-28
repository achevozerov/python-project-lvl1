"""Contains main function that starts the calc game"""

from random import randint

import prompt
from brain_games import cli


def generate_expression():
    """
    Generate expression for calc game.
    
    Returns:
        first_digit (int): first num in expression
        second_digit (int): second num in expression
        expression_type (str): can be addition, substraction and multiplication
    """
    typo = randint(1, 3)
    if typo == 1:
        expression_type = 'addition'
    elif typo == 2:
        expression_type = 'substraction'
    else:
        expression_type = 'multiplication'
    first_digit = randint(1, 100)
    if expression_type == 'multiplication':
        second_digit = randint(2, 10)
    else:
        second_digit = randint(1, 100)
    return expression_type, first_digit, second_digit


def generate_question(name, right_answer_count=0):
    """
    Generate answer and manage game processing.

    Parameters:
        name (str): user name
        right_answer_count (int): integer number meaning right answer count
    """
    if right_answer_count == 3:
        print('Congratulations,', name, '!')
        return
    expression_type, first_digit, second_digit = generate_expression()
    if expression_type == 'addition':
        print('Question:', first_digit, '+', second_digit)
        right_answer = first_digit + second_digit
    elif expression_type == 'substraction':
        print('Question:', first_digit, '-', second_digit)
        right_answer = first_digit - second_digit
    elif expression_type == 'multiplication':
        print('Question:', first_digit, '*', second_digit)
        right_answer = first_digit * second_digit
    answer = prompt.string('Your answer: ', empty=False)
    if int(answer) == right_answer:
        right_answer_count += 1
        print('Correct!')
    else:
        print(str(answer), 'is wrong answer ;(. Correct answer was', str(right_answer))
        print('Let\'s try again,', name, '!')
        return
    generate_question(name, right_answer_count)
    


def main():
    """Launch the calc game"""
    # Greets user
    name = cli.welcome_user()
    # Write rules
    print('What is the result of the expression?')
    generate_question(name)
