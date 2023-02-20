def main():
    file = 'random_numbers.txt'
    with open(file, 'r') as f:
        count = 0
        total = 0
        contents = f.readlines()
        for c in contents:
            total += int(c.strip())
            count += 1
        print(f'Total: {total:,}\n{count} numbers were read from the file.')


if __name__ == '__main__':
    main()
