# Getting the difficulty from live.py
# opening file and summing
import os
from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    # Calculating user score
    score = (difficulty * 3) + 5
    # Check if file exists
    if os.path.isfile(SCORES_FILE_NAME):
        # Checks if file is not empty
        if os.stat(SCORES_FILE_NAME).st_size != 0:
            # Opens the file readable and names it file
            with open(SCORES_FILE_NAME, 'r') as file:
                total_score = int(file.read())
                score += total_score
    # If the file dose not exist, it will create a new file and write the score
    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(score))


add_score(5)




