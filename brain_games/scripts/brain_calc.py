#!/usr/bin/env python

from brain_games.games import calc
from brain_games import engine

# WIN
# brain-calc

# Welcome to the Brain Games!
# May I have your name? Sam
# Hello, Sam!
# What is the result of the expression?
# Question: 4 + 10
# Your answer: 14
# Correct!
# Question: 25 - 11
# Your answer: 14
# Correct!
# Question: 25 * 7
# Your answer: 175
# Correct!
# Congratulations, Sam!


# LOOSE
# Question: 25 * 7
# Your answer: 145
# '145' is wrong answer ;(. Correct answer was '175'.
# Let's try again, Sam!


def main():
    engine.play(calc.GAME_NAME)


if __name__ == '__main__':
    main()
