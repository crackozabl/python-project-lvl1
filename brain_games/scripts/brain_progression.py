#!/usr/bin/env python

from brain_games import engine
from brain_games.games import progression

# brain-progression

# WIN

# Welcome to the Brain Games!
# May I have your name? Sam
# Hello, Sam!
# What number is missing in the progression?
# Question: 5 7 9 11 13 .. 17 19 21 23
# Your answer: 15
# Correct!
# Question: 2 5 8 .. 14 17 20 23 26 29
# Your answer: 11
# Correct!
# Question: 14 19 24 29 34 39 44 49 54 ..
# Your answer: 59
# Correct!
# Congratulations, Sam!


# LOOSE

# Question: 5 7 9 11 13 .. 17 19 21 23
# Your answer: 1
# '1' is wrong answer ;(. Correct answer was '15'.
# Let's try again, Sam!

def main():
    engine.play(progression.GAME_NAME)


if __name__ == '__main__':
    main()
