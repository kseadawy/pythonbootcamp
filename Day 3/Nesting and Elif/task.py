print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = float(input("Enter your age: "))
    if  age <= 12:
        print("You have to pay $5")
    elif age >12 and age < 18:
        print("you have to pay $7")
    else:
        print("you have to pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
