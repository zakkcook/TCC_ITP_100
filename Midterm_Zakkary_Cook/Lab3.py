'''
Write a program that asks the user for the speed of a vehicle(in MPH)
and the number of hours it has traveled. It should then use a loop to
display the distance the vehicle has traveled for each hour of that
time period. (distance = speed x time)

Hour        Distance Traveled
--------------------------------
1                   40
2                   80
3                  120
'''


def main():

    speed = float(input("Enter the speed of the vehicle in mph: "))
    hours = int(input("Enter the number of hours traveled: "))
    distance = 0

    print('Hour\tDistance Traveled')
    print('-------------------------')
    for hoursTraveled in range(hours):

        distance += speed * 1
        print(f'{hoursTraveled+1}\t{distance:.2f}')


if __name__ == "__main__":
    main()