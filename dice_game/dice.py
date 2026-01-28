import random

def dice_roll():
    return random.randint(1,6)

x = 0
count = 0

while True:
    user = input("Do you want to roll (y/n): ").lower()
    if user == "y":
        roll = dice_roll()
        count += 1
        x += roll
        print(f"The number on the dice is {roll}")
        print(f"The total amount is {x}")
        if x > 36:
            x -= roll
            print("Oops! You went over 36, try again.")
        elif x == 36:
            print(f"HOORAY! You won in {count} tries.")
            break
    elif user == "n":
        print("Quitting...")
        break
    else:
        print("The input has to be y/n.")
