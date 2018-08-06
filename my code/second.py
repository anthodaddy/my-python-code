import turtle

a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()

a.shape('turtle')
b.shape('turtle')
c.shape('turtle')
d.shape('turtle')

a.color('red', 'green')
b.color('red', 'green')
c.color('blue', 'black')
d.color('blue', 'black')

a.shapesize(3,3,0)
b.shapesize(3,3,0)
c.shapesize(4,4,0)
d.shapesize(4,4,0)

a.width(20)
a.circle(40)

b.penup()
c.penup()
d.penup()

b.forward(80)
b.pendown()
b.width(20)
b.circle(40)

c.forward(160)
c.pendown()
c.width(20)
c.circle(40)

