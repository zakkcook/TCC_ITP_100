'''
in mathematics, the notation n! represents the factorial of the nonnegative
integer n. the factorial of n is the product of all the nonnegative integers
from 1 to n. for example, 7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5,040 and
4! = 1 x 2 x 3 x 4 = 24. write a program that lets the user enter a nonnegative
integer then uses a loop to calculate the factorial of that number.
display the factorial.
'''


def main():
    x = 0
    while x < 1:
        x = int(input('Enter a positive integer: '))
    y = factorial2(x)
    print(f'The factorial of {x} is {y}')


def factorial(n):
    result = 1
    for item in range(1, n+1):
        result = result * (item)
    return result


def factorial2(n):
    if n == 1:
        return n
    else:
        return n * factorial2(n-1)


if __name__ == "__main__":
    main()
