#!/usr/bin/python3
import turtle
turtle.tracer(False)

turtle.right(270)

def circle():
    for _ in range(200):
         turtle.forward(1)
         turtle.right(180/200)
    for _ in range(50):
         turtle.forward(1)
         turtle.right(180/50)

for i in range(4):
    circle()

turtle.update()
turtle.mainloop()
