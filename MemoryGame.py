# Memory game
# Given : Difficulty
import random  # For generating sequence
import time  # For printing the seuqence to the user with time difference


def generate_sequence(difficulty):  # Generates a list of number from the PC with the length of difficulty
    sequence = []
    for number in range(1, (difficulty + 1)):
        sequence.append(random.randint(1, 102))
    return sequence


def get_list_from_user(difficulty):  # Takes input from the user and creates a list with the length of difficulty
    user_list = []
    print("Enter the numbers you just saw! and press enter after each number!", end='\r')
    for item in range(1, (difficulty + 1)):
        number = int(input())
        user_list.append(number)
    return user_list


def is_list_equal(difficulty, pc_sequence, user_list):  # compares two lists for match
    for num in range(0, difficulty):
        if user_list[num] != pc_sequence[num]:
            return False
    return True


def play(difficulty):
    pc_sequence = generate_sequence(difficulty)
    print("Lets play! :)")
    for number in pc_sequence:
        print(number, end='\r')
        time.sleep(.7)
    user_list = get_list_from_user(difficulty)
    if is_list_equal(difficulty, pc_sequence, user_list):
        print("You won!, great memory!")
        return True
    else:
        print("You lost! try again!")
        return False

