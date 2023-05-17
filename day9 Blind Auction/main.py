from art import logo
# this list will have dict enteries with two keys: name and bid
auction = []
is_bidding_over = False

print(logo)
print("The bidding starts now: ")

## bidding loop
while not is_bidding_over:
    bidder = {}
    bidder["name"] = input("What is your name? : ")
    bidder["bid"] = int(input("What is your bid? $"))

    auction.append(bidder) # adding to list in order to compare bids in future

    print("Are there any other bidders? Type 'yes or 'no' ")
    more_bidders = input("> ")
    while more_bidders != "yes" and more_bidders != "no":
        more_bidders = input("Invalid Input!!! Type 'yes' or 'no' : ")
    
    if more_bidders == "no":
        is_bidding_over = True

## who has the max bid
max_bid = auction[0]["bid"]
max_bidder = auction[0]["name"]

for i in range(1, len(auction)):
    if auction[i]["bid"] > auction[i-1]["bid"]:
        max_bid = auction[i]["bid"]
        max_bidder = auction[i]["name"]

print()
print(f"max bid is {max_bid} by {max_bidder}")
print()
print(auction)