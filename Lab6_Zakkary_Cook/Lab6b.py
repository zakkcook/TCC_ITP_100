import random


def main():

    file = input('Enter the name of the file to which results should be written: ')
    numberTimes = input('Enter the number of random numbers to be written to the file: ')
    numberCount = 0

    if not file:
        file = "random_numbers.txt"
    if not numberTimes:
        numberCount = 100
    else:
        numberCount = int(numberTimes)

    with open(file, 'w') as f:
        for r in range(0, numberCount):
            number = random.randint(0, 999)
            f.write(str(number) + '\n')
    f.close()


if __name__ == '__main__':
    main()