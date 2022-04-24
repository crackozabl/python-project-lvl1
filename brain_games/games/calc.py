import prompt
from random import random

GAME_RULES = 'What is the result of the expression?'
GAME_NAME = 'calc'
_OPERATORS = ['*', '+', '-']
_OPERAND_MAX = 3
_OPERAND_MIN = 1


def generate_question():
    operator = _OPERATORS[int(random() * 3)]
    operand_1 = int(random() * _OPERAND_MAX) + _OPERAND_MIN
    operand_2 = int(random() * _OPERAND_MAX) + _OPERAND_MIN

    question = f'{operand_1} {operator} {operand_2}'
    answer = None

    if operator == _OPERATORS[0]:
        answer = operand_1 * operand_2
    elif operator == _OPERATORS[1]:
        answer = operand_1 + operand_2
    elif operator == _OPERATORS[2]:
        answer = operand_1 - operand_2

    return (question, str(answer))


def read_user_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer
