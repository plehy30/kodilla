from turtle import *

speed(0)
def paprotka(d,k):
    if d > 5:
        fd(d/2)
        lt(70+k)
        paprotka(0.5*d,k)
        rt(70+k)
        fd(d/2)
        rt(70-k)
        paprotka(0.5*d,-k)
        lt(70-k)
        rt(k)
        paprotka(d-2,k)
        lt(k)
        bk(d)

pu()
goto(0,-100)
pd()
seth(90)
paprotka( 30,2)

mainloop()
