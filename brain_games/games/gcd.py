from math import gcd
from random import random


GAME_RULES = 'Find the greatest common divisor of given numbers.'
GAME_NAME = 'gcd'
_NUMBER_MAX = 10
_NUMBER_MIN = 1


def generate_question():
    number_1 = int(random() * _NUMBER_MAX) + _NUMBER_MIN
    number_2 = int(random() * _NUMBER_MAX) + _NUMBER_MIN

    question_numbers = f'{number_1} {number_2}'
    answer = gcd(number_1, number_2)

    return (str(question_numbers), str(answer))
