#!/usr/bin/python3
import turtle

turtle.tracer(False)
turtle.speed(0)
turtle.right(90)

S = 200

def circle():
    for _ in range(S):
        turtle.forward(1)
        turtle.left(360/S)
    for _ in range(S):
        turtle.forward(1)
        turtle.right(360/S)

for i in range(10):
    S = S+40
    circle()

    

turtle.update()
turtle.mainloop()
