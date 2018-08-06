def drawsquare(n,x):
  n.forward(x)
  n.left(90)
  n.forward(x)
  n.left(90)
  n.forward(x)
  n.left(90)
  n.forward(x)
  n.left(90)



import turtle
name=turtle.Turtle()
name.shape('turtle')
name.pencolor('black')

while -100<name.xcor()<100:
  drawsquare(name,10)




  #poopyrandan looks ugly
