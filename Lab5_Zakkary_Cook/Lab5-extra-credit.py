import random


def main():
    userChoice = 0
    computerChoice = 0
    while userChoice == computerChoice:
        userChoice = int(input('Enter 1 for rock, 2 for paper, 3 for scissors: '))
        computerChoice = random.randint(1, 3)
        handleChoice(userChoice, computerChoice)


def handleChoice(userChoice, computerChoice):
    computerWon = isComputerWinner(userChoice, computerChoice)

    if computerChoice == 1:
        print('Computer chose rock')
    if computerChoice == 2:
        print('Computer chose paper')
    if computerChoice == 3:
        print('Computer chose scissors')

    if userChoice == 1:
        print('You chose rock')
    if userChoice == 2:
        print('You chose paper')
    if userChoice == 3:
        print('You chose scissors')

    if userChoice == computerChoice:
        print('You made the same choice as the computer. Starting over')
    elif computerWon is True:
        print('The computer wins the game')
    else:
        print('You win the game')


def isComputerWinner(userChoice, computerChoice):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    computerWins = False

    if computerChoice == ROCK and userChoice == SCISSORS:
        computerWins = True
    elif computerChoice == PAPER and userChoice == ROCK:
        computerWins = True
    elif computerChoice == SCISSORS and userChoice == PAPER:
        computerWins = True

    return computerWins


if __name__ == "__main__":
    main()
