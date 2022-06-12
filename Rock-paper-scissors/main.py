import random

# while loop to play the game several times

while True:
    user_action = input("Enter a choice ( R for rock, P for paper, S for scissors): ")
    possible_actions = ["R", "P", "S"]
    computer_choice = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_choice}.\n")

    if user_action == computer_choice:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_choice == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "P":
        if computer_choice == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "S":
        if computer_choice == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
                    