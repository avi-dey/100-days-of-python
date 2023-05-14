# completed on 13th may 23
import random
import os
from time import sleep
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# game can end in 2 ways: win or lose
# end_of_game = True in both of those conditions
end_of_game = False
lives = 6

# start of the ascii art 
print(logo)
print("="*50)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

# we guess new letters till we lose or win
# while loop terminates if we win or lose 
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # sleep(1) # halt the next line of code for 2 secs
    os.system("cls") # cls for windows, clear for linux/mac

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed \"{guess}\" before")
    
    # update the display
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    

    #Check if user is wrong. -- lose condition
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"Wrong guess: \"{guess}\". It is not in the word\nLives left: {lives}")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters. -- win condition
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # print the ascii art on each iteration of guessing
    print(stages[lives])