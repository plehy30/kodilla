from turtle import *

speed(0)

def koch(d):
    if d<1:
        fd(d)
    else:
        koch(d/3)
        lt(60)
        koch(d/3)
        rt(120)
        koch(d/3)
        lt(60)
        koch(d/3)

pu()
goto(0,200)
rt(45)
pd()
#seth(90)
koch(300);rt(90)
koch(300);rt(90)
koch(300);rt(90)
koch(300);rt(90)
pu()
home()
mainloop()
