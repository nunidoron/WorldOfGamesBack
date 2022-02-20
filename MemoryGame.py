from __future__ import print_function

import collections
import os
import time


def memory_game(gen_num=list, game_diff_level=int, a=int, i=int, n=int, get_list_from_user=None, gen_list=list):
    print("\nPlease choose a game Difficulty level greater than zero:")
    game_diff_level = input()

    # Validate that input value for Game Difficulty Level is larger than "0"
    if int(game_diff_level) <= 0:
        print("Wrong choice as ", game_diff_level, " is not a supported option to choose, exiting program!")
        exit(0)
    else:
        print("you selected valid Game Difficulty level =", game_diff_level)

    # Setting length of the required list based on the user input for Difficulty level
    n = int(game_diff_level)

    # Generate random series of numbers based on n values (difficulty level) and print to screen for 0.7 second
    # using list comprehension + randrange() to generate random number list
    import random
    gen_list: int = [ random.randrange(1, 101, 1) for i in range(n) ]

    # printing generated random list for 0.7 sec
    print(gen_list)
    time.sleep(0.7)
    print("\n" * 100)

    # Get user list in a row with space separation
    print("\nPlease enter", n, "numbers in a row with space between each number")

    # Convert user list to list variable
    get_list_from_user = list(map(int, input("\nEnter the numbers : ").strip().split()))

    # print(get_list_from_user)
    print("\nYou inserted the following list: ", get_list_from_user)

    # using collections.Counter() to check if user input list equal or not to generated random list
    if collections.Counter(get_list_from_user) == collections.Counter(gen_list):
        print("True answer | The lists are identical")
    else:
        print("False answer | The lists are not identical")


# memory_game()
