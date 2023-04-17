import sqlite3 as db
'''
Students will develop a website with everything they have learned
during the semester. The theme of the project is up to the student.
Your code should use variables, conditions, loops, lists, dictionaries,
objects, GUI, etc. Students will present their project to the class
and explain and answer questions related to the code(5 - 15 minutes).
'''

'''
Grading Rubric (Up to 100 pts awarded)
Comments	1
Variables	1
Reading input from the keyboard	1
String concatenation	2
Conditions:
   - If statements	5
   - If-elif-else statements	5
Loops:
   - While	5
   - For	5
   - Nest loop of your choice	5
Functions	5
More about strings	5
Files and exceptions	10
List and Tuples	10
Dictionaries	10
Classes and Object-Oriented programming	10
GUI	10
Complexity	10


Bonus (TOTAL 20pts)
   - Recursion	10
   - Database Programming	10

'''
class Movie:
    def__init__(self, title, year, rating, image_name)
    self.title = title
    self.year = year
    self.rating = rating
    self.image_name = image_name

movies = getMovies()
for movie in movies:
    film = Movie(record.title, record.year, record.rating, record.file_name)
    movies.add(movie)

def initDB():
    conn = db.connect("movies.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE movie(title, year, rating, file_name)")
    data = [
        ('Monty Python and the Holy Grail', 1975, 8.2, 'image1.jpg'),
        ('And Now for Something Completely Different', 1971, 7.5, 'image1.jpg'),
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9, 'image1.jpg'),
        ("Monty Python's The Meaning of Life", 1983, 7.5, 'image1.jpg'),
        ("Monty Python's Life of Brian", 1979, 8.0, 'image1.jpg'),
    ]
    cur.executemany("INSERT INTO movie VALUES(?, ?, ?, ?)", data)
    conn.commit()

def getMovies():
    # get movies from database
    # put them into a list
    # return the list
    pass

def main():
    file = 'movies.html'
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


