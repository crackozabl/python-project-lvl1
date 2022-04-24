import prompt
from brain_games.games import even
from brain_games.games import calc
from brain_games.games import gcd
from brain_games.games import progression
from brain_games.games import prime


MAX_MOVES = 3


def read_user_name():
    return prompt.string('May I have your name? ')


def read_user_answer():
    return prompt.string('Your answer: ')


def generate_question(game_name):
    if game_name == even.GAME_NAME:
        return even.generate_question()
    elif game_name == calc.GAME_NAME:
        return calc.generate_question()
    elif game_name == gcd.GAME_NAME:
        return gcd.generate_question()
    elif game_name == progression.GAME_NAME:
        return progression.generate_question()
    elif game_name == prime.GAME_NAME:
        return prime.generate_question()
    else:
        print('ERROR: unknown game name')
        return ('no question', 'no answer')


def print_game_rules(game_name):

    if game_name == even.GAME_NAME:
        print(even.GAME_RULES)
    elif game_name == calc.GAME_NAME:
        print(calc.GAME_RULES)
    elif game_name == gcd.GAME_NAME:
        print(gcd.GAME_RULES)
    elif game_name == progression.GAME_NAME:
        print(progression.GAME_RULES)
    elif game_name == prime.GAME_NAME:
        print(prime.GAME_RULES)
    else:
        print('ERROR: unknown game name')


def play(game_name, max_moves=MAX_MOVES):
    user_name = read_user_name()
    print_game_rules(game_name)

    for move in range(0, max_moves):
        (question, answer) = generate_question(game_name)
        print(f'Question: {question}')
        user_answer = read_user_answer()

        if answer == user_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(.',
                  f'Correct answer was \'{answer}\'')
            print(f'Let\'s try again, {user_name}!')
            return

    print(f'Congratulations, {user_name}!')
