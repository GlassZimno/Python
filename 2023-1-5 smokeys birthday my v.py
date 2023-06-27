import turtle
import time
import random

message = turtle.Turtle()
message.hideturtle()
message.penup()
message.left(90)
#time.sleep(random.randint(4,12))
text = ""
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
  chance = random.randint(1,100)
  for i in textOp:
    if chance>100-i[0]:
      text = i[1]
      break
  message.write(text, align="center", font=("cooper black",25,"normal"))
  message.fd(50)
  time.sleep(0.2)
  message.clear()
  
