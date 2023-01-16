import random
import logging
logging.basicConfig(level=logging.DEBUG)

def win_or_lose(user, computer):
    if user == computer:
        return "draw"
    if user == "paper" and computer == "rock":
        return "win"
    if user == "rock" and computer == "scissors":
        return "win"
    if user == "scissors" and computer == "paper":
        return "win"
    if user == "paper" and computer == "scissors":
        return "lose"
    if user == "rock" and computer == "paper":
        return "lose"
    if user == "scissors" and computer == "rock":
        return "lose"

choices = ["rock", "paper", "scissors"]
score = 0
while score < 3:
    print("This is your turn")
    user_choice = input("Please choose rock/paper/scissors:")
    if user_choice in choices:
        computer_choice = random.choice(choices)
        result = win_or_lose(user_choice, computer_choice)
        if result == "win":
            score += 1
        
        logging.info(f"Current score '{score}'")

        print(
            f"Your choice: '{user_choice}'; Computer's choice: '{computer_choice}'; Result:'{result}'"
        )

        if result == "lose":
            break
    else:
        print(f"what you typed is not a valid answer")



if score == 3:
    print('you won')
else:
    print('you lose. game over...')