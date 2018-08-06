import turtle
q = turtle.Turtle()
w = turtle.Screen()
w.listen()
q.speed(0)
q.hideturtle()

def click(x, y):
     q.penup()
     q.setpos(x, y)
     q.pendown()
     q.begin_fill()
     for z in range(4):
          q.forward(10)
          q.left(90)
     q.end_fill()


w.onclick(click, btn=1)


