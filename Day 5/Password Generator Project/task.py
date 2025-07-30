import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

selected_letters = selected_symbols = selected_numbers = []
if  nr_letters>0:
    selected_letters = random.sample(letters, k=nr_letters)
if  nr_symbols>0:
    selected_symbols = random.sample(symbols, k=nr_symbols)
if  nr_numbers>0:
    selected_numbers = random.sample(numbers, k=nr_numbers)

#Easy version
print(f"Your easy password is: {"".join(selected_letters)}{"".join(selected_symbols)}{"".join(selected_numbers)}" )

#Hard version
combined_password = selected_letters + selected_symbols + selected_numbers
perfect_password = random.sample(combined_password, k=len(combined_password))
print(f"Your perfect password is: {"".join(perfect_password)}")