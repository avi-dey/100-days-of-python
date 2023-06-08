# Angela's code didn't appeal me, I couldn't make sense out of it. A lot of the key functionaliy were ignored in order to simply the project
# source : https://youtu.be/mpL0Y01v6tY (channel name: Code Coash)

## Game Terminologies:
# bust: tatal sum of hand is above 21
# hit: draw one more card
# stand: don't need any more cards
# in a real game there can be multiple players and one dealer, in this program there is only one player and one dealer(i.e. computer)
# play the game at: https://games.washingtonpost.com/games/blackjack

## approach (thinking):
# 1. four deck of cards
# 2. deal the cards -- fn
# 3. calculate score -- fn
# 4. check for winner -- fn
# 5. game loop

import random

# 1
deck = [ "A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "K", "Q", "A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "K", "Q", "A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "K", "Q", "A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "K", "Q"]
player_hand = []
dealer_hand = [] # computer is the dealer

player_in = True # player wants to draw more cards
dealer_in = True # dealer ,, 

# 2
def deal_card(hand: list) -> None:
    """appends a card to player or dealer"""
    card = random.choice(deck)
    # remove the card from the deck, once it is taken out
    hand.append(card)
    deck.remove(card)

# 3
# do check youtube_comment.txt which was given under the video
def calculate_total(hand: list) -> int:
    total = 0
    face_cards = ["J", "K", "Q"]
    for card in hand:
        if card in range(2,10):
            total += card
        elif card in face_cards:
            total += 10 # "J", "K" or "Q"
        # only the case of "A" is left
        # "A" can have 2 values 1 or 11, 11 if total sum is <= 21 and 1 if total sum is > 21
        else: # else clause will only be executed when the card is an "A"
            if total < 11:
                total += 11
            else:
                total += 1
    return total

# 4
def reveal_dealer_hand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2: ### DOUBT, why revealing only 2, there could be cases where we have to reveal 3 or 4 or 5......
        return dealer_hand[0], dealer_hand[1] # returns a tuple
    

# 5
# both player and dealer gets 2 cards at the start of the game
for _ in range(2):
    deal_card(dealer_hand)
    deal_card(player_hand)

while player_in or dealer_in:
    print(f"Dealer has {reveal_dealer_hand()} and X") 
    print(f"Your hand is {player_hand} and total score {calculate_total(player_hand)}")
    
    # player decision
    if player_in:
        stand_or_hit = input("1: Stand\n2: Hit\n")
    if stand_or_hit == "1": # input() returns a str
        player_in = False
    else:
        deal_card(player_hand)
    
    # dealer decision
    # 16 is a safe score for dealer
    if calculate_total(dealer_hand) > 16:
        dealer_in = False
    else:
        deal_card(dealer_hand)

    # anyone of player or dealer busts or both busts:
    if calculate_total(player_hand) or calculate_total(dealer_hand) > 21:
        break


# if both has 21 then dealer wins, follow the odrer of the statements
if calculate_total(dealer_hand) == 21:
    print(f"Your hand is {player_hand} w total of {calculate_total(player_hand)}\nDealer hand is {dealer_hand} w total of {calculate_total(dealer_hand)}")
    print("BlackJack!!! Dealer wins!")
elif calculate_total(player_hand) == 21:
    print(f"Your hand is {player_hand} w total of {calculate_total(player_hand)}\nDealer hand is {dealer_hand} w total of {calculate_total(dealer_hand)}")
    print("BlackJack!!! You win!")
elif calculate_total(player_hand) < 21 and calculate_total(dealer_hand) > 21:
    print(f"Your hand is {player_hand} w total of {calculate_total(player_hand)}\nDealer hand is {dealer_hand} w total of {calculate_total(dealer_hand)}")
    print("BlackJack!!! You win!")
elif calculate_total(player_hand) > 21 and calculate_total(dealer_hand) < 21:
    print(f"Your hand is {player_hand} w total of {calculate_total(player_hand)}\nDealer hand is {dealer_hand} w total of {calculate_total(dealer_hand)}")
    print("BlackJack!!! Dealer wins!")
# only the case where both above 21 and both below 21 is left, for such case winner will be the one who is nearer to 21
elif 21 - calculate_total(player_hand) < 21 - calculate_total(dealer_hand):
    print(f"Your hand is {player_hand} w total of {calculate_total(player_hand)}\nDealer hand is {dealer_hand} w total of {calculate_total(dealer_hand)}")
    print("BlackJack!!! You win!")
elif 21 - calculate_total(player_hand) > 21 - calculate_total(dealer_hand):
    print(f"Your hand is {player_hand} w total of {calculate_total(player_hand)}\nDealer hand is {dealer_hand} w total of {calculate_total(dealer_hand)}")
    print("BlackJack!!! Dealer wins!")
    