import random

import art

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

is_game_over = False
while not is_game_over:

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempt = 10
    else:
        attempt = 5

    guessed_num = random.randrange(1,101)
    is_guessed = False
    for itr in range(attempt):
        print(f"You have {attempt} attempts to guess the number")
        your_guess_num = int(input("Make a guess: "))
        if your_guess_num == guessed_num:
            is_guessed = True
            break
        elif your_guess_num > guessed_num:
            print("Too high")
        else:
            print("Too Low")
        attempt-=1
    if is_guessed:
        print("You Win!")
    else:
        print("You Lose!")

    if input("Do you want to play again y for, n for n") != 'y':
        is_game_over = True