from hangman_words import word_list
from random import choice
from hangman_art import *
# generate a random word
word = choice(word_list)
is_game_over = False
lives = 6

# creating the dash version of the word
dashed_word = ""
for _ in range(len(word)):
    dashed_word += "_"

print(logo)
print("current stage of hangman: ")
print(stages[-1])
print("start guessing the word: ")
print("-" * 20)


while not is_game_over:
    guess_letter = input("enter guess letter: ")
    
    # guess out comes: correct guess and wrong guess
    if guess_letter in word:
        for i in range(len(word)):
            if guess_letter == word[i]:
                # dashed_word[i] = guess_letter # 'str' object does not support item assignment
                dashed_word = dashed_word.replace(dashed_word[i], guess_letter)
                guess_letter = ""
                print(f"you guessed the correct letter : now you got {dashed_word} ")
    else: 
        lives -= 1
        if lives == 0:
            print("you have lost the game")
            print(stages[lives])
            is_game_over == True
        print(stages[lives])
        print(f"the guess was incorrect, you have {lives} live(s) left")

    # all the blanks filled
    if word == dashed_word:
        print("HURRAY")
        print("you have won the game")
        is_game_over = True
    