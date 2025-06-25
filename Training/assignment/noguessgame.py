"""
Date: 22-6-2025
Author: Subrato
Desc: for in -> Number guessing game
"""

import random

#Generate a number between 1 and 10

secret_number = random.randint(1,10)

print('Guess no . between 1 and 10')

#loop until user guess the correct number
while True:
    try:
        guess = int(input('Enter your guess: '))

        if guess<1 or guess>10:
            print("Please guess number between 1 and 10")
            continue

        if guess < secret_number:
            print('Low! try again')
        elif guess >secret_number:
            print('High! try again')

        else:
            print('Congratulations! you are correct')
            break

    except ValueError:
        print("Invalid input. Please enter number.")

    else:
        print('Well Played')

    finally:
        print("Let's try again")


