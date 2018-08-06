import turtle

c = turtle.Turtle()

c.shape('turtle')
c.speed(0)

sides = int(input('side'))
print (sides)

for x in range (9999999999999999999999):
     c.forward(5*x)
     pos=c.position()
     head=c.heading()
     for y in range(x) :
          c.forward(y)
          c.left(360/sides+2)
     c.setpos(pos)
     c.setheading(head)
     c.left(360/sides+2)
