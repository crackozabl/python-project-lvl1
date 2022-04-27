from random import random

GAME_RULES = 'What is the result of the expression?'
GAME_NAME = 'calc'
_OPERATORS = ['*', '+', '-']
_OPERAND_MAX = 3
_OPERAND_MIN = 1


def generate_question():
    operator = _OPERATORS[int(random() * len(_OPERATORS))]
    operand_1 = int(random() * _OPERAND_MAX) + _OPERAND_MIN
    operand_2 = int(random() * _OPERAND_MAX) + _OPERAND_MIN

    question = f'{operand_1} {operator} {operand_2}'
    answer = None

    if operator == '*':
        answer = operand_1 * operand_2
    elif operator == '+':
        answer = operand_1 + operand_2
    elif operator == '-':
        answer = operand_1 - operand_2

    return (question, str(answer))
