import sqlite3
from typing import List
import datetime

'''
Students will develop a website with everything they have learned
during the semester. The theme of the project is up to the student.
Your code should use variables, conditions, loops, lists, dictionaries,
objects, GUI, etc. Students will present their project to the class
and explain and answer questions related to the code(5 - 15 minutes).
'''


def main():
    name = ''
    year = int(0)

    while isInvalidName(name):
        name = input('Enter your name: ')

    while isInvalidYear(year):
        year = int(input('Enter your birth year: '))

    # create_sqlite_database()
    movie_list = getMovieList()
    sqlite_insert(movie_list)

    writeHTML(name, year)


def isInvalidName(name: str) -> bool:
    '''If the name contains at least one letter, then its valid'''
    for character in name:
        if character.isalpha():
            return False
    return True


def isInvalidYear(year: int) -> bool:
    '''Checks for valid year. Returns False if invalid.'''
    today = datetime.date.today()
    max_year = today.year
    min_year = 1900
    result = True

    if year == 0:
        print('')
    elif year < min_year:
        print('Please choose a year 1900 or later.')
    elif year > max_year:
        print('Please choose a year on or before ' + str(max_year))
    else:
        age = str(max_year - year)
        print(f'Nice!! You are (or will be) {age} years old this year!!')
        result = False

    return result


def getMovieList():
    data = [
        ('Alice in Wonderland', 2010, 3.4, 'Alice in Wonderland.jpg'),
        ('Back to the Future', 1985, 4.5, 'Back to the Future.jpg'),
        ('Casper', 1995, 3.3, 'Casper.jpg'),
        ('Despicable Me', 2010, 4.0, 'Despicable Me.jpg'),
        ('E.T.', 1982, 3.5, 'ET.jpg'),
        ('Fast and Furious', 2009, 3.7, 'Fast and Furious.jpg'),
        ('Ghostbusters', 1984, 4.2, 'Ghostbusters.jpg'),
        ('Hacksaw Ridge', 2016, 4.3, 'Hacksaw Ridge.jpg'),
        ('Indiana Jones', 2008, 3.3, 'Indiana Jones.jpg'),
        ('Jumanji', 1995, 3.5, 'Jumanji.jpg'),
        ('Kill Bill', 2003, 3.4, 'Kill Bill.jpg'),
        ('Little Nicky', 2000, 3.3, 'Little Nicky.jpg'),
        ('Matrix', 1999, 3.6, 'Matrix.jpg'),
        ('Nacho Libre', 2006, 3.3, 'Nacho Libre.jpg'),
        ('O brother, Where Art Thou', 2000, 4.1, 'OBrotherWhereArtThou.jpg'),
        ('Priest', 2011, 3.2, 'Priest.jpg'),
        ('Quarantine', 2008, 3.0, 'Quarantine.jpg'),
        ('R.I.P.D.', 2013, 3.0, 'RIPD.jpg'),
        ('Scary Movie', 2000, 3.0, 'Scary Movie.jpg'),
        ('Toy Story', 1995, 3.8, 'Toy Story.jpg'),
        ('UP.', 2009, 4.3, 'UP.jpg'),
        ('V For Vendetta', 2005, 4.3, 'V For Vendetta.jpg'),
        ('WALL-E', 2008, 4.3, 'WALL-E.jpg'),
        ('X-MEN', 2000, 3.9, 'X-MEN.jpg'),
        ('You''ve Got Mail', 1998, 3.8, 'Youve Got Mail.jpg'),
        ('Zoolander', 2001, 4.0, 'Zoolander.jpg'),
    ]
    return data


def create_sqlite_database():
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE movie(title, year, rating, file_name)")
    data = [
        ('Alice in Wonderland', 2010, 3.4, 'Alice in Wonderland.jpg'),
        ('Back to the Future', 1985, 4.5, 'Back to the Future.jpg'),
        ('Casper', 1995, 3.3, 'Casper.jpg'),
        ('Despicable Me', 2010, 4.0, 'Despicable Me.jpg'),
        ('E.T.', 1982, 3.5, 'ET.jpg'),
        ('Fast and Furious', 2009, 3.7, 'Fast and Furious.jpg'),
        ('Ghostbusters', 1984, 4.2, 'Ghostbusters.jpg'),
        ('Hacksaw Ridge', 2016, 4.3, 'Hacksaw Ridge.jpg'),
        ('Indiana Jones', 2008, 3.3, 'Indiana Jones.jpg'),
        ('Jumanji', 1995, 3.5, 'Jumanji.jpg'),
        ('Kill Bill', 2003, 3.4, 'Kill Bill.jpg'),
        ('Little Nicky', 2000, 3.3, 'Little Nicky.jpg'),
        ('Matrix', 1999, 3.6, 'Matrix.jpg'),
        ('Nacho Libre', 2006, 3.3, 'Nacho Libre.jpg'),
        ('O brother, Where Art Thou', 2000, 4.1, 'OBrotherWhereArtThou.jpg'),
        ('Priest', 2011, 3.2, 'Priest.jpg'),
        ('Quarantine', 2008, 3.0, 'Quarantine.jpg'),
        ('R.I.P.D.', 2013, 3.0, 'RIPD.jpg'),
        ('Scary Movie', 2000, 3.0, 'Scary Movie.jpg'),
        ('Toy Story', 1995, 3.8, 'Toy Story.jpg'),
        ('UP.', 2009, 4.3, 'UP.jpg'),
        ('V For Vendetta', 2005, 4.3, 'V For Vendetta.jpg'),
        ('WALL-E', 2008, 4.3, 'WALL-E.jpg'),
        ('X-MEN', 2000, 3.9, 'X-MEN.jpg'),
        ('You''ve Got Mail', 1998, 3.8, 'Youve Got Mail.jpg'),
        ('Zoolander', 2001, 4.0, 'Zoolander.jpg'),
    ]

    cur.executemany("INSERT INTO movie VALUES(?, ?, ?, ?)", data)
    conn.commit()


def sqlite_insert(data: List[dict]):
    con_sqlite = sqlite3.connect("movies.db")
    cur = con_sqlite.cursor()

    sql = "INSERT INTO resource VALUES(?,?,?,?,?,?)"
    cur.executemany(sql, [list(i.values()) for i in data])
    con_sqlite.commit()


def writeHTML(name, year):
    file = 'movies.html'
    with open(file, 'w') as f:
        f.write('\n')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('    <center>\n')
        f.write(f'        <h1>Hi {name}. Here are some movie recommendations ',
                'for you!</h1>\n')
        f.write('    </center>\n')
        f.write('    <hr />\n')
        f.write(f'    {year}\n')
        f.write('    <hr />\n')
        f.write('</body>\n')
        f.write('</html>\n')

    f.close()


class Movie:
    def __init__(self, title, year, rating, image_name):
        self.title = title
        self.year = year
        self.rating = rating
        self.image_name = image_name


def getMovies():
    # get movies from database
    # put them into a list
    # return the list
    pass


if __name__ == '__main__':
    main()