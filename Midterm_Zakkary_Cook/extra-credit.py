'''
Write a program that predicts the approximate size of a population of
organisms. The application should use text boxes to allow the user to enter
the starting number of organisms, the average daily population increase
(as a percentage), and the number of days the organisms will be left to
multiply.

Starting number of organisms: 2
Average daily increase: 30%
Number of days to multiply: 10
'''

organisms = -1
while organisms <= 0:
    organisms = int(input('Starting number of organisms: '))

average = -1.0
while average <= 0:
    average = float(input('Average daily increase: '))
    if average >= 1:
        average = float(average) / 100

nbr_days = -1
while nbr_days <= 0:
    nbr_days = int(input('Number of days to multiply: '))

print('Day\tApproximate Population')
print('----------------------------------')
for d in range(1, nbr_days+1):
    print(f'{d}\t{organisms}')
    organisms = organisms + (organisms * average)
