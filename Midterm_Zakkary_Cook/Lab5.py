'''
Write a program that generates a random number in the range of 1 through
100, and asks the user to guess what the number is. If the user's guess
is higher than the random number, the program should display "Too low, try
again." If the user guesses the number, the application should congratulate
the user and generate a new random number so the game can start over.
'''

import random

# will do i appreciate your help. gotta go!
def main():
    secretNumber = createSecretNumber()
    content = guessSecretNumber(secretNumber)
    writeToFile('data5.txt', content)


def createSecretNumber() -> int:
    result = random.randint(1, 100)
    return result


def guessSecretNumber(secretNumber: int):
    result = []
    guess = 1

    while guess > 0 or guess <= 100:
        guess = int(input('Enter a number between 1 and 100, or 0 to quit: '))

        if guess <= 0 or guess > 100:
            print('Thanks for playing!')
            break
        elif guess > secretNumber:
            print('Too high, try again')
            result.append(f'Too high:{guess}\n')
        elif guess < secretNumber:
            print('Too low, try again')
            result.append(f'Too low:{guess}\n')
        else:
            print('Conratulations! You guessed the right number!')
            result.append(f'Correct:{guess}\n')

    # Display results of guess
    return result


def writeToFile(file: str, content):
    with open(file, 'w') as f:
        f.writelines(content)
    f.close()


if __name__ == "__main__":
    main()
