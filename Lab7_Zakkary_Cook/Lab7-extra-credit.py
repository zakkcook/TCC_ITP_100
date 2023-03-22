'''
In a program you can simulate a magic square using a two-dimensional list.
Write a function that accepts a two-dimensional list as an arguement and
determines whether the list is a Lo Shu Magic Square.

The grid contains the numbers 1 through 9 exactly.
The sum of each row, each column, and each diagonal all add up to the same
number.
'''


def main():
    my_list = get_nine_numbers()
    print_square(my_list)

    isMagicSquare = isLoShuMagicSquare(my_list)
    if isMagicSquare is True:
        print('This is a Lo Shu magic square.')
    else:
        print('This is not a Lo Shu magic square.')


def get_nine_numbers():
    my_2DList = []
    my_list = []

    for row in range(0, 3):
        for number in range(0, 3):
            choice = int(input(f'Enter number for row {row + 1}: '))
            my_list.append(choice)

        my_2DList.append(my_list[:])
        my_list.clear()

    return my_2DList


def print_square(my_2Dlist):
    for list in my_2Dlist:
        row = ''
        for number in list:
            row += f'{number} '
        print(row)


def isLoShuMagicSquare(my_list):
    result = True

    # check rows
    for item in my_list:
        sum = 0

        for number in item:
            sum += number

        if sum != 15:
            result = False
            break

    # check columns
    if result is True:
        for i in range(0, 3):
            sum = 0
            for item in my_list:
                sum += item[i]

            if sum != 15:
                result = False
                break

    return result


if __name__ == "__main__":
    main()
