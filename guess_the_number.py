import random as r

number = r.randint(1, 30)

print("Welcome to the Number Guesser Game!!!\n")
print("I am thinking of a number between 1 and 30. You have 3 attempts to guess it correctly.\n")

attempts = 3

while attempts != 0:

    user_guess = int(input(f"Your guess: "))
    
    if user_guess == number:
        print(f"Perfecto! You win! The number was indeed {number}.")
        break

    elif user_guess > number:
        print("Nope, too high!", end=" ")
        if attempts != 1:
            print("Guess lower\n")

    elif user_guess < number :
        print("Nope, too low!", end=" ")
        if attempts != 1:
            print("Guess higher\n")

    attempts -= 1

    if attempts == 0:
        print(f"\nSorry, unfortunately you LOST! The number was {number}.")
        break
