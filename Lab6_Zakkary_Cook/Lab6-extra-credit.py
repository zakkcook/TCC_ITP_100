

def main():
    file = 'my_page.html'
    name = input('Enter your name: ')
    description = input('Describe yourself: ')

    if name == "":
        name = 'Cesar Barbieri'

    if description == "":
        description = 'Happy :)'

    with open(file, 'w') as f:
        f.write('\n')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('    <center>\n')
        f.write(f'        <h1>{name}</h1>\n')
        f.write('    </center>\n')
        f.write('    <hr />\n')
        f.write(f'    {description}\n')
        f.write('    <hr />\n')
        f.write('</body>\n')
        f.write('</html>\n')

    f.close()


if __name__ == '__main__':
    main()
