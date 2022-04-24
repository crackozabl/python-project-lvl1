from random import random


GAME_RULES = 'What number is missing in the progression?'
GAME_NAME = 'progression'
_NUMBER_MAX = 10
_NUMBER_MIN = 1
_PROGRESSION_LEN_MIN = 5


def generate_question():
    start = int(random() * 100)
    # print('DBG: start ', progression_start)
    step = int(random() * 10) + 1
    # print('DBG: step', progression_step)
    end = step * (int(random() * 5) + _PROGRESSION_LEN_MIN) + start
    # print('DBG: end', progression_end)
    progression = list(range(start, end, step))
    x_index = int(random() * len(progression))
    # print('DBG: ', progression)
    # print('DBG: ', x_index)
    question = \
        " ".join(str(x) for x in progression[0:x_index]) + \
        " .. " + \
        " ".join(str(x) for x in progression[x_index + 1:])

    answer = progression[x_index]

    return (str(question), str(answer))
