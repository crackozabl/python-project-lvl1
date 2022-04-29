import prompt

MOVE_MAX = 3


def play(game):

    user_name = prompt.string('May I have your name? ')

    print(game.GAME_DESCRIPTION)

    for move in range(0, MOVE_MAX):
        (question, answer) = game.generate_move_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if answer == user_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(.',
                  f'Correct answer was \'{answer}\'')
            print(f'Let\'s try again, {user_name}!')
            return

    print(f'Congratulations, {user_name}!')
