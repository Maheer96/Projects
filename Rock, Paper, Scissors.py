# Rock Paper Scissors Mini Project
import random
import time

# Importing two useful modules used to both create the program and allow for functionality + correctness

while True:
    possible_options = ['rock', 'paper', 'scissors']
    user_choice = input("Enter a choice (rock, paper, or scissors): ")
    computer_choice = random.choice(possible_options)
    separator = "-"*40

# While loop used to offer an option to replay the game
# Establish a list for the computer to randomly select from
# Allow the user to enter their choice amongst rock, paper, and scissors
# Create a separation variable for visuals of code output
    print(f"\nYou chose {user_choice}, the computer chose {computer_choice}! \n"+separator)
    time.sleep(1)

# Creating a delay between displaying the choices and the verdict to allow for a more realistic feel

    if user_choice == computer_choice:
        print(f"Both players chose {user_choice}, it's a tie!\n")

    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print("Rock beats scissors, you've won! \U0001F604\n") # End code represents emojis
        else:
            print("Paper crushes rock, computer wins! \U0001F641\n")

    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print("Paper crushes rock, you've won! \U0001F604\n")
        else:
            print("Scissors slices paper, computer wins! \U0001F641\n")

    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print("Scissors slices paper, you've won! \U0001F604\n")
        else:
            print("Rock beats scissors, computer wins! \U0001F641\n")

    else:
        print("Unfortunately that combination does not work! Please enter a valid input.\n")

    time.sleep(1)

# Use of several conditional statements to cover the potential outcomes of the game
# Final else statement to ensure user enters appropriate input

    play_again = input("Would you like to play again? (y/n): \n")
    if play_again != 'y':
        print("Thank you for playing.")
        break
