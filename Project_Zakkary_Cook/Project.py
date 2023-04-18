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


def getLetterFromName(name):
    result = 'A'
    return result


def getMovieWithLetterInTitle(letter_from_name):
    result = 'Quarantine.jpg'
    return result


def GetMovieBasedOnBirthYear(year):
    result = 'Indiana Jones.jpg'
    return result


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
        {'title': 'Alice in Wonderland', 'year': 2010, 'rating': 3.4, 'image': 'Alice in Wonderland.jpg'},
        {'title': 'Back to the Future', 'year': 1985, 'rating': 4.5, 'image': 'Back to the Future.jpg'},
        {'title': 'Casper', 'year': 1995, 'rating': 3.3, 'image': 'Casper.jpg'},
        {'title': 'Despicable Me', 'year': 2010, 'rating': 4.0, 'image': 'Despicable Me.jpg'},
        {'title': 'E.T.', 'year': 1982, 'rating': 3.5, 'image': 'ET.jpg'},
        {'title': 'Fast and Furious', 'year': 2009, 'rating': 3.7, 'image': 'Fast and Furious.jpg'},
        {'title': 'Ghostbusters', 'year': 1984, 'rating': 4.2, 'image': 'Ghostbusters.jpg'},
        {'title': 'Hacksaw Ridge', 'year': 2016, 'rating': 4.3, 'image': 'Hacksaw Ridge.jpg'},
        {'title': 'Indiana Jones', 'year': 2008, 'rating': 3.3, 'image': 'Indiana Jones.jpg'},
        {'title': 'Jumanji', 'year': 1995, 'rating': 3.5, 'image': 'Jumanji.jpg'},
        {'title': 'Kill Bill', 'year': 2003, 'rating': 3.4, 'image': 'Kill Bill.jpg'},
        {'title': 'Little Nicky', 'year': 2000, 'rating': 3.3, 'image': 'Little Nicky.jpg'},
        {'title': 'Matrix', 'year': 1999, 'rating': 3.6, 'image': 'Matrix.jpg'},
        {'title': 'Nacho Libre', 'year': 2006, 'rating': 3.3, 'image': 'Nacho Libre.jpg'},
        {'title': 'O brother, Where Art Thou', 'year': 2000, 'rating': 4.1, 'image': 'OBrotherWhereArtThou.jpg'},
        {'title': 'Priest', 'year': 2011, 'rating': 3.2, 'image': 'Priest.jpg'},
        {'title': 'Quarantine', 'year': 2008, 'rating': 3.0, 'image': 'Quarantine.jpg'},
        {'title': 'R.I.P.D.', 'year': 2013, 'rating': 3.0, 'image': 'RIPD.jpg'},
        {'title': 'Scary Movie', 'year': 2000, 'rating': 3.0, 'image': 'Scary Movie.jpg'},
        {'title': 'Toy Story', 'year': 1995, 'rating': 3.8, 'image': 'Toy Story.jpg'},
        {'title': 'UP.', 'year': 2009, 'rating': 4.3, 'image': 'UP.jpg'},
        {'title': 'V For Vendetta', 'year': 2005, 'rating': 4.3, 'image': 'V For Vendetta.jpg'},
        {'title': 'WALL-E', 'year': 2008, 'rating': 4.3, 'image': 'WALL-E.jpg'},
        {'title': 'X-MEN', 'year': 2000, 'rating': 3.9, 'image': 'X-MEN.jpg'},
        {'title': 'You''ve Got Mail', 'year': 1998, 'rating': 3.8, 'image': 'Youve Got Mail.jpg'},
        {'title': 'Zoolander', 'year': 2001, 'rating': 4.0, 'image': 'Zoolander.jpg'},
    ]
    return data


def sqlite_insert(data: List[dict]):
    con_sqlite = sqlite3.connect("movies.db")
    cur = con_sqlite.cursor()

    try:
        cur.execute("SELECT * FROM movie")  # check if the table already exists

    except sqlite3.OperationalError:
        print("Creating table: movie")
        cur.execute("CREATE TABLE movie(title, year, rating, image)")
        sql = "INSERT INTO movie VALUES(?,?,?,?)"
        cur.executemany(sql, [list(i.values()) for i in data])

    finally:
        con_sqlite.commit()
        con_sqlite.close()


def writeHTML(name, year):

    letter_from_name = getLetterFromName(name)
    movie_1 = getMovieWithLetterInTitle(letter_from_name)
    movie_2 = GetMovieBasedOnBirthYear(year)

    file = 'movies.html'
    with open(file, 'w') as f:
        f.write('\n')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('    <center>\n')
        f.write(f'        <h1>Hi {name}.</h1>\n')
        f.write('        <h1>Here are some movie recommendations for you!</h1>\n')
        f.write('    </center>\n')
        f.write('\n')
        f.write('    <hr />\n')
        f.write('    <h2>Here is a movie that begins with a letter\n')
        f.write(f'        from your name: {letter_from_name}</h2>\n')
        f.write(f'    <img src="Project_Zakkary_Cook/images/{movie_1}"\n')
        f.write('    width="250" style="display: block; margin: 30px auto;">\n')
        f.write('\n')
        f.write('    <hr />\n')
        f.write(f'    <h2>Here is a movie from your birth year: {year}</h2>\n')
        f.write(f'    <img src="Project_Zakkary_Cook/images/{movie_2}"\n')
        f.write('    width="250" style="display: block; margin: 30px auto;">\n')
        f.write('\n')
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