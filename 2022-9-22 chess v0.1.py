# Glass Zimny
# 22/9/2022

board = [["bro","bkn","bbi","bqu","bki","bbi","bkn","bro"],
         ["bpa","bpa","bpa","bpa","bpa","bpa","bpa","bpa"],
         ["nul","nul","nul","nul","nul","nul","nul","nul"],
         ["nul","nul","nul","nul","nul","nul","nul","nul"],
         ["nul","nul","nul","nul","nul","nul","nul","nul"],
         ["nul","nul","nul","nul","nul","nul","nul","nul"],
         ["wpa","wpa","wpa","wpa","wpa","wpa","wpa","wpa"],
         ["wro","wkn","wbi","wqu","wki","wbi","wkn","wro"]]

bpm = []
wpm = []

i=0
pl = {0:"w",1:"b"}
while True:
  print("Player " + str(i+1) + "'s turn")
  
  while True:
    move = input("[piece][current location]to[target location] ")
    pID = move[:3]
    pCL = move[3:5]
    pTL= move[7:9]
    if pID[0] == pl[i]:
      break
    print("Not your piece")
  i = (i+1)%2
