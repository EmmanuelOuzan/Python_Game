import GuessGame
import MemoryGame
import CurrencyRouletteGame
import Score


def welcome(name):
    return f"Hello {name} and welcome to the World Of Games(WoG).\nHere you can find many cool games to play."


def load_game():
    print('''
Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 0.7 seconds and you have to
    guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    ''')

    game_number = input()
    game_difficulty = input("Please choose game difficulty from 1 to 5")
    if (game_number.isdigit() is True) and (game_difficulty.isdigit() is True):
        game_number = int(game_number)
        game_difficulty = int(game_difficulty)
        if not ((0 < game_number < 4) and (0 < game_difficulty < 6)):
            print("Please choose a game number from 1 to 3 & a difficulty from 1 to 5")
            load_game()
    else:
        print("Please type only numbers")
        load_game()

    if game_number == 1:
        print("Starting Memory game")
        result = MemoryGame.play(game_difficulty)
    if game_number == 2:
        print("Starting Guess Game")
        result = GuessGame.play(game_difficulty)
    if game_number == 3:
        print("Starting Currency Roulette game")
        result = CurrencyRouletteGame.play(game_difficulty)

    if result is True:
        Score.add_score(game_difficulty)