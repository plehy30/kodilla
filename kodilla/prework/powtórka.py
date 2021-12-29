import turtle

zolw = turtle.Turtle()
zolw.shape("turtle")

zolw.penup()
zolw.goto(-200, 200)
zolw.pendown()
zolw.color('green')
zolw.fillcolor('red')
zolw.begin_fill()
zolw.forward(400)
zolw.right(90)
zolw.forward(400)
zolw.right(90)
zolw.forward(400)
zolw.right(90)
zolw.forward(400)
zolw.right(90)
zolw.end_fill()

zolw.penup()
zolw.goto(-400, 200)
zolw.pendown()
zolw.color('black')
for i in range(3):
    zolw.forward(200)
    zolw.left(120)
