alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# converts string to list
def convert_str_to_list(string : str) -> list:
    lst = []
    for i in range(len(string)):
        lst.append(string[i])
    return lst

# modifies the message in-place
def encoder(message: list, shift: int = 0)-> list:
    for i in range(len(message)):
        if message[i] in alphabets:
            idx_of_alphabet = alphabets.index(message[i]) # can you write this in a more simple manner?
            pos = (idx_of_alphabet + shift) % 26
            message[i] = alphabets[pos]
    return message

# modifies the message in-place
def decoder(message: list, shift: int = 0)-> list:
    for i in range(len(message)):
        if message[i] in alphabets:
            idx_of_alphabet = alphabets.index(message[i]) # can you write this in a more simple manner?
            pos = (idx_of_alphabet - shift) % 26 # (0 - 2) % 26 = 24
            message[i] = alphabets[pos]
    return message

# checking 
# shift = 2
# print(f"pffft, the encoded text is {encoder(lst, shift)}")
# print(lst)
# print(f"pffft, the decoded text is {decoder(lst, shift)}")
# print(lst)

user_rerun_choice = True

while user_rerun_choice:
    print("Type 'encode' to encrypt, type 'decode' to decrypt:")
    cipher_type = input(">").lower()
    while cipher_type != "encode" and cipher_type != "decode":
        cipher_type = input("Invalid input!!! Please type chose 'encode' or 'decode' : ").lower()
    
    msg = input(f"Please enter the text you want to {cipher_type}: ")
    shift = int(input("Type the shift number:"))

    # conversion to list
    msg_list = convert_str_to_list(msg)
    
    # encoding and decoding
    if cipher_type == "encode":
        encoded_msg_lst = encoder(msg_list, shift)
        encoded_msg = "".join(encoded_msg_lst) # converting back to string
        print(f"Here's the encoded result : {encoded_msg}")
        # user_wish = False
    else:
        decoded_msg_lst = decoder(msg_list, shift)
        decoded_msg = "".join(decoded_msg_lst)
        print(f"Here's the decoded result : {decoded_msg}")
        # user_wish = False
    
    user_rerun_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if user_rerun_input != "yes" and user_rerun_input != "no":
        user_rerun_input = input("Invalid input!! Please reply with 'yes' or 'no'").lower()
    
    # updating user_rerun_choice 
    if user_rerun_input == "yes":
        user_rerun_choice = True
    else:
        user_rerun_choice = False