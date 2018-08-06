import turtle
q=turtle.Turtle()
w=turtle.Screen()
w.listen()
q.hideturtle()
q.speed(0)

q.forward(300)
q.penup()
q.left(90)
q.forward(100)
q.pendown()
q.left(90)
q.forward(300)
q.left(180)
q.forward(100)
q.left(90)
q.forward(100)
q.left(180)
q.forward(300)
q.penup()
q.left(90)
q.forward(100)
q.pendown()
q.left(90)
q.forward(300)


def xxx(x, y):
     q.penup()
     q.setpos(x, y)
     q.write('X', font=('Arial', 30))
     q.pendown()

w.onclick(xxx, btn=1)
     
def ooo(x, y):
     q.penup()
     q.setpos(x, y)
     q.write('O', font=('Arial', 30))
     q.pendown()

w.onclick(ooo, btn=3)


def reset():
     q.clear()
     q.penup()
     q.setpos(0, 0)
     q.pendown()
     q.forward(300)
     q.penup()
     q.left(90)
     q.forward(100)
     q.pendown()
     q.left(90)
     q.forward(300)
     q.left(180)
     q.forward(100)
     q.left(90)
     q.forward(100)
     q.left(180)
     q.forward(300)
     q.penup()
     q.left(90)
     q.forward(100)
     q.pendown()
     q.left(90)
     q.forward(300)
     


w.onkey(reset, 'space')

