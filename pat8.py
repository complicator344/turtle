import turtle
import math



def rectangle(width, height):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)

def triangle(short_side):

    asq = short_side**2
    bsq = short_side**2
    answer = math.sqrt(asq + bsq)

    turtle.pencolor("blue")
    turtle.forward(short_side)
    turtle.right(90)
    turtle.pencolor("red")    
    turtle.forward(short_side)
    turtle.right(135)
    turtle.pencolor("blue")
    turtle.forward(answer)
    turtle.right(45)

triangle(211)
raw_input ("Press any key to exit")
