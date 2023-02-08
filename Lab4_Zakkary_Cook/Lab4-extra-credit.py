"""
use a loop with the turtle graphics library to draw the design shown:
"""
import turtle as t

def main():
    t.pensize(1)
    t.pencolor("black")

    t.pendown()
    for i in range(50):
        t.forward(10 * i)
        t.left(90)

    input()

if __name__ == "__main__":
    main()
