# Rock Paper Scissors Game in Python
import random

# User choice and Computer random choice
while True:
    user_action = input("Enter a Choice (rock, paper, scissors): ")
    possible_actions = ['rock', 'paper', 'scissors']
    computer_action = random.choice(possible_actions)
    print(f"\nYou Chose {user_action}, Computer Chose {computer_action}")

# Game Decision
    if user_action == computer_action:
        print(f"Both Selected {user_action}, It's a tie!")
    elif user_action == 'rock':
        if computer_action == 'scissors':
            print("Rock Smashes Scissors, You Win!")
        else:
            print("Paper Covers Rock, You Lose")
    elif user_action == 'paper':
        if computer_action == 'rock':
            print("Paper Covers Rock, You Win!")
        else:
            print("Scissors Cut Paper, You Lose!")
    elif user_action == 'scissors':
        if computer_action == 'paper':
            print("Scissors cut Paper, You Win!")
        else:
            print("Rock Smashes Scissors. You Lose!")
    break
