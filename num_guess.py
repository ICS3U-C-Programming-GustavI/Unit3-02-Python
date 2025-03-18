#!/usr/bin/env python3
# Created by: Gustav I
# Created on: March 18, 2025
# This program executes a number guessing game.

import random  # Import the random module


def main():
    # Get user's guess
    number_guess = int(input("Guess a number (0-9): "))
    print("")

    # Computer chooses a random number
    chosen_number = random.randint(0, 9)  # Use random.randint()

    # Check if the number is right or wrong
    if number_guess == chosen_number:
        print("You got the right number!")
    if number_guess != chosen_number:
        print(
            "You did not get the right number. The correct number was:", chosen_number
        )


if __name__ == "__main__":
    main()
