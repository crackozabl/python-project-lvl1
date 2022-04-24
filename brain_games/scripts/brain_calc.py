#!/usr/bin/env python

from brain_games.games import calc
from brain_games import engine


def main():
    engine.play(calc.GAME_NAME)


if __name__ == '__main__':
    main()
