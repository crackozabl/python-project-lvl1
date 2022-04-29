from random import random


GAME_DESCRIPTION = 'What number is missing in the progression?'
_START_NUMBER_MAX = 10
_START_NUMBER_MIN = 1
_STEP_MAX = 10
_PROGRESSION_LENGTH_MIN = 5


def _list_to_string(list, none_str=".."):
    str_values = [str(x) if x is not None else none_str for x in list]
    return " ".join(str_values)


def generate_move_data():
    start = int(random() * _START_NUMBER_MIN) + _START_NUMBER_MIN
    step = int(random() * _STEP_MAX) + 1
    end = step * (int(random() * _STEP_MAX) + _PROGRESSION_LENGTH_MIN) + start
    progression = list(range(start, end, step))
    x_index = int(random() * (len(progression) - 1)) + 1

    answer = progression[x_index]
    progression[x_index] = None
    question = _list_to_string(progression)

    return (str(question), str(answer))
