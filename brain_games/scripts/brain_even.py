#!/usr/bin/env python

from brain_games import engine
from brain_games.games import even


# WIN
# brain-even
# Welcome to the Brain Games!
# May I have your name? Sam
# Hello, Sam!
# Answer "yes" if the number is even, otherwise answer "no".
# Question: 15
# Your answer: no
# Correct!
# Question: 6
# Your answer: yes
# Correct!
# Question: 7
# Your answer: no
# Correct!
# Congratulations, Sam!


# LOOSE
# 'yes' is wrong answer ;(. Correct answer was 'no'.
# Let's try again, Bill!


def main():
    engine.play(even.GAME_NAME)


if __name__ == '__main__':
    main()
