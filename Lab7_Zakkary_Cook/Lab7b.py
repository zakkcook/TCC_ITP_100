'''
Design a program that asks the user to enter a series of 20 numbers. The
program should store the numbers in a list then display the following data:

The lowest number in the list
The highest number in the list
The total of the numbers in the list
The average of the numbers in the list
'''


def main():
    num_count = 20
    num_list = []

    for x in range(0, num_count):
        num = int(input(f"Enter number {x + 1} of {num_count}: "))
        num_list.append(num)

    low = get_low(num_list)
    high = get_high(num_list)
    total = get_total(num_list)
    average = get_average(num_list)

    print(f'Low: {low:,.1f}')
    print(f'High: {high:,.1f}')
    print(f'Total: {total:,.2f}')
    print(f'Average: {average:,.2f}')


def get_low(num_list):
    num_list.sort()
    return num_list[0]


def get_high(num_list):
    num_list.sort(reverse=True)
    return num_list[0]


def get_total(num_list):
    total = 0
    for x in num_list:
        total += x
    return total


def get_average(num_list):
    total = 0
    item_count = len(num_list)
    for x in num_list:
        total += x
    return total / item_count


if __name__ == "__main__":
    main()
