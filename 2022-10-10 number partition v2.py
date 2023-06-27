# Glass Zimny
# 10/10/2022

def enum(n,calced):
  if n in calced:
    o = switch(calced[n],0)
  elif n==2:
    o = [[2],[1,1]]
  elif n==1:
    o = [[1]]
  else:
    o = [[n]]
    for i in range(1,n-1):
      prevN=switch(enum(n-i,calced)[0],0)
      for j in range(len(prevN)):
        prevN[j].append(i)
        o.append(prevN[j])
    for i in o:
      iLoc=o.index(i)
      tempO = o[:iLoc]+o[iLoc+1:]
      for j in range(len(tempO)):
        tempO[j].sort()
      if i in tempO:
        o.remove(i)
    calced[n]=switch(o,1)
  return o, calced

def switch(l,d):
  if not d:
    l=list(l)
  for i in range(len(l)):
    if d:
      l[i]=tuple(l[i])
    else:
      l[i]=list(l[i])
  if d:
    l=tuple(l)
  return l 

def prod(n):
  calced={}
  l,calced = enum(n,calced)
  o = []
  for i in l:
    product = 1
    for j in i:
      product *= j
    o.append(product)
  o = list(set(o))
  length = len(o)
  o.sort()
  if length % 2 == 1:
    med = o[length//2]
  else:
    med = (o[(length-1)//2]+o[length//2])/2
  return "Range: "+str(o[-1]-o[0])+" Average: "+"{:0.2f}".format(sum(o)/len(o))+" Median: "+"{:0.2f}".format(med)

for i in range(1,51):
      print(prod(i))


