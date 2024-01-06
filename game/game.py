import random
import sys


def meet_condition():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return apply(level)

        except ValueError:
            continue


def apply(level):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                pass
        except ValueError:
            continue
        jmare = random.randint(1, level)
        if guess < jmare:
            print("Too small!")

        elif guess > jmare:
            print("Too large!")

        elif guess == jmare:
            sys.exit("Just right!")


meet_condition()
