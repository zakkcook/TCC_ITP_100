'''
Design a program that generates a seven-digit lottery number. The program
should generate seven random numbers, each in a range of 0 through 9, and
assign each number to a list element. Then write another loop that displays the
contents of the list.
'''

import random as r


def main():
    lotto_numbers = []
    result = ""

    # get 7 random numbers
    for x in range(0, 7):
        lotto_numbers.append(r.randint(0, 9))

    # build a string of my numbers with a comma except for the last one
    for x in range(0, len(lotto_numbers)):
        if x < len(lotto_numbers) - 1:
            result += str(lotto_numbers[x]) + ', '
        else:
            result += str(lotto_numbers[x])

    print(result)


if __name__ == "__main__":
    main()