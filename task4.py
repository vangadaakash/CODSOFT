import random
while True:
    user=input("Enter a choice (rock, paper, scissors): ")
    options=["rock", "paper", "scissors"]
    computer=random.choice(options)
    print(f"\nYou choose {user},computer choose {computer}.\n")
    if user==computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user=="rock":
        if computer=="scissors":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
    elif user=="paper":
        if computer=="rock":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beat paper! You lose.")
    elif user=="scissors":
        if computer=="paper":
            print("Scissors beat paper! You win!")
        else:
            print("Rock beats scissors! You lose.")
            
    play_again = input("Do you want to play another round? (y/n): ")
    if play_again.lower()!="y":
        break
