import prompt

MAX_MOVES = 3


def play(game, max_moves=MAX_MOVES):

    user_name = prompt.string('May I have your name? ')

    print(game.GAME_RULES)

    for move in range(0, MAX_MOVES):
        (question, answer) = game.generate_question()
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
