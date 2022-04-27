from random import random


GAME_RULES = 'What number is missing in the progression?'
GAME_NAME = 'progression'
_NUMBER_MAX = 10
_NUMBER_MIN = 1
_STEP_MAX = 10
_PROGRESSION_LEN_MIN = 5


def _array_to_string(array):
    return " ".join(str(x) for x in array)


def generate_question():
    start = int(random() * _NUMBER_MIN)
    step = int(random() * _STEP_MAX) + 1
    end = step * (int(random() * _STEP_MAX) + _PROGRESSION_LEN_MIN) + start
    progression = list(range(start, end, step))
    x_index = int(random() * (len(progression) - 1)) + 1

    question_before_x = _array_to_string(progression[0:x_index])
    question_after_x = _array_to_string(progression[(x_index + 1):])
    question = question_before_x + " .. " + question_after_x

    answer = progression[x_index]

    return (str(question), str(answer))
