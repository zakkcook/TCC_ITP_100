def main():
    age = int(input('Please enter a persons age: '))
    if age <= 1:
        print('Infant')
    elif age > 1 and age < 13:
        print('Child')
    elif age >= 13 and age < 20:
        print('Teenager')
    elif age >= 20:
        print('Adult')
    else:
        print('Error. Check your input.')

if __name__ == "__main__":
    main()