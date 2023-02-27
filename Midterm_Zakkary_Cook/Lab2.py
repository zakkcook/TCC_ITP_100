'''
Use the flowchart to create a program that leads a person through the
steps of fixing a bad Wi-Fi connection.
'''


def main():

    # put troubleshooting steps into a list
    troubleshooting_steps = [
        'Reboot the computer and try to connect.',
        'Reboot the router and try to connect.',
        'Make sure the cables between the router and modem are plugged in '
        'firmly.',
        'Move the router to a new location and try to connect.']

    # loop thru steps
    for step in troubleshooting_steps:
        print(step)

        # Ask if its fixed
        isFixed = False
        isFixed = is_problem_fixed()

        # if yes terminate
        if isFixed is True:
            break

    # print success message
    if isFixed is True:
        print('Glad to be of help.')
    else:
        print('Get a new router.')


def is_problem_fixed():
    answer = ''
    while answer != 'YES' and answer != 'NO':
        answer = input('Did that fix the problem? ')
        answer = answer.upper()

    if answer == 'YES':
        return True
    else:
        return False


if __name__ == "__main__":
    main()
