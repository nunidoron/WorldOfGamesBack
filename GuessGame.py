# Request user to enter game difficulty level.
from random import randrange


def guess_game(game_guess_state=None, gen_num=0, game_diff_level=0):
    import random
    print("\nPlease choose a game Difficulty level greater than zero:")
    game_diff_level = input()

    # Validate that input value for Game Difficulty Level is larger than "1"
    if int(game_diff_level) <= 1:
        print("Wrong choice as ", game_diff_level, " is not a supported option to choose, exiting program!")
        exit(0)
    else:
        print("you selected valid Game Difficulty level =", game_diff_level)
    # Generate Random number from Game Difficulty level variable
    gen_num = randrange(1, int(game_diff_level), 1)
    print(gen_num)
    # Get user guess number and validate if it is equal to random number (True=Win Game) or not (False=Lost Game)
    print("\nPlease guess the secret number:")
    get_guess_from_user = input()
    if int(get_guess_from_user) == int(gen_num):
        game_guess_state = True
        print("\nAmazing - You've successfully guessed the secret number which is:", gen_num, " | ", game_guess_state)
    else:
        game_guess_state = False
        print("\nYou couldn't guess the right number and lost this game round! | ", game_guess_state, "| correct number was=", gen_num)

# guess_game()