from turtle import *

speed(0)
def figura(d,k):
    if d >= 2:
        fd(d)
        rt(k)
        fd(d)
        lt(2*k)
        bk(d)
        rt(k)
        bk(d)
        rt(k)
        figura(0.98 * d, k)


pu()
goto(0,0)
pd()
seth(90)
figura( 60,25)

mainloop()
