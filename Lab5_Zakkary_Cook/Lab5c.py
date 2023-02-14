















































'''
# Import random
import random


def is_even(number):
    # Determine whether the number is even.
    if (number % 2) == 0:
        return True
    else:
        return False


# Main function.
def main():
    # The count for even numbers starts at 0.
    even = 0
    # The count for odd numbers starts at 0.
    odd = 0
    # Specify the range for the random numbers.
    for count in range(100):
        # Get a random number.
        number = random.randint(1, 100)
        # Display the number.

        # Set up the counter for the even and odd numbers)
        if (is_even(number)):
            even += 1
        else:
            odd += 1

    # Print how many even numbers there are.
    print(f' Out of 100 random numbers, {odd} were odd, and {even} were even.')


# Call the main function.
main()
'''
