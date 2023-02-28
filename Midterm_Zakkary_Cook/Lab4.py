'''
Write a program with a loop that asks the user to enter a series of
positive numbers. The user should enter a negative number to signal the end
of the series. After all the positive numbers have been entered, the
program should display their sum.
'''


def main():

    total = 0.00
    number = float(input('Enter a positive number (negative to quit): '))
    while number >= 0:
        number = float(input('Enter a positive number (negative to quit): '))
        total = total + number
    print('Total = ', total)


if __name__ == "__main__":
    main()












'''
    number = ''
    while number >= 0:
        number = float(input("Enter a positive number (negative to quit): "))

    if number >= 0:
        return True
    else:
        return False

'''