# Glass Zimny
# 27/9/2022

# First letter denotes if the piece is black or white,
# then the remaining two letters are the first two of the piece's full name
# null is shortened to match the length of all piece codes
board = [["bro","bkn","bbi","bqu","bki","bbi","bkn","bro"],
         ["bpa","bpa","bpa","bpa","bpa","bpa","bpa","bpa"],
         ["nul","nul","nul","nul","nul","nul","nul","nul"],
         ["nul","nul","nul","nul","nul","nul","nul","nul"],
         ["nul","nul","nul","nul","nul","nul","nul","nul"],
         ["nul","nul","nul","nul","nul","nul","nul","nul"],
         ["wpa","wpa","wpa","wpa","wpa","wpa","wpa","wpa"],
         ["wro","wkn","wbi","wqu","wki","wbi","wkn","wro"]]

whiteGrave = []
blackGrave = []

# Small function to turn classic codes to a usable number, e.g. "a1" to [0,7]
# n is in the form [column, row] 
def AlToNum(a):
  n=[8-int(a[1]),ord(a[0])-97]
  return n

i=0
pl = {0:"w",1:"b"}
while True:
  print("Player " + str(i+1) + "'s turn")
  for j in range(8):
    print(board[j])
  while True:
    move = input("[piece][current location]to[target location] ").lower()
    pID = move[:3]
    pCL = move[3:5]
    pTL= move[7:9]
    CL = AlToNum(pCL)
    TL = AlToNum(pTL)
    TP = board[TL[0]][TL[1]]
    print(TP)
    if board[CL[0]][CL[1]] == pID:
      if TP[0] != pl[i]:
        if TL != CL:
          if pID[0] == pl[i]:
            pID=pID[1:]
            m = False
            
            difx,dify = TL[1] - CL[1], TL[0] - CL[0]
            if pID == "pa":
              print(difx,dify,i)
              if i and difx==0 and dify==1:
                m = True
              elif (not i) and difx==0 and dify==-1:
                m = True
            difx,dify=abs(difx),abs(dify)
            if pID in ["qu","bi"] and difx == dify:
              m = True
            if pID in ["qu","ro"] and ((difx!=0 and dify==0) or (dify!=0 and difx==0)):
              m = True
            if pID == "ki" and  difx<2 and dify<2:
              m = True
            if pID == "kn" and ((difx==2 and dify==1) or (difx==1 and dify==2)):
              m = True
            if m:
              break
            else:
              print("This piece cannot move like that")
          else:
            print("Not your piece")
        else:
          print("Piece is already here")
      else:
        print("Cannot capture your own pieces")
    else:
      print("This piece is not here")
  if not TP == "nul":
    if i:
      whiteGrave.append(TP)
    else:
      blackGrave.append(TP)
  board[TL[0]][TL[1]] = pl[i]+pID
  board[CL[0]][CL[1]] = "nul"
  i = (i+1)%2
