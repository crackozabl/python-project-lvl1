from random import random

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
GAME_NAME = 'even'
_NUMBER_MAX = 100
_NUMBER_MIN = 1


def generate_question():
    question_number = int(random() * _NUMBER_MAX) + _NUMBER_MIN

    return (str(question_number), 'yes' if question_number % 2 == 0 else 'no')
