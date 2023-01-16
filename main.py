"""
requirments:
"""
# read input from command line (your turn)
# opponent to select rock, paper, or scissors 
# winner must win x times 


import random
import logging
logging.basicConfig(level=logging.DEBUG)

choices = ["rock", "paper", "scissors"]
score = 0
while score < 3:
    print("This is your turn")
    user_choice = input("Please choose rock/paper/scissors:")
    if user_choice in choices:
        computer_choice = random.choice(choices)
        logging.debug('Current score %s' % score)

        print(
            f"Your choice: '{user_choice}'; Computer's choice: '{computer_choice}'"
        )
    else:
        print(f"what you typed is not a valid answer")

print('you won')