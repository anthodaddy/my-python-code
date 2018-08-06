import turtle

q=turtle.Turtle()
w=turtle.Screen()
w.listen()
q.speed(0)
q.hideturtle()


def click(x, y):
     for spiral in range(10):
          
          q.penup()
          q.setpos(x, y)
          q.pendown()
          for circles in range(15):
##               q.begin_fill()
               q.circle(10 + 1 * circles)
##               q.end_fill()
          q.forward(100 + 10 * spiral)
          q.write(x, y)
          q.left(90)

w.onclick(click, btn=1)

def clear():
     q.clear()

w.onkey(clear, 'space')
