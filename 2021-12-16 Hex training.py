#Glass Zimno
#2021/12/16
import turtle
import random

ref=turtle.Turtle()
gu=turtle.Turtle()
s = turtle.Shape("compound")
poly=((-100,-100),(-100,100),(100,100),(100,-100))
s.addcomponent(poly, "#ffffff", "#000000")
turtle.register_shape("bsquare",s)
ref.shape("bsquare")
ref.penup()
ref.setpos(-150,0)
gu.shape("bsquare")
gu.penup()
gu.setpos(150,0)

file=open("hextrainingdifficulties.txt")
f = file.read().split("*&*")
file.close()
print("Available difficulties:")
flen=len(f)
difficulties = {}
for i in range(flen):
  f[i]=f[i].split(",")
  difficulties.update({f[i][0]:[f[i][1],f[i][2]]})
  print(str(i+1)+": "+f[i][0])
print(difficulties)
while True:
  choice=input("Please choose one: ")
  try:
    choice=int(choice)
  except ValueError:
    pass
  
def genhex():
  r,g,b=0,0,0
  n=[r,g,b]
  for i in range(3):
    v=hex(random.randint(0,255))[2:]
    if len(v)==1:
      v="0"+v
    n[i]=v
  return n

def dec(n):
  for i in range(3):
    n[i]=int(n[i],16)
  return n

def check(g,n,p):
  g=dec(g)
  dif=[0,0,0]
  for i in range(3):
    dif[i]=abs(n[i]-g[i])
    dif[i]=100*(dif[i]/255)
  av=sum(dif)/3
  if av<=p:
    return True
  return False

p=10
c=3
while True:
  n=genhex()
  s.addcomponent(poly,"#"+"".join(n),"#000000")
  num=dec(n)
  ref.shape("bsquare")
  for i in range(c):
    while True:
      guess="#"+input("guess "+str(i+1)+": #")
      if len(guess) == 7:
        break
    s.addcomponent(poly,guess,"#000000")
    gu.shape("bsquare")
    guess=[guess[1:3],guess[3:5],guess[5:]]
    if check(guess, num, p):
      print("Correct")
      break
    else:
      print("Wrong")
    print("The answer was #"+"".join(n))
    
