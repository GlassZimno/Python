#Dominik Zimny
#12/11/2019

def enter(limit):
  total = 0
  for i in range(0, limit):
    limit = 0
    coins[i] = input()
    coins[i] = coins[i].lower()
    if coins[i] == "stop":
      limit = "s"
      break
    try:
      coins[i] = int(coins[i])
    except ValueError:
      limit += 1
    if coins[i] in real:
      total = total + 1
    else:
      limit += 1
    return limit

coins = [1,2,3,4,5,6,7,8,9,10]
real = [1,2,5,10,20,50,100,200]
while True:
  do = input()
  loop = True
  while do == "clear":
    for i in range(0,10):
      coins[i] = 0
    print(coins)
    do = ""
  while do == "new":
    limit = 10
    while  limit != "stop":
      limit = enter(limit)
    total = str(total)
    print(total+"p")
    break
