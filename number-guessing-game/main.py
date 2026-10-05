import random

def game():
    print("=== Number Guessing Game ===")
    print("Guess the number between 1 and 100")

    number = random.randint(1, 100)
    attempts = 0

    maxAttempts = 7

    while True:

        if attempts >= maxAttempts:
            print("Game over!")
            print("The actual number was :", number)
            break

        try:
            guess = int(input("Enter your guess : "))
        except ValueError:
            print("Enter a valid integar value.")
            continue

        attempts += 1

        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
        else:
            print("Bullseye!")
            print("You guessed it in ", attempts, " attemps")
            break

while True:
    game()

    ans = input("Do you want to play again? (y/n) : ")

    if ans == "y":
        continue
    else:
        print("Thanks for playing!")
        break



    