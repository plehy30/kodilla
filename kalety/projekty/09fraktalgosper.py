from turtle import *

speed(0)

def gosper(d):
    fd(d)
    rt(60)
    fd(d)
    rt(120)
    fd(d)
    lt(60)
    fd(d)
    lt(120)
    fd(2*d)
    lt(60)
    fd(d)







pu()
setpos(0,0)
pd()
seth(90)
for i in range(100):
    gosper(40)
    lt(60)
    gosper(40)
    rt(60)

mainloop()
