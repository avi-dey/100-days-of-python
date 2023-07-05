from art import logo, vs
from random import choice
from game_data import data
import os
import copy

score = 0
game_over = False

# display art
print(logo)

# generate a random account from the game data and remove that dict from the list (remove locally, thus deepcopy is used)
instagram_data = copy.deepcopy(data)
account_b = choice(instagram_data) 
instagram_data.remove(account_b) # remove the dict entry from list

## get score (repetitive thus a function is made)
def check_guess(guess: str, a_followers: int, b_followers: int)-> str:
    # if guess == "a":
    #     return a_followers > b_followers
    # else: # guess is b
    #     return b_followers > a_followers
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# format the data into printable format (repetitive)
def print_formatted(account: dict)-> str :
    """takes in dict and returns a formatted string"""   
    name = account["name"]
    country = account["country"]
    desc = account["description"]
    follower_reveal = account["follower_count"] # to test code
    return f"{name}, a {desc} from {country}. \nREVEAL:{follower_reveal}"


# make the game repeatable
while not game_over :
    # make the account B turn into account A for the next round (irrespective of who has more followers)
    account_a = account_b
    account_b = choice(instagram_data)
    instagram_data.remove(account_b)

    # ask for a guess
    print("compare A:", print_formatted(account_a))
    print(vs)
    print("against B:", print_formatted(account_b))

    # check if the user is correct
    ## get the scores of each account
    guess = input("guess whether A or B has more followers: ").lower().strip()
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    print(check_guess(guess, a_followers, b_followers)) # testing purpose

    # clear the screen after each round
    # os.system("cls")

    # give user feedback on their game
    if check_guess(guess, a_followers, b_followers):
        score += 1
        print(f"You have guessed it right. current score is {score} ")
    else:
        game_over = True
        print(f"wrong guess. final score is {score} ")