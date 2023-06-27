#Nick Zimny
#21/12/20

import turtle
import time
import math

#setup enemy
enemy = turtle.Turtle()
enemy.shape("triangle")
enemy.color("red")

#setup screen
wn = turtle.Screen()
wn.title("Turt Time")
wn.screensize(520,520)
#draw border
enemy.pencolor("black")
enemy.hideturtle()
enemy.penup()
enemy.setposition(-260,260)
enemy.pensize(5)
enemy.speed(0)
enemy.pendown()
for i in range(4):
  enemy.forward(520)
  enemy.right(90)
enemy.penup()
enemy.setheading(90)
enemy.setposition(-240,0)
enemy.showturtle()

#setup player
player=turtle.Turtle()
player.shape("circle")
player.color("#1e90ff")
player.penup()

#setup golden apple
gapple = turtle.Turtle()
gapple.shape("circle")
gapple.color("gold")
gapple.shapesize(0.5)
#setup player enemy collision
def col():
  difs = dif()
  x = difs[0]
  y = difs[1]
  distance = math.sqrt(x**2 + y**2)
  if distance == 0:
    print("Game Over")
    
#setup enemy movement
def dif():
  xdif = enemy.xcor() - player.xcor()
  ydif = enemy.ycor() - player.ycor()
  return [xdif, ydif]

def emove(c):
  col()
  difs = dif()
  xdif = difs[0]
  ydif = difs[1]
  if abs(xdif) > abs(ydif):
    if not abs(xdif) == 40:
        c *= 2
    if xdif < 0:
      for i in range(s):
        enemy.setx(enemy.xcor()+c)
    else:
      for i in range(s):
        enemy.setx(enemy.xcor()-c)
  else:
    if not abs(ydif) == 40:
        c *= 2
    if ydif < 0:
      for i in range(s):
        enemy.sety(enemy.ycor()+c)
    else:
      for i in range(s):
        enemy.sety(enemy.ycor()-c)
  col()
  
#setup controls
c = 2
s = 20
def up():
  if s*c + player.ycor() <= 240:
    for i in range(s):
      player.sety(player.ycor() + c)
    emove(c)

def left():
  if player.xcor() - s*c >= -240:
    for i in range(s):
      player.setx(player.xcor() - c)
    emove(c)

def down():
  if player.ycor() - s*c >= -240:
    for i in range(s):
      player.sety(player.ycor() - c)
    emove(c)

def right():
  if s*c + player.xcor() <= 240:
    for i in range(s):
      player.setx(player.xcor() + c)
    emove(c)

wn.onkey(up,"w")
wn.onkey(left,"a")
wn.onkey(down,"s")
wn.onkey(right,"d")

wn.listen()
