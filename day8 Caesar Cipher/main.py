alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

msg = input("Please enter the text you want to encode: ")

# converts string to list
def convert_str(string : str) -> list:
    lst = []
    for i in range(len(string)):
        lst.append(string[i])
    return lst
lst = convert_str(msg)

# returns a list
def encoder(message: list, shift: int = 0)-> list:
    for i in range(len(message)):
        idx_of_alphabet = alphabets.index(message[i]) # can you write this in a more simple manner?
        pos = (shift + idx_of_alphabet) % 26
        message[i] = alphabets[pos]
    return message

# checking 
shift = 2
print(f"pffft, the encoded text is {encoder(lst, shift)}")
