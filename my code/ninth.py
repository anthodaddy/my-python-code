import turtle

a = turtle.Turtle()
a.shape('turtle')
a.speed(0)

sides= int (input('number of sides') )
colorlist = []
for x in range(sides) :
     new_color = input('type a color')
     colorlist.append(new_color)


for x in range(99999999999999999999999999999999999999999999999999999999999) :
     a.left(360 / sides + 2)
     a.forward(1 + 2 * x)
     a.width(1 + 0.02 * x)
     a.pencolor(colorlist[x % sides] )
