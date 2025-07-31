alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#  Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

#  Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

def encrypt(original_text, shift_number):
    ciphered_text = ""
    for letter in original_text:
        ciphered_letter_index = alphabet.index(letter) + shift_number
        if  ciphered_letter_index >= len(alphabet):
            ciphered_letter_index -= len(alphabet)
        ciphered_text += alphabet[ciphered_letter_index]
    print(ciphered_text)
# What happens if you try to shift z forwards by 9? Can you fix the code?
#Fixed by adding a condition
# Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(text, shift)