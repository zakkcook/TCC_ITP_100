def main():
    year = int(input('Enter the year: '))

    if (year % 400) == 0:
        print('That is a leap year. February has 29 days.')
    elif (year % 100) != 0 and (year % 4) == 0:
        print('That is a leap year. February has 29 days.')
    else:
        print('That is not a leap year. February has 28 days.')

if __name__ == "__main__":
    main()