import turtle
aiden = turtle.Turtle()
aiden.shape('turtle')
aiden.speed(0)
aiden.pencolor('blue')

####for x in range(9999999999999999999999999999) :
######     aiden.circle(90 + 1 * x)
######     aiden.pencolor('yellow')
######     aiden.forward(4 + 1 * x)
######     aiden.pencolor('blue')
######     aiden.circle(90 + 1 * x)
######     aiden.pencolor('green')
######     aiden.backward(4 + 1 * x)
######     aiden.pencolor('red')
######     aiden.left(90 + 0.1 * x)
######     aiden.pencolor('brown')
######     aiden.forward(90 + 1 * x)
######     aiden.pencolor('black')
######     aiden.circle(90 + 1 * x)
######     aiden.pencolor('grey')
######     for x in range(9 + 1 * x) :
######          aiden.backward(1 + 2 * x)
######          aiden.pencolor('blue')
######          aiden.circle(20 + 3 * x)
######          aiden.pencolor('lightgreen')
######          aiden.forward(1 + 2 * x)
######          aiden.pencolor('black')
######          aiden.circle(20 + 3 * x)
######          aiden.pencolor('orange')
######
######
##
##for x in range(99999999999999999999) :
##     aiden.circle(10 + 1 * x)
##     aiden.right(5 + 1 * x)

##aiden.circle(40)
colorlist = ('red', 'yellow', 'red', 'blue', 'yellow')
cic = int (input('type number of circles here') )
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for x in range(cic) :
     aiden.pencolor(colorlist[x % 5] )
     aiden.circle(cic * 5, 180)
     aiden.write(alphabet[cic - 1])
     aiden.circle(cic * 5, 180)
     aiden.left(360 / cic)

