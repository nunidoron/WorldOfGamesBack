# Used https://pypi.org/project/CurrencyConverter/ as the currency converter API after deploying "pip install
# currencyconverter"
import collections
import itertools
import requests
import sets
import subset as subset


def currencyroulettegame(c=int, x=int, t=int, d=int, get_user_dollar_input=int,
                         get_guess_from_user=str):
    # Prepare the currency converter function
    from currency_converter import CurrencyConverter
    c = CurrencyConverter()

    # Get user dollar value input
    get_user_dollar_input = input("\nEnter Dollar value to convert to ILS: ")

    # Get user game difficulty value input
    d = input("\nPlease enter Game difficulty (1-5): ")

    if int(d) <= 5:
        # Convert from Dollar to ILS and place value in t variable
        t = c.convert(get_user_dollar_input, 'USD', 'ILS')
        # print("real conversion value for", get_user_dollar_input, "$ will be", t, "ILS") # only for debug
        get_money_interval = [int(t) - (5 - int(d)), int(t) + (5 - int(d))]
        print(get_money_interval)  # only for debug

        # Get user guess input
        get_guess_from_user:str = input("\nGuess the converted ILS value")
        # print(get_guess_from_user, get_money_interval)
        print("You guessed the following value =", get_guess_from_user)

        # Check if user guess was matching one of the two money interval values
        s1 = [get_guess_from_user]
        s2 = map(str, get_money_interval)
        s2 = list(s2)
        print(s1, s2)
        s3 = s1.issubset(s2)
        if s3 == "True":
            print("\nSuccess, you've Won and the correct number is", get_guess_from_user)
        else:
            print("\nOH NO, you lose the game!")

    else:
        print("\nWrong Game difficulty value beyond allowed range (1-5), existing")
        return


# currencyroulettegame()
