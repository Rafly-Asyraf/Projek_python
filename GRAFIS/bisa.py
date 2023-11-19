import turtle
from turtle import *

   
wn = Screen()
wn.bgcolor('black')
 
t = turtle.Turtle()
t.pencolor('white')
t.speed(9000)
def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)

def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()
heart()
t.ht()

def write(message,pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    t.color('white')
    Style=('stencil std',18,'italic')
    t.write(message,font=Style)

write('A',(-68,95))
write('U',(-55,95))
write('L',(-39,95))

write('P',(-14,95))
write('A',(-1,95))
write('N',(13,95))
write('T',(29,95))
write('E',(44,95))
write('K',(60,95))


wn.mainloop()
