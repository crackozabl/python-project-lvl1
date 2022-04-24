import prompt
from random import random

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
GAME_NAME = 'even'


def generate_question():
    question_number = int(random() * 100)

    return (str(question_number), 'yes' if question_number % 2 == 0 else 'no')


def read_user_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer
