alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(ciphered_text, shift_amount):
    plain_text = ""
    for letter in ciphered_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        plain_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {plain_text}")

def combined_caesar(original_text, shift_amount, dir):
    target_text = ""
    if  dir == "encode":
        shift_amount = shift_amount
    elif dir == "decode":
        shift_amount *= -1
    else:
        print("Invalid direction")
        return
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        target_text += alphabet[shifted_position]
    print(f"Here is the result: {target_text}")

def caesar(original_text, shift_amount, dir):
    if  dir == "encode":
        encrypt(original_text, shift_amount)
    elif dir == "decode":
        decrypt(original_text, shift_amount)
    else:
        print("Invalid direction")

combined_caesar(text, shift, direction)



