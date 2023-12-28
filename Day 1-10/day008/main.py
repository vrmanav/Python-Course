# Day 008: Caesar Cipher
from time import sleep
from os import system
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True

def caesar_cipher(cipher_direction, start_text, shift_amount):
    end_text = ""
    #! T0: If direction is decode, then turn shift amount from +ve to -ve 
    if cipher_direction == 'decode':
            shift_amount *= -1
    for char in start_text:
        #! T1: Any char other than in alphabet should be added directly to the end_text
        if char not in alphabet:
             end_text += char
        else:
            #! T2: Find the position of the char
            current_pos = alphabet.index(char)
            #! T3: Add shift to the char's position
            new_position = (current_pos + shift_amount)%26
            #! T4: Find the new char using the list and add it to the final string
            end_text += alphabet[new_position]
    print(f"{cipher_direction.capitalize()}d text is {end_text}")

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(direction, text, shift)
    result = input("Do you want to continue? [YES/NO]\n").lower()
    if result == 'no':
         should_continue = False
         print("\nGOOD-BYE !!")
    sleep(0.5)
    system('clear')