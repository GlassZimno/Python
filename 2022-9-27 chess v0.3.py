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
# n is in the form [row, column] 
def AlToNum(a):
  n=[8-int(a[1]),ord(a[0])-97]
  return n

i=0
pl = {0:"w",1:"b"}
while True:
  # Ask user for input, sanitise and check 
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
    # Check piece is correct
    if board[CL[0]][CL[1]] == pID:
      # Check the player isn't trying to capture their own piece
      if TP[0] != pl[i]:
        # Check piece isn't being requested to be moved to where it already is
        if TL != CL:
          # Check the piece being moved belongs to the current player
          if pID[0] == pl[i]:
            pID=pID[1:]
            m = False
            difx,dify = TL[1] - CL[1], TL[0] - CL[0]
            # Check if the selected piece can move as requested
            if pID == "pa":
              if i:
                if difx==0 and dify==1:
                  m = True
                elif CL[0]==1 and difx==0 and dify==2:
                  m = True
              else:
                if difx==0 and dify==-1:
                  m = True
                elif CL[0]==6 and difx==0 and dify==-2:
                  m = True
            aDifx,aDify=abs(difx),abs(dify)
            if pID in ["qu","bi"] and aDifx == aDify:
              m = True
            if pID in ["qu","ro"] and ((aDifx!=0 and aDify==0) or (aDify!=0 and aDifx==0)):
              m = True
            if pID == "ki" and  aDifx<2 and aDify<2:
              m = True
            if pID == "kn" and ((aDifx==2 and aDify==1) or (aDifx==1 and aDify==2)):
              m = True
            if pID != "kn":
              # Find if any pieces are in the way of the current piece's movement
              movedTo = [CL[0],CL[1]]
              while True:
                if movedTo[0]==TL[0] and movedTo[1]==TL[1]:
                  break
                if dify<0:
                  movedTo[0]-=1
                if dify>0:
                  movedTo[0]+=1
                if difx<0:
                  movedTo[1]-=1
                if difx>0:
                  movedTo[1]+=1
                if board[movedTo[0]][movedTo[1]] != "nul":
                  m = False
            if m:
              break
            # Inform user of errors
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
