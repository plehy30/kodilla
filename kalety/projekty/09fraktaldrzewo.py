from turtle import *

speed(0)
def drzewo(d,k):
    if d < 2:
        rt(90)
        circle(2)
        lt(90)
    else:
        fd(d)
        lt(k)
        drzewo(0.6 * d, k)
        rt(2 * k)
        drzewo(0.6 * d, k)
        lt(k)
        bk(d)

pu()
goto(0,-200)
pd()
seth(90)
drzewo( 100,40)

mainloop()
