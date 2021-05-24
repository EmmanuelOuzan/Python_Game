# Emmanuel's Ouzan GuessingGame
# main program MainGame.py
import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    # print(f"secret number {secret_number}")
    return secret_number


def get_guess_from_user(difficulty):
    return int(input(f"Please choose a number from one to {difficulty}"))


def compare_results(difficulty):
    if generate_number(difficulty) == get_guess_from_user(difficulty):
        print("Yay you got the same number!")
        return True
    else:
        print("the Computer choose something else!")
        return False


def play(difficulty):
    return compare_results(difficulty)


generate_number(2)