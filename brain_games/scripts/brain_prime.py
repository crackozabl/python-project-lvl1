#!/usr/bin/env python

from brain_games import engine
from brain_games.games import prime

# Welcome to the Brain Games!
# May I have your name? Sam
# Hello, Sam!
# Answer "yes" if given number is prime. Otherwise answer "no".
# Question: 7
# Your answer: yes
# Correct!


def main():
    engine.play(prime.GAME_NAME)


if __name__ == '__main__':
    main()
