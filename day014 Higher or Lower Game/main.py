## INSTAGRAM FOLLOWERS GUESS GAME: WHETHER AN INSTA ACCOUNT HAS HIGHER OR LOWER INSTA FOLLOWER COUNT

## What did I learn from this ?
# 1. the use of list.index() method
# 2. only functions have local scoping
# 3. anything apart from functions like for, if, else, while doesn't have any local scoping
# 4. (needs some polishing) using "global" keyword for variables defined globally outside of any function. since, functions have local scopping we cannot reassign a global variable, inside a function a local variable is created even if a variable with the same name exits outside

from game_data import data
import art
import random
import os

# compare and check who has more insta followers
def compare(a, b):
    """will only take in followers key"""
    if a >= b:
        return "1"
    else:    
        return "2"

# return formatted string
def formatted_str(account):
    """will take in the dictionaries of insta accounts"""
    name = account["name"]
    followers_count = account["follower_count"]
    country = account["country"]
    desc = account["description"]
    return f"{name} a {desc}, from {country} \n REVEAL: followers {followers_count}"


def comprare_promt(account_a, account_b):
    print("who has more followerrs? ")
    print(f"is it {formatted_str(account_a)}")
    print(art.vs)
    print(f"or is it {formatted_str(account_b)}")


def game():
    print(art.logo)
    game_over = False
    score = 0

    account_a = random.choice(data)
    data.remove(account_a) # removing account_a from out data to: 1.prevent repeatation and 2.comparing one account with itself

    account_b = random.choice(data)

    # game
    while not game_over:
        # if there is no more accounts(dicts) left in game_data(list). then game should end.
        if len(data) == 0:
            print("YOU ARE CHAMPION. ALL GUESSES ARE CORRECT. VICTORY!!!!!!!!!!!") 

        comprare_promt(account_a, account_b)
        guess = input("make a guess? 1 or 2")

        correct_ans = compare(account_a["follower_count"], account_b["follower_count"])
        if correct_ans == guess:
            print(f"you are correct. score : {score}")
            score +=1
        else:
            print(f"you are wrong. score : {score}")
            game_over =True

        account_a = account_b
        account_b = random.choice(data)
        os.system("cls")

    
    print(f"GAME OVER. your total score was : {score}")

game()