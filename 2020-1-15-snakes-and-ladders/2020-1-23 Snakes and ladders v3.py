#Glass Zimny
#21/1/2020
#Runs on python 3.6
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
    87 : 24,
    93 : 73,
    95 : 75,
    98 : 79
    }

#Create a dictionary for all ladders
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
def move(player, square, look, moves, turtle):
    #Move the player around corners
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
        #Increment the square's number
        square = int(square) + 1
        if square >= 100:
            return [0, "win"]
       
    #Check if the player is either on a snake or a ladder
    if square in snakes:
        goTo = snakes[square]
        m = True
    elif square in ladders:
        goTo = ladders[square]
        m = True
    else:
        m = False
    if m == True:
        square = goTo
       
        #Find the coordinates the player will go to based on the square's number
        time.sleep(0.5)
        player.speed(1)
        x = (goTo - 1) % 10
        y = (goTo - 1) // 10
        x *= 50
        y *= 50
        if y % 20 == 0:
            x -= 215
            y -= 235


            #Make the player definitely look right
            if look != "right":
                player.right(180)
            look = "right"
        else:
            x =  235 - x
            y -= 235
            #Definite left
            if look != "left":
                player.right(180)
            look = "left"

        #Make the computer move to the top left of the square
        if turtle == "computer":
            x -= 20
            y += 20
        endX = x
        endY = y
        player.goto(endX, endY)
        if square >= 100:
            return [0, "win"]


    #Return square and look to be used next time
    return [square, look]

#Create the player
player = turtle.Turtle()
player.shape("circle")
player.color("#1e90ff")
player.penup()
player.speed(0)

#Create the computer
computer = turtle.Turtle()
computer.shape("circle")
computer.color("#ff8000")
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
players = ""

while not players in [1, 2]:
    try:
        players = int(input("How many people playing? "))
        if players > 2:
            print("No more than two players")
        elif players < 1:
            print("Can't have no players")
    except:
        print("Must be a number")

if players == 1:
    p = "Your"
    c = "Computer"
    print("You are blue\nComputer is orange")
else:
    p = "Player 1"
    c = "Player 2"
    print("Player1 is blue\nPlayer 2 is orange\n")

#Main game loop
while True:
    if players == 1:
        print("Your turn")
    else:
        print("Player 1's turn")
    #Player initiates roll
    while pMove != "":
        pMove = input("Press \"enter\" to roll ")
    pMove = roll()
    print(p, "rolled ", pMove)
    salCheck = move(player, pSquare, pLook, pMove, "player")
    pSquare = salCheck[0]
    pLook = salCheck[1]
    if pLook == "win":
        time.sleep(0.5)
        pic = "win.gif"
        turtle.register_shape(pic)
        turtle.shape(pic)
        break

    cRoll = 1
    cMove = 1
    print(c + "'s turn:")
    #computer rolls
    if players == 2:
        while cMove != "":
            cMove = input("Press \"enter\" to roll ")
    cMove = roll()
    print(c, "rolled", cMove)
    salCheck = move(computer, cSquare, cLook, cMove, "computer")
    cSquare = salCheck[0]
    cLook = salCheck[1]
    if cLook == "win":
        time.sleep(0.5)
        pic = "lose.gif"
        turtle.register_shape(pic)
        turtle.shape(pic)
        break
