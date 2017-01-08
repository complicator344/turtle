import decimal
import math

a = int(raw_input ("Enter lenght of side A: "))
b = int(raw_input ("Enter lenght of side B: "))

    turtle.pencolor("blue")
    asq = a**2
    bsq = b**2
    answer = math.sqrt(asq + bsq)

print str(a) + " squared equals " + str(asq)
print str(b) + " squared equals " + str(bsq)
print str(answer)


