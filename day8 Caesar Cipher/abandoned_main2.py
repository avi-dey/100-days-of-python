# abandoned -- bullshit logic of ord() -- totally dumb
msg = input("Please enter the text you want to encode: ")
shift = 2

# converts string to list
def convert_str(string : str) -> list:
    lst = []
    for i in range(len(string)):
        lst.append(string[i])
    return lst

lst = convert_str(msg)

list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# returns encoded list
# z shift 1 = a (should be circular)
def encoder(message: list, shift: int = 0) -> list:
    for i in range(len(message)):
        letter = message[i]
        if ord(letter) >= 97 and ord(letter) <= 122:
            pos = (ord(letter) + shift) % 26 # to get the circular behaviour
            message[i] = list_of_letters[pos]
    return message

print(encoder(lst, shift))
        
    
