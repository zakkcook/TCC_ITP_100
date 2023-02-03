'''
a bug collector collects bugs every day for five days. write a program that
keeps a running total of the number of bugs collected during the five days.
the loop should ask for the number of bugs collected each day, and when the
loop is finished, the program should display the total number of bugs collected
'''


def main():
    bugsCollected = 0

    for count in range(1, 6):
        todaysBugs = int(input('Enter the number of bugs collected today: '))
        bugsCollected += todaysBugs

    print(f'Total bugs collected: {bugsCollected}')


if __name__ == '__main__':
    main()
