from turtle import *
from math import sqrt
speed(0)
def kwadrat(d):
    if d > 1:
        for i in range(4):
            fd(2*d)
            rt(90)
        pu()
        fd(d)
        rt(45)
        pd()
        kwadrat(d / sqrt(2))

pu()
goto(-200,-200)
pd()
seth(90)
kwadrat( 200)

mainloop()
