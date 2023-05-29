# guess the number game
# easy mode has 10 attempts 
# difficult mode has 5 attempts

from art import logo, success
import os
import random

attempts = 5
number = random. randint(1,100)

print(logo)
print(f"pfft, here is the number {number}")
difficulty = input("1. Easy\n2. Hard\n")

if difficulty == "1":
    attempts = 10 # while, for, if, else doesn't have local block scoping in python(unlike Java and C++)
print(f"You have {attempts} to complete you guess")
guess = int(input("Make your first guess: "))
print("=="*20)

while True:
    print(f"Your guess was {guess}")
    
    # while, for, if, else doesn't have local block scoping in python(unlike Java and C++)
    attempts -= 1
    if attempts == 0:
        print(f"Game Over. You have {attempts} left")
        break

    if guess == number:
        print(success)
        print(f"Correct Guess!!! Hurray! The number was {number}")
        break
    elif guess < number:
        print("Too low")
        print("Guess Again")
    else:
        print("Too high")
        print("Guess Again")
        
    
    print(f"You have {attempts} remaining chances to guess the number")
    guess = int(input("Make a guess: "))
    os.system("cls")