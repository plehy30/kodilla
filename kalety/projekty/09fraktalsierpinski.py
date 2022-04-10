from turtle import *

speed(0)

def sierpinski(d):
    if d>3:
        for i in range(3):
            sierpinski(d/2)
            fd(d)
            rt(120)

pu()
setpos(0,200)
pd()
rt(60)
sierpinski(400)
lt(60)

mainloop()
