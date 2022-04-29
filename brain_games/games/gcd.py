from math import gcd
from random import random


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
_NUMBER_MAX = 10
_NUMBER_MIN = 1


def generate_move_data():
    number_1 = int(random() * _NUMBER_MAX) + _NUMBER_MIN
    number_2 = int(random() * _NUMBER_MAX) + _NUMBER_MIN

    question_numbers = f'{number_1} {number_2}'
    answer = gcd(number_1, number_2)

    return (str(question_numbers), str(answer))
