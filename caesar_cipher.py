import os
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(msg,shift,direction):
    new_msg = ""
    shift = shift % len(alphabet)
    if direction == 'decode':
        shift *= -1
    for l in msg:
        if l in alphabet:
            index = alphabet.index(l) + shift
            new_msg += alphabet[index]
        else:
            new_msg += l
    return new_msg

while True:
    os.system('cls||clear') 
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(f"The {direction}d message is:\n{caesar(text,shift,direction)}")

    again = input("Would you like to continue? Y or N\n").lower()

    if again != 'y':
        print("Goodbye!")
        break