"""
H-Tree Fractal using recursion and Turtle Graphics.
Robin Andrews - https://compucademy.net/
"""

from turtle import *


xx = 800
yy = 800
dx = 700
dy = 500
TITLE = ""
FRACTAL_DEPTH = 3


def linia(tt, pos1, pos2):
    tt.pu()
    tt.goto(pos1[0], pos1[1])
    tt.pd()
    tt.goto(pos2[0], pos2[1])


def rysujH(tt, x, y, dx, dy, n):
    linia(tt, [x + 1/4*dx, y + 1/2*dy], [x + 3/4*dx, y+1/2*dy])
    linia(tt, [x + 1/4*dx, y + 1/4*dy], [x + 1/4*dx, y+3/4*dy])
    linia(tt, [x + 3/4*dx, y + 1/4*dy], [x + 3/4*dx, y+3/4*dy])
    if n > 0:
        n -= 1
        rysujH(tt, x+0/2*dx, y+0/2*dy, dx/2, dy/2, n)  # Top left
        rysujH(tt, x+1/2*dx, y+1/2*dy, dx/2, dy/2, n)  # Bottom right
        rysujH(tt, x+1/2*dx, y+0/2*dy, dx/2, dy/2, n)  # Top right
        rysujH(tt, x+0/2*dx, y+1/2*dy, dx/2, dy/2, n)  # Bottom left


if __name__ == "__main__":
    # Screen setup
    okno = Screen()
    okno.setup(xx, yy)
    okno.title("H-Tree Fractal with Python Turtle Graphics")
    okno.bgcolor("yellow")

    # Turtle artist (pen) setup
    t = Turtle()
    t.hideturtle()
    t.pensize(2)
    t.color("red")
    t.speed(0)

    # Initial call to recursive draw function
    rysujH(t, -dx / 2, -dy / 2, dx, dy, 5)

    mainloop()
