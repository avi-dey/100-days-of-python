#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# i am doing hard level
# 52 letters randint
# 10 numbers randint
# 9 symbols randint

rand_string = ""

for _ in range(nr_letters):
    # rand_order = random.randint(1,3) # 1 -> letters, 2 -> numbers, 3 -> symbol
    rand_string += random.choice(letters)
for _ in range(nr_numbers):
    rand_string += random.choice(numbers)
for _ in range(nr_symbols):
    rand_string += random.choice(symbols)
print(rand_string)

# EASY LEVEL COMPLETED TIL HERE
# i will make letters+numbers+symbols format (easy then I will randomize it) : this way clone will be cleaner
# NOW HARD LEVEL:

# random.sample() method returns a list of non-duplicate elements from a sequence
# and the len of this list is the 2nd positional argument (mandatory to write)
rand_order_string_list = random.sample(rand_string, len(rand_string)) # sample() method makes a lIST
password = ""
for ele in rand_order_string_list:
    password += ele
print(password)
# HARD LEVEL COMPLETED -- WORKS FINE


# new_rand_str = ""
# total_len = len(rand_string)
# for _ in range(total_len):
#     new_rand_str = random.choice(rand_string)
    # won't work -- duplicate choices 



