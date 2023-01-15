import turtle as t


def main():
    try3()
    input()

def try3():
    setup()
    colors = ['blue', 'yellow', 'black', 'green', 'red', 'pink', 'brown']
    x_pos = -300
    y_pos = 0

    for color in colors:
        t.goto(x_pos, y_pos)
        drawCircle(color)
        x_pos = x_pos + 130
        y_pos = 0 if y_pos == -100 else -100

def try2():
    setup()

    t.goto(-300,0)
    drawCircle('blue')

    t.goto(-170,-100)
    drawCircle('yellow')
  
    t.goto(-40,0)
    drawCircle('black')

    t.goto(90,-100)
    drawCircle('green')

    t.goto(220,0)
    drawCircle('red')

def try1():
    t.hideturtle()

    t.penup()
    t.goto(-300,0)
    t.pendown()

    t.pencolor('blue')
    t.pensize(5)
    t.circle(100)

    t.penup()
    t.goto(100,-100)
    t.goto(-200,-100)
    t.forward(30)
    t.pendown()

    t.pencolor('yellow')
    t.pensize(5)
    t.circle(100)

    t.penup()
    t.goto(-100,0)
    t.forward(50)
    t.pendown()

    t.pencolor('black')
    t.pensize(5)
    t.circle(100)

    t.penup()
    t.goto(100,-100)
    t.goto(-200,-100)
    t.forward(100)
    t.forward(175)
    t.pendown()

    t.pencolor('green')
    t.pensize(5)
    t.circle(100)

    t.penup()
    t.goto(200,0)
    t.pendown()

    t.pencolor('red')
    t.pensize(5)
    t.circle(100)

def setup():
    t.hideturtle()
    t.penup()
    t.pensize(5)

def drawCircle(color, size = 100):
    t.pencolor(color)
    t.pendown()
    t.circle(size)
    t.penup()


if __name__ == "__main__":
    main()