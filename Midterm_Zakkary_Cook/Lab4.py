'''
Write a program with a loop that asks the user to enter a series of
positive numbers. The user should enter a negative number to signal the end
of the series. After all the positive numbers have been entered, the
program should display their sum.
'''


def main():
    total = 0.00
    number = 0.00
    output = []

    # User inputs a list of positive numbers
    while number >= 0.00:
        total = total + number
        number = float(input('Enter a positive number (negative to quit): '))
        if number == 0.00:
            print('Zero is not a positive number. Try again!')
        elif number < 0.00:
            break
        else:
            output.append(str(f'{number:,.1f}'))

    print(f'Total = {total:,.2f}')
    myString = buildTextString(output)
    writeToFile('data.txt', myString)


def buildTextString(stringList):
    mystring = ''
    total = 0

    # Loop thru list and build string
    for x in range(len(stringList)):
        total += float(stringList[x])
        if x < len(stringList) - 1:
            mystring += f'{stringList[x]} + '
        else:
            mystring += f'{stringList[x]} = {total}'

    return mystring


def writeToFile(file, content):
    with open(file, 'w') as f:
        f.write(content)
    f.close()


if __name__ == "__main__":
    main()
