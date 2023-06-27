# Glass Zimny
# 29/9/29

def enum(n):
  if n==2:
    o = [[2],[1,1]]
  elif n==1:
    o = [[1]]
  else:
    o = [[n]]
    for i in range(1,n-1):
      prevN=enum(n-i)
      for j in range(len(prevN)):
        prevN[j].append(i)
        o.append(prevN[j])
  for i in o:
    iLoc=o.index(i)
    tempO = o[:iLoc]+o[iLoc+1:]
    for j in range(len(tempO)):
      tempO[j]=set(tempO[j])
    if set(i) in tempO:
      o.remove(i)
  return o

def prod(n):
  l = enum(n)
  o = []
  for i in l:
    product = 1
    for j in i:
      product *= j
    o.append(product)
  o = list(set(o))
  length = len(o)
  if length % 2 == 1:
    med = o[length//2]
  else:
    med = (o[(length-1)//2]+o[length//2])/2
  return "Range: "+str(o[-1]-o[0])+" Average: "+"{:0.2f}".format(sum(o)/len(o))+" Median: "+"{:0.2f}".format(med)
  


# https://www.codewars.com/kata/55cf3b567fc0e02b0b00000b
# enum(4) = [[4],[enum(3),1],[enum(2),2]] => [[4],[3,1],[2,1,1],[1,1,1,1],[2,2],[1,1,2]] => [[4],[3,1],[2,1,1],[1,1,1,1],[2,2]]
# enum(3) = [[3],[enum(2),1]] => [[3],[2,1],[1,1,1]]
# enum(2) = [[2],[1,1]]

# enum(n!=1) = [[n],[enum(n-1),1],[enum(n-2),2],....,[enum(2),n-2]]

for i in range(1,11):
  print(prod(i))
