import random

# Define a function to roll a dice
def dice_roll():
    return random.randint(1,6)

# Counting total starting from 0
x = 0

# Counting the number of attempts
count = 0

# Infinite loop until user decides to quit
while True:
    user = input("Do you want to roll (y/n): ").lower()
    if user == "y":
        roll = dice_roll()
        # Counting 1 per turn
        count += 1
        # Adding the result to the total (x)
        x += roll
        # CLI feedback
        print(f"The number on the dice is {roll}")
        print(f"The total amount is {x}")

        # Re-rolling if the total exceeds 36
        if x > 36:
            x -= roll
            print("Oops! You went over 36, try again.")
        
        # Winning condition
        elif x == 36:
            print(f"HOORAY! You won in {count} tries.")
            break
    # Quitting on user's demand (q)
    elif user == "n":
        print("Quitting...")
        break
    # Handling some user induced errors
    else:
        print("The input has to be y/n.")
