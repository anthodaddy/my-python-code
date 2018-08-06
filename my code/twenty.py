import turtle
q = turtle.Turtle()
w = turtle.Screen()

w.bgcolor('black')
q.pencolor('green')
w.listen()
w.title('W A S D')
q.speed(0)
q.setpos(0,0)
stepsize=10
sz=stepsize

def dot():
     for som in range(4):
          q.forward(sz)
          q.left(90)

#--------------------------------------#

def up():
     q.setheading(90)
     q.forward(sz)



def right():
     q.setheading(0)
     q.forward(sz)



def down():
     q.setheading(270)
     q.forward(sz)



def left():
     q.setheading(180)
     q.forward(sz)


#-------------------------------#
def clear():
     q.clear()



def penup():
     q.penup()


def pendown():
     q.pendown()



def home():
     q.penup()
     q.setpos(0, 0)
     q.pendown()

def stop():
     stop='true'
stop='false'


w.onkey(up, 'w')
w.onkey(right, 'd')
w.onkey(down, 's')
w.onkey(left, 'a')
w.onkey(penup, '1')
w.onkey(pendown, '2')
w.onkey(home, '3')
w.onkey(clear,'q')



#--------------------------------------------------key logged actions



##w.onclick(dot, btn=1, add=False)
