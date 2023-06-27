import turtle
import time
import random

liveMessages = 6
moveAmount = 50
message = []
text=[]
for i in range(liveMessages):
  message.append(turtle.Turtle())
  text.append("")
  message[i] = turtle.Turtle()
  #message[i].hideturtle()
  message[i].penup()
  message[i].left(90)
#time.sleep(random.randint(4,12))
textOp = [
  (10,"\U0001F382Happy Birthday"),
  (20,"\U0001F382"),
  (30,"\U0001F924"),
  (40,"\U0001F389"),
  (50,"\U0001F499"),
  (60,"\U0001F389Happy Birthday\U0001F924"),
  (100,"\U0001F389")
  ]

while 1:
  for i in range(liveMessages):
    curY = message[i].ycor()
    if curY == 0:
      chance = random.randint(1,100)
      for j in textOp:
        if chance>100-j[0]:
          text[i] = j[1]
          break
      message[i].write(text[i],align="center",font=("cooper black",25,"normal"))
    if curY == moveAmount*liveMessages:
      message[i].clear()
      message[i].goto(0,0)
    else:
      message[i].fd(moveAmount)
    








