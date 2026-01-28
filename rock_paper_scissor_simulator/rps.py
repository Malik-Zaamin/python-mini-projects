import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")


    print(f"Player 1: {player}")
    print(f"Computer: {computer}")

    if player == "rock" and computer == "scissors":
        print("You won!")
    elif player == "scissors" and computer == "paper":
        print("You won!")
    elif player == "paper" and computer == "rock":
        print("You won")
    elif player == computer:
        print("You drew")
    else:
        print("You lost")

    print("GAME OVER")

    play_again = input("Play again (y/n): ").lower()
    if play_again == "n":
        running = False

print("Thanks for playing")