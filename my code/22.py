import turtle
q=turtle.Turtle()
w=turtle.Screen()
w.bgcolor('green')
q.hideturtle()
##q.speed(0)


for dud in range(4):
     q.forward(100)
     for oh in range(4):
##          q.begin_fill()
          q.circle(20)
##          q.end_fill()
          q.left(90)
     q.left(90)

     q.begin_fill()
     q.end_fill()
show turtle
