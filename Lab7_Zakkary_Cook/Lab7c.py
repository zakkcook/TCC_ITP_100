'''
In a program, write a function that accepts two arguments: a list, and a
number n. Assume that the lists contains numbers. The function should display
all of the numbers in the list that are greater than the number n.
'''


def main():

    listofnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 5

    new_list = print_numbers_greater_than(n, listofnumbers)
    print('List of numbers:')
    print(listofnumbers)
    print(f'List of numbers that are greater than {n}:')
    print(new_list)


def print_numbers_greater_than(min_number, listofnumbers):
    my_new_list = []
    for number in listofnumbers:
        if number > min_number:
            my_new_list.append(number)
    return my_new_list


if __name__ == "__main__":
    main()
