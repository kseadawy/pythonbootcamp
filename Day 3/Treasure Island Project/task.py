print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()
if direction == "left":
    choice2 = input('You\'re at a lake, what do you want to do? '
                      'Type "Swim" or "Wait".\n').lower()
    if  choice2 == "wait":
        door = input('You\'re at the doors and near to the treagure, what do you want to choose? '
                      'Type "Red" or "Blue" or "Yellow".\n').lower()
        if door == "yellow":
            print("You Win!")
        elif door == "red":
            print("Burned by fire.Game Over.")
        elif door == "blue":
            print("Eaten by beasts.Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("Fall into a hole.Game Over.")