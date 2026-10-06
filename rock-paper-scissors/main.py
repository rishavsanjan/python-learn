import random

print("=== Play rock paper scissors with your computer ===")
print("=== First one with 5 points wins the game ===")



def game():
    playerWins = 0
    computerWins = 0

    while playerWins < 5 and computerWins < 5:
        if playerWins == 5:
            print("You won the game!")
            break 
        elif computerWins == 5:
            print("Computer won the game!")
            break

        options = ['rock', 'scissors', 'paper']
        computerChoice = random.choice(options)

        print("Choose one of the followings: ")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print()

        try:
            playerChoice = int(input("Enter your choice : "))
        except ValueError:
             print("Invalid input!")
             continue

        if playerChoice > 3 or  playerChoice < 1:
            print("Invalid input!")
            continue
             
        if playerChoice == 1 and computerChoice == "rock" or playerChoice == 2 and computerChoice == "paper" or playerChoice == 3 and computerChoice == "scissors":
            print("Draw")
        elif playerChoice == 1 and computerChoice == "paper" or playerChoice == 2 and computerChoice == "scissors" or playerChoice == 3 and computerChoice == "rock":
            print("Computer Wins")
            computerWins += 1
        elif playerChoice == 1 and computerChoice == "scissors" or playerChoice == 2 and computerChoice == "rock" or playerChoice == 3 and computerChoice == "paper":
            print("You Win")
            playerWins += 1

        print("Computer choose : ",  computerChoice)
        print("Score : ", playerWins, "-", computerWins)


while True: 
    game()

    playAgain = input("Do you want to play again? (y/n)")

    if playAgain == "n":
         print("Goodbye homie")
         break


