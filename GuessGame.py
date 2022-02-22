# Request user to enter game difficulty level.
from random import randrange


def guess_game(game_diff_level):
    game_guess_state = None
    gen_num = 0
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