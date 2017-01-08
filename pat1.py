import turtle

patrickwayup = 100

patrickway = 200
turtle.shape("turtle")
turtle.speed(5)
while patrickwayup < 200:
    turtle.forward(patrickway)
    patrickwayup = patrickwayup + 10
    turtle.left(97)
    turtle.forward(patrickwayup)
    turtle.left(97)
raw_input ("Press any key to exit")
