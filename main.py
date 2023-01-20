import random
import logging
import csv
logging.basicConfig(filename="score.log", level=logging.DEBUG)

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

def printScores():
    with open('score.log') as logfile:
        lines = logfile.read().splitlines() #splitlines make lines into an array
    with open('scores.csv', 'w+') as csvfile:
        fieldnames = ["Your choice", "Computer's choice", "Result", "Current score"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for line in lines:
            value = line.split("'") #split a string into an array containing each word as an element
            writer.writerow({"Your choice": value[1], "Computer's choice": value[4], "Result": value[6], "Current score": value[8]})
            
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
        
        message = f"Your choice: '{user_choice}'; Computer's choice: '{computer_choice}'; Result:'{result}'; Current score '{score}'"
        logging.info(message)

        print(message)

        if result == "lose":
            break
    else:
        print(f"what you typed is not a valid answer")



if score == 3:
    print('you won')
else:
    print('you lose. game over...')

printScores()