# CurrencyRouletteGame by Emmanuel Ouzan
# Then use the conversion API to pull conversations :
#  https://freecurrencyapi.net/#documentationSection
import requests
import random


def get_money_interval(random_number):
    # getting the currency for that number
    request = requests.get("https://freecurrencyapi.net/api/v1/latest?base_currency=USD")
    currency = request.json()
    ILS = currency['rates']['ILS']
    # Calculating the exchange rate
    exchange = random_number * ILS
    return exchange


def get_guess_from_user(random_number):
    print(f"Hello dear User! The random number to be converted is : {random_number}")
    currency_guess = input("Please guess the currency Exchange for the random number!")
    if currency_guess.replace('.', '').isdigit():
        currency_guess = float(currency_guess)
    else:
        print("Please enter only a number! :) ")
        get_guess_from_user(random_number)
    return currency_guess


def play(difficulty):
    # Generating a random number to exchange:
    random_number = random.randint(1, 100)
    # Getting input from the user for the currency
    user_number = get_guess_from_user(random_number)
    # Calls the Converting API to get the conversation rate
    exchange_rate = get_money_interval(random_number)
    print(exchange_rate)
    if (exchange_rate - (5 - difficulty)) <= user_number <= (exchange_rate + (5 - difficulty)):
        print("You are right! you won!")
        return True
    else:
        print("You lost mate! You are wrong!")
        return False
