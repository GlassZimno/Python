#Dominik Zimny
#8/1/2020

colours = ["gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

import turtle
import random
turtle.speed(0)
turtle.width(3)
turtle.hideturtle()

c = 340
turtle.setposition(0,-c)
turtle.pendown()
turtle.setposition(0,c)
turtle.penup()

turtle.setposition(-c * 2,0)
turtle.pendown()
turtle.setposition(c * 2,0)
turtle.penup()

def newInt(q):
    while True:
        num = input(q)
        try:
            num = int(num)
            return num
        except:
            print("Incorrect input")

again = "y"

while again == "y":
    turtle.penup()
    start = newInt("Starting x coordinate: ")
    end = newInt("Ending x coordinate: ")
    while True:
            width = input("Width: ")
            try:
                width = float(width)
                break
            except:
                print("Incorrect input")
    width = 1 / width
    up = newInt("Apex y coordinate: ")
    right = newInt("Apex x coordinate: ")
    usd = input("Reverse parabola? [y/n] ")
    if usd == "y":
        neg = True
    else:
        neg = False
        
    a = 20
    b = a * 5

    start *= b
    end *= b + 1
    dig = random.randint(0,18)
    colour = colours[dig]
    colours.pop(dig)
    turtle.color(colour)
    
    for x in range(start, end):
        
        x /= b

        y = (((x * width) ** 2)*a)
        
        if neg == True:
            y = -y
        x = (x)*a + right
        
        turtle.setposition(x,y + up)
        turtle.pendown()
    again = ""
    while not again in ["y","n"]:
        again = input("Another quadratic? [y/n] ")
        
