import turtle
import random

screen = turtle.Screen()
screen.bgcolor('black')

q = turtle.Turtle()
q.hideturtle()
q.speed(0)

for x in range(99999999999999999999999):
     print (random.randint (0, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999) )
     q.forward(100 + 2 * x)
     q.left(90 + 1 * x)
     q.pencolor('blue')
     q.forward(20 + 3 * x)
     q.left(90 + 1 * x)
     print (random.randint (0, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999) )
     q.pencolor('green')
     q.right(80 + 2 * x)
     q.pencolor('white')
     q.circle(10 + 1 * x)
     q.pencolor('green')
     q.forward(10 + 5 * x)
     print (random.randint (0, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999) )
     q.left(90)
     q.left(90)
     q.forward(50 +1 * x)
     q.width(1 + 0.08 * x)
