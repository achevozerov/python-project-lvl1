"""Contains main function that starts the gcd (great common divisor) game."""

from random import randint

import prompt
from brain_games import cli


def check_right(right_answer, answer):
    """
    Check rightly answer.

    Parameters:
        right_answer (int): question number
        answer (int): answer received from the user

    Returns:
        result (bool): checked answer.
    """
    if right_answer == int(answer):
        return True
    print(f'{int(answer)} is wrong answer ;(. Correct answer was {int(right_answer)}')
    return False


def find_max_common_divisor(first_num, second_num, name):
    """
    Find max common divisor of two numbers.

    Parameters:
        first_num (int): first number
        second_num (int): second number
        name (string): user name

    Returns:
        max(common_elements) (int): max common divisor of two numbers
    """
    first_divisors_list = []
    second_divisors_list = []
    for i in range(2, first_num + 1):
        if first_num % i == 0:
            first_divisors_list.append(i)
    for i in range(2, second_num + 1):
        if second_num % i == 0:
            second_divisors_list.append(i)
    common_elements = [x for x in first_divisors_list if x in second_divisors_list]
    if len(common_elements) == 0:
        return 'uncorrect elements was generated'
    return max(common_elements)


def generate_questions(name, right_answer_count=0):
    """
    Generate question and check his right.

    Parameters:
        name (str): user name
        right_answer_count (int): integer number meaning right answer count
    """
    if right_answer_count == 3:
        print('Congratulations,', name, '!')
        return
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    right_answer = find_max_common_divisor(first_num, second_num, name)
    if right_answer == 'uncorrect elements was generated':
        generate_questions(name, right_answer_count)
    else:
        print('Question:', first_num, second_num)
        answer = prompt.string('Your answer? ', empty=False)
        if check_right(right_answer, answer):
            print('Correct!')
            right_answer_count += 1
            generate_questions(name, right_answer_count)
        else:
            return


def main():
    """Launch the gcd game."""
    name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    generate_questions(name)


if __name__ == '__main__':
    main()
