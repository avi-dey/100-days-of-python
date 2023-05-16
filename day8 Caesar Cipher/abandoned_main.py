# this approach fails at to rotate from z to a for shift of 1

msg = input("Please enter the text you want to encode: ")
shift = 2

# converts string to list
def convert_str(string : str) -> list:
    lst = []
    for i in range(len(string)):
        lst.append(string[i])
    return lst

lst = convert_str(msg)

# returns encoded list
def encoder(message: list) -> list:
    for i in range(len(message)):
        # small a 97 and small z 122 in ascii
        letter = message[i] # for easy redability
        if ord(letter) >= 97 and ord(letter) <=122:
            letter = chr(ord(letter) + shift) # ascii of the letter + shift value
            message[i] = letter # reassigning
    return message

result = encoder(lst)
print(f"test code result : {result}")

# decode the text
def decoder(encoded_msg: list)-> list:
    for i in range(len(encoded_msg)):
        # small a 97 and small z 122 in ascii
        letter = encoded_msg[i] # for easy redability
        if ord(letter) >= 97 and ord(letter) <=122:
            letter = chr(ord(letter) - shift) # ascii of the letter + shift value
            encoded_msg[i] = letter # reassigning
    return encoded_msg

