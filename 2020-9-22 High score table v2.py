#Dominik Zimny
#22/9/2020
file = open("highScores.txt")
top10 = file.read().split(",")
file.close

def table(i, biggest, biggestName):
  if i == 0:
    print("Top 10 leaderboard: ")
  print("%s %-15s %s" %(str(i+1) + ")",biggestName, str(biggest)))
  
for i in range(1,len(top10),2):
  table(i//2, int(top10[i]), top10[i-1])
  
score = input("Enter new score: ")
name = input("Enter your name: ")

top10.append(name)
top10.append(score)
top10Scores = []
top10Names = []
newTop10 = ""

for i in range(1,len(top10),2):
  top10Scores.append(int(top10[i]))
  top10Names.append(top10[i-1])
  table(i//2, int(top10[i]), top10[i-1])
  
for i in range(10):
  biggest = max(top10Scores)
  bigPos = top10Scores.index(biggest)
  top10Scores.remove(biggest)
  biggestName = top10Names[bigPos]
  top10Names.remove(biggestName)
  table(i, biggest, biggestName)
  newTop10 += biggestName + "," + str(biggest)+ ","

file = open("highScores.txt","w")
file.write(newTop10[:-1])
file.close()
  
