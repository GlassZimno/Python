#Dominik Zimny
#10/1/2020
import turtle
import math
import random

lines = []
colours = ["gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

turtle.hideturtle()
turtle.penup()
turtle.setposition(300,0)
turtle.pendown()
turtle.left(90)
turtle.forward(10)
turtle.right(180)
turtle.forward(10)
turtle.right(90)


for i in range(12):
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(10)
    turtle.right(90)
turtle.penup()
turtle.setposition(0,-250)
turtle.pendown()
turtle.left(180)
turtle.forward(10)
turtle.right(180)
turtle.forward(10)
turtle.right(90)
for i in range(10):
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(10)
    turtle.right(90)
    
turtle.width(3)
turtle.penup()

again = "y"
while again == "y":
    turtle.penup()
    for i in range(len(lines)):
        print(lines[i])
    xSqCoeff = float(input("X^2 coefficient: "))
    curve = int(math.ceil(xSqCoeff * 5))
    xCoeff = float(input("X coefficient: "))
    yIntercept = float(input("Y Intercept: "))
    start = int(input("Starting x coordinate: ")) * curve
    end = int(input("Ending x coordinate: ")) * curve

    dig = random.randint(0,len(colours))
    colour = colours[dig]
    colours.pop(dig)
    turtle.color(colour)
    if yIntercept < 0:
        neg = "- "
    else:
        neg = "+ "
    if xCoeff < 0:
        xNeg = "- "
    else:
        xNeg = "+ "
    line = colour + ": y = " + str(xSqCoeff) + "x^2 " + xNeg + str(xCoeff) + "x " + neg + str(yIntercept)
    lines.append(line)
    
    
    for x in range(start,end+1):
        print(x**2, "aaa", xSqCoeff * (x**2))
        x /= curve / 2
        y = (xSqCoeff * (x**2)) + (xCoeff * x) + yIntercept
        turtle.setposition(x, y)
        turtle.pendown()
    again = ""
    while not again in ["y","n"]:
        again = input("Another quadratic? [y/n] ")
