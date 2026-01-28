import random

print("Welcome to the custom number guessing game!")

low = int(input("Enter the lower range: "))
high = int(input("Enter the upper range: "))

print(f"You have 7 chances to guess the number between {low} and {high} \nGood Luck!")

num = random.randint(low,high)
ch = 7
gc = 0

while ch > gc:
    gc += 1
    guess = int(input("what is your guess?: "))

    if guess == num:
        print(f"Congratulations, you got it correct on attempt number {gc}.")
        break
    elif gc >= ch:
        print(f"Sorry the number was {num}. Better luck next time.")
    elif guess > num:
        print("Too High")
    elif guess < num:
        print("Too low")