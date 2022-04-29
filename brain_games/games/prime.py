from random import random


GAME_DESCRIPTION = \
    'Answer "yes" if given number is prime. Otherwise answer "no".'

_NUMBER_MAX = 10
_NUMBER_MIN = 1


def _is_prime(n):

    if n == 2 or n == 3:
        return True

    if n == 1 or n % 2 == 0 or n % 3 == 0:
        return False

    for x in range(5, int(n ** 0.5), 2):
        if n % x == 0:
            return False

    return True


def generate_move_data():
    number = int(random() * _NUMBER_MAX) + _NUMBER_MIN
    answer = 'yes' if _is_prime(number) else 'no'

    return (str(number), str(answer))
