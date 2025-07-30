import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

userChoice = int(input("What do you choose?  0 for Rock, 1 for Paper, 2 for Scissors\n"))
computerChoice = random.randint(0, 2)
gameChoices = [rock, paper, scissors]
gameChoicesNames = ['Rock', 'Paper', 'Scissors']

if  userChoice < 0 or userChoice > 2:
    print("Invalid Choice, Game Over!!!")
else:
    print(gameChoices[userChoice])
    print(f"Computer Chose: {computerChoice}\n"+gameChoices[computerChoice])
    print(f"Your choice {gameChoicesNames[userChoice]}, Computer choice {gameChoicesNames[computerChoice]}")
    if userChoice == 0 and computerChoice == 2:
        print("You Win!")
    elif computerChoice == 0 and userChoice == 2:
        print("You Lose!")
    elif userChoice > computerChoice:
        print("You Win!")
    elif userChoice == computerChoice:
        print("It's a draw!")
    else:
        print("You Lose!")
