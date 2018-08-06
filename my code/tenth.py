import turtle

b = turtle.Turtle()
b.shape('turtle')
b.speed(0)

##b.setpos(0, 0)
##b.setpos(50, -60)
##b.setpos(0, -120)
##b.setpos(50, -120)
##b.setpos(0, -60)
##b.setpos(50, 0)
##b.setpos(0, 0)

sides = int(input('how many sides') )
print(sides)
            
for x in range(200999999999999999999999999999999999999999999999999999):
     b.forward(5 * x + 2)
     b.left(360 / sides + 2)
     
