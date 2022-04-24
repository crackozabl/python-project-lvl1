#!/usr/bin/env python

from brain_games import engine
from brain_games.games import gcd

# brain-gcd

# WIN
# Welcome to the Brain Games!
# May I have your name? Sam
# Hello, Sam!
# Find the greatest common divisor of given numbers.
# Question: 25 50
# Your answer: 25
# Correct!
# Question: 100 52
# Your answer: 4
# Correct!
# Question: 3 9
# Your answer: 3
# Correct!
# Congratulations, Sam!


# LOOSE
# Question: 25 50
# Your answer: 1
# '1' is wrong answer ;(. Correct answer was '25'.
# Let's try again, Sam!


def main():
    engine.play(gcd.GAME_NAME)


if __name__ == '__main__':
    main()
