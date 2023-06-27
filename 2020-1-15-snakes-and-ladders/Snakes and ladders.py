#Dominik Zimny
#15/1/2020
import turtle
import random
import time
import math

#Create a dictionary for all snakes
snakes = {
    17 : 7,
    54 : 34,
    62 : 19,
    64 : 60,
    87 : 87,
    93 : 73,
    95 : 75,
    98 : 79
    }

ladders = {
    1 : 38,
    4 : 14,
    9 : 31,
    21 : 42,
    28 : 84,
    51 : 67,
    71 : 91,
    80 : 100
    }

#generate the game board
screen = turtle.Screen()
#screen.setup(525,525)
screen.setup(800,700)
screen.bgpic("bg.gif")

#Create a function to roll a die
def roll():
    num = random.randint(1,6)
    print("Rolling", end = "")
    for i in range(3):
        time.sleep(0.75)
        x = "."
        print(x, end = "")
    print("")
    return num

#Move the player
def move(player, square, look, moves):
    print(player)
    for i in range(moves):
        square = str(square)
        time.sleep(0.5)
        if square[-1] == "0" and not square == "0" and int(square) <= 100:
            if look == "right":
                player.left(90)
            else:
                player.right(90)
            player.forward(50)
            if look == "right":
                player.left(90)
                look = "left"
            else:
                player.right(90)
                look = "right"
        else:
            player.forward(50)
        square = int(square) + 1
        print(square)
        if square >= 100:
            return [0, "win"]
    salCheck = sal(player, square, look)
    return salCheck

#Find the coordinates of a square
def findSquare(player, square, look):
    x = (square - 1) % 10
    y = (square - 1) // 10
    x *= 50
    y *= 50
    if y % 20 == 0:
        x -= 215
        y -= 235
        if look != "right":
            player.right(180)
        look = "right"
    else:
        x =  235 - x
        y -= 235
        if look != "left":
            player.right(180)
        look = "left"
    return [x, y, look]

def slide(player, end, look):
    time.sleep(0.5)
    player.speed(1)
    end = findSquare(player, end, look)
    endX = end[0]
    endY = end[1]
    look = end[2]
    player.goto(endX, endY)
    return look

def sal(player, square, look):
    if square in snakes:
        goTo = snakes[square]
        m = True
    elif square in ladders:
        goTo = ladders[square]
        m = True
    else:
        m = False
        return [square, look]
    if m == True:
        look = slide(player, goTo, look)
        return [goTo, look]
    
#Create the player
player = turtle.Turtle()
player.shape("circle")
player.color("black", "purple")
player.penup()
player.speed(0)

#Create the computer
computer = turtle.Turtle()
computer.shape("circle")
computer.color("black", "maroon")
computer.penup()
computer.speed(0)

#Squares are 50 x 50 pixels
player.setposition(-265,-235)
computer.setposition(-285, -215)

#Set up the default for the player and computer
pSquare = 0
pMove = 0
pLook = "right"
cSquare = 0
cLook = "right"


#Main game loop
while True:
    print("Your turn:")
    #Player initiates roll
    while pMove != "":
        pMove = input("Press \"enter\" to roll ")
    pMove = roll()
    print("you rolled ", pMove)
    salCheck = move(player, pSquare, pLook, pMove)
    pSquare = salCheck[0]
    pLook = salCheck[1]
    if pLook == "win":
        time.sleep(0.5)
        pic = "win.gif"
        turtle.register_shape(pic)
        turtle.shape(pic)
        break
        
    cRoll = 1
    print("Computer's turn:")
    #computer rolls
    cMove = roll()
    print("Computer rolled rolled ", cMove)
    salCheck = move(computer, cSquare, cLook, cMove)
    cSquare = salCheck[0]
    cLook = salCheck[1]
    if cLook == "win":
        time.sleep(0.5)
        pic = "lose.gif"
        turtle.register_shape(pic)
        turtle.shape(pic)
        break
