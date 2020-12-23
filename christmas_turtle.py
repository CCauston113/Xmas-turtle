import turtle
import random

turg = turtle.Turtle()
turg.shape("turtle")
turg.shapesize(0.5, 0.5, 1)
turg.pencolor("green")
turg.color("green")
turg.penup()

turg.write("Merry Christmas people!", 'true', 'center', ('Comic sans', 18, 'bold'))

#sky
turg.pencolor("lightblue")
turg.color("lightblue")
turg.setposition(120, -10)
turg.pendown()
turg.begin_fill()
turg.setposition(120, -140)
turg.setposition(-120, -140)
turg.setposition(-120, -10)
turg.setposition(120, -10)
turg.end_fill()
turg.penup()

#tree time
turg.pencolor("darkgreen")
turg.color("darkgreen")

turg.setposition(50, -50)
turg.pendown()
turg.begin_fill()
turg.setposition(76, -50)
turg.setposition(63, -25)
turg.end_fill()
turg.penup()

turg.setposition(40, -80)
turg.pendown()
turg.begin_fill()
turg.setposition(86, -80)
turg.setposition(63, -40)
turg.end_fill()
turg.penup()

turg.setposition(30, -110)
turg.pendown()
turg.begin_fill()
turg.setposition(96, -110)
turg.setposition(63, -60)
turg.end_fill()
turg.penup()

turg.pencolor("brown")
turg.color("brown")
turg.setposition(58, -110)
turg.right(90)
turg.pendown()
turg.begin_fill()
turg.fd(30)
turg.left(90)
turg.fd(10)
turg.left(90)
turg.fd(30)
turg.left(90)
turg.fd(10)
turg.end_fill()
turg.penup()

#snow time
turg.pencolor("snow")
turg.color("snow")

xPos = [109, 91, 103]
yPos = [-23, -52, -77]

for n in range (1, 50):
    x = random.randint(-115, 115)
    xPos.append(x)
    y = random.randint(-135, -15)
    yPos.append(y)

for i in range (0, len(xPos)):
    turg.setpos(xPos[i], yPos[i])
    turg.dot(5)
