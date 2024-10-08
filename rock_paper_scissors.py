import random as r

print("Welcome to rock, paper, scissors game")
print("\nYou will play against the computer")
print("\nThe first to reach 3 points wins\n")

universal_options = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while 1:

    #Get the user's and computer's choice
    user_choice = input("Enter rock, paper, or scissors.\nYour choice: ").lower()
    computer_choice = r.choice(universal_options)

    if user_choice == computer_choice:
        print("\nIt's a tie\n")

    elif user_choice == "rock" and computer_choice == "scissors" or \
         user_choice == "scissors" and computer_choice == "paper" or \
         user_choice == "paper" and computer_choice == "rock":
         user_score += 1
         print(f"\nUser choses {user_choice} and computer choses {computer_choice}.")
    else:
        computer_score += 1
        print(f"\nComputer choses {computer_choice} and user choses {user_choice}.")

    print(f"Computer score: {computer_score} User: {user_score}\n")

    if user_score == 3:
        print("You win! Yee ho!")
        break
    elif computer_score == 3:
        print("Computer wins!")
        break

