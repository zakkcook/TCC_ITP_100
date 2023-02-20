def main():
    file = input('Enter the name of the file: ')
    with open(file, 'r') as f:
        count = 1
        contents = f.readlines()
        for c in contents:
            print(f'{count}: ' + c.strip())
            count += 1


if __name__ == '__main__':
    main()
