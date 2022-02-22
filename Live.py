from GuessGame import guess_game
from MemoryGame import memory_game

# Define Welcome function with your name variable
def welcome(user_name=str):
    print("Enter your name:")
    user_name = input()
    print("Hello", user_name, "and welcome to the World of Games (WoG)")
    return user_name


# welcome()

# Define Game selection function which also validates that input range will remain from 1-3 and if input is different the function will exit.
def load_game(game_opt=int):
    print("\nPlease choose a game to play:"
          "\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back."
          "\n2. Guess Game - guess a number and see if you chose like the computer"
          "\n3. Currency Roulette - try and guess the value of a random amount of USD in IL")
    print("\nplease choose game from 1 to 3:")
    game_opt = int(input())
    if 4 > game_opt > 0:
        print(game_opt)
        return game_opt
    else:
        print("Wrong choice as ", game_opt, " is not a supported option to choose, exiting program!")
        exit(0)


#load_game()

# Define Game Level function which also validates that input range will remain from 1-5 and if input is different the function will exit.

def game_level(diff_level=int):
    print("Please choose game difficulty from 1 to 5:")
    diff_level = int(input())
    if 6 > diff_level > 0:
        print(diff_level)
        return diff_level
    else:
        print("Wrong choice as ", diff_level, " is not a supported option to choose, exiting program!")
        exit(0)

# game_level()

def play_game(game, diff):
    if game == 1:
        memory_game(diff)
    elif game == 2:
        guess_game(diff)

