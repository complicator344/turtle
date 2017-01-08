import turtle


def square(size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)

def supersquare(posx, posy):
    turtle.penup()
    turtle.setx(posx)
    turtle.sety(posy)
    turtle.pendown()
    for x in xrange (5,100,5):
        square (x)

def jez(width):
    height = 7
    for x in xrange (1,width,2):
        turtle.penup()
        turtle.setx(0)
        turtle.sety(0)
        turtle.pendown()
        turtle.goto(x,height)

def circle (numberofcircles):
    for x in range (6,numberofcircles,6): 
        turtle.circle(x)
        


        
#supersquare(0,0)
#supersquare(-100,0)
#supersquare(100,0)
turtle.pencolor("blue")
#jez(200)
circle(1000)


raw_input ("Press any key to exit")





