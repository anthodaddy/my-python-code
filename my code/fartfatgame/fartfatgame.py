import turtle


q=turtle.Turtle()
w=turtle.Screen()
w.listen()
image='butt.gif'

w.register_shape(image)
q.shape(image)
w.bgpic("cbelt.gif")

q.penup()

w.bgcolor('black')
q.speed(0)

def dot():
     for som in range(4):
          q.forward(sz)
          q.left(90)

#--------------------------------------#

def up():
     q.setheading(90)
     q.forward(100)



def right():
     q.setheading(0)
     q.forward(100)



def down():
     q.setheading(270)
     q.forward(100)



def left():
     q.setheading(180)
     q.forward(100)


#-------------------------------#
def clear():
     q.clear()


w.onkey(up, 'w')
w.onkey(right, 'd')
w.onkey(down, 's')
w.onkey(left, 'a')



#--------------------------------------------------key logged actions



##w.onclick(dot, btn=1, add=False)

