# Glass Zimny
# 29/9/2022

def switch(l,d):
  for i in range(len(l)):
    if d:
      l[i]=tuple(l[i])
    else:
      l[i]=list(l[i])
  return l

l = [[4], [3, 1], [2, 1, 1], [1, 1, 1, 1], [2, 2], [1, 1, 2]]

for i in l:
  iLoc=l.index(i)
  tempL = l[:iLoc]+l[iLoc+1:]
  for j in range(len(tempL)):
    tempL[j].sort()
  if i in tempL:
    l.remove(i)

print(l)
print(switch(l,1))
