# Glass Zimny
# 3/1/2023

import turtle

player=[turtle.Turtle()]
player[0].penup()
turtle.setup(500,500)
turtle.title("I am trying")

scale=3
offset=2.5*scale*20
tile=[]
for i in range(36):
  tile.append(turtle.Turtle())
  tile[i].speed(0)
  tile[i].penup()
  tile[i].shape("square")
  tile[i].shapesize(scale,scale,1)
  tile[i].fillcolor("white")
  y=(i//6)*(scale*20)-offset
  x=(i%6)*(scale*20)-offset
  tile[i].goto(x,y)

player[0].left(90)
player[0].shapesize(scale,scale)
player[0].goto(-offset,-offset)
pos = [0,0]
coor=scale*20
d={"1":"up","2":"right","3":"down","4":"left"}
while True:
  truePos=player[0].pos()
  direction=input("direction: ").lower()
  if direction in d:
    direction = d[direction]
  if direction=="down":
    if pos[1]!=0:
      pos[1]-=1
      player[0].sety(truePos[1]-coor)
  elif direction=="up":
    if pos[1]!=5:
      pos[1]+=1
      player[0].sety(truePos[1]+coor)
  elif direction=="left":
    if pos[0]!=0:
      pos[0]-=1
      player[0].setx(truePos[0]-coor)
  elif direction=="right":
    if pos[0]!=5:
      pos[0]+=1
      player[0].setx(truePos[0]+coor)
  else:
    print("Not a valid direction")
