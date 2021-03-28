"""Contains main function that starts the progression game."""

from random import randint

import prompt
from brain_games import cli


def check_right(answer, right_answer):
    """
    Generate question and check his right.

    Parameters:
        answer (str): user answer
        right_answer (int): hidding number
    """
    if right_answer == int(answer):
        return True
    return False


def generate_sequence(name, right_answer_count=0):
    """
    Generate question and check his right.

    Parameters:
        name (str): user name
        right_answer_count (int): integer number meaning right answer count
    """
    if right_answer_count == 3:
        print(f'Congratulations, {name}!')
        return
    sequence_length = randint(5, 10)
    start = randint(2, 30)
    step = randint(2, 9)
    hidden_num = randint(1, sequence_length)
    seq_list = []
    for i in range(sequence_length):
        if i == hidden_num:
            right_answer = start
            start += step
            seq_list.append('..')
            continue
        seq_list.append(start)
        start += step
    print(f'Question: {seq_list}')
    answer = prompt.string('Your answer? ', empty=False)
    if check_right(answer, right_answer):
        right_answer_count += 1
        print('Correct!')
        generate_sequence(name, right_answer_count)
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {right_answer}.')
        print(f"Let's try again, {name}!")
    return


def main():
    """Launch the progression game."""
    name = cli.welcome_user()
    print('What number is missing in the progression?')
    generate_sequence(name)


if __name__ == '__main__':
    main()
