from random import random


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
_NUMBER_MAX = 100
_NUMBER_MIN = 1


def generate_move_data():
    question_number = int(random() * _NUMBER_MAX) + _NUMBER_MIN

    return (str(question_number), 'yes' if question_number % 2 == 0 else 'no')
