import turtle

q = turtle.Turtle()
q.speed (0)


for x in range(9999999999999999999999) :
     q.width(5 + 1 * x)
     q.forward(50 + 5 * x)
     q.pencolor('blue')
     q.left(90 + 1 * x)
     q.forward(50 + 5 * x)
     q.pencolor('red')
     q.left(90 + 1 * x)
     q.forward(50 + 5 * x)
     q.pencolor('green')
     q.left(90 + 1 * x)
     q.forward(50 + 5 * x)
     q.pencolor('orange')
     q.left(90 + 1 * x)
     
