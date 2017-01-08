import turtle

patrickwayup = 2

patrickway = 100
turtle.shape("turtle")
turtle.speed(4)
while patrickwayup < 100:
    turtle.forward(patrickway)
    patrickwayup = patrickwayup + 2
    turtle.left(90)
    turtle.forward(patrickwayup)
    turtle.left(90)
raw_input ("Press any key to exit")
