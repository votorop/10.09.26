#!ussr\bin\python3
import turtle
turtle.speed(0)
for i in range(11):
    turtle.pendown()
    a = i*10
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.penup()
    turtle.forward(5)
    turtle.left(90)
    turtle.backward(5)
turtle.mainloop()
