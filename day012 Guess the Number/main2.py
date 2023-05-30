# main.py I didn't use any functions
# main2.py with functions

# functionality
# 1. guess high or low
# 2. assign difficulty
# 3. game

from art import logo, success
import os
import random

## constants defined globally : 
EASY_LEVEL_ATTEMPTS = 10 # easy level
HARD_LEVEL_ATTEMPTS = 5 # hard level

def check_ans(number: int, guess: int)-> int:
    if guess == number:
        print(success)
        print(f"Correct Guess!!! Hurray! The number was {number}")
        return 0 # correct guess return 0
    elif guess < number:
        print("Too Low, Guess Again")
    else:
        print("Too High, Guess Again")
    return 1

def assign_difficulty():
    difficulty = input("Choose difficulty: 1. Easy\n2. Hard\n")
    if difficulty == "1":
        return EASY_LEVEL_ATTEMPTS
    return HARD_LEVEL_ATTEMPTS

def game():
    print(logo)
    number = random.randint(1,100)
    print(f"pfft, the answer is {number}")
    attempts = assign_difficulty()
    print(f"you are starting with {attempts} attempts")

    while attempts:
        guess = int(input("Make a guess: "))
        right_or_wrong_guess = check_ans(number, guess)
        
        if right_or_wrong_guess == 0:
            break

        attempts -= 1
        print(f"You have {attempts} left")

    if not attempts: # if attempts == 0
        print("Oops! You have finished all your attempts")

game()