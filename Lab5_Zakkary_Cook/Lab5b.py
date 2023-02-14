
# prompts the user to enter two integer values
firstNumber = int(input("Enter number 1: "))
secondNumber = int(input("Enter number 2: "))


# a function named max that accepts two integer values as arguments
# and returns the value that is the greater of the two.
def max(firstNumber, secondNumber):
    if firstNumber > secondNumber:
        return firstNumber
    else:
        return secondNumber


# get max value
maxValue = max(firstNumber, secondNumber)

# display the value that is the greater of the two.
print(f"The maximum number is {maxValue}")
