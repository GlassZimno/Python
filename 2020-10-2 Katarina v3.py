#Nick Zimny
#2/10/2020
import random
import getpass
import time

def roll(num):
  rolls = []
  input("Press [enter] to roll ")
  print("Rolling...")
  time.sleep(0.3)
  for i in range(num):
    rolls.append(random.randint(1,6))
    print("Die "+str(i+1) + ": ", rolls[i])
  return rolls

def turn(player, score):
  for j in range(2):
    print("\n"+player[j]+ "'s turn: ")
    rolls = roll(2)
    total = sum(rolls)
    output = "(" + str(rolls[0]) + " + " + str(rolls[1]) + ")"
    if total % 2 == 0:
      total += 10
      output += " + 10"
      if rolls[0] == rolls[1]:
        print("Double!\nRoll again!")
        bonus = roll(1)
        total += bonus[0]
        output += " + " + str(bonus[0])
    else:
      total -= 5
      output += " - 5"
    if total <=0:
      total = 0
    score[j] += total
    print(output + " =", total)
    print(player[j] + "'s score current sore:", score[j])
  return score

def encrypt(privateKey, userKey, mas):
  #determine if master password is need or not
  if mas:
    prompt = "Master password: "
  else:
    prompt = "Please enter password: "
  #securely let user input password (only in console)
  password = getpass.getpass(prompt)
  #find the first starting seed for the encryption
  seed = privateKey * userKey
  output = ""
  for i in password:
    #find numeric value of each character
    num = ord(i)
    num *= seed
    output += str(hex(num)).replace("0x", "")

    #make a new seed from the old one
    seed = str(seed)
    total = 0
    #find the sum of the numbers in the seed
    for i in seed:
      total += int(i)
    #find the 6 middle numbers (excluding the middle num if odd length)
    length = len(seed)
    midPoint = length//2
    mid = []
    if length % 2 != 0:
      seed = seed[:midPoint] + seed[midPoint+1:]
    #add total so that no two starting seeds ever make the same seed later
    seed = int(seed[midPoint-3: midPoint+3]) + total
    seed **= 2
  return output

def infoUpdate(fileName, cont):
  #update the users' info text file
  file = open(fileName,"w")
  file.write(",".join(cont))
  file.close()

def login(privateKey, mas, num):
  #loop entire function until a valid username and password are provided
  while True:
    if mas != True:
      print("\nPlayer"+num+":")
      userInput = input("To login, enter your username.\nTo create a new account, press [enter]\n").replace(" ","")
    else:
      userInput = "MasterLogin"
    if userInput == "":
      while True:
        username = input("Please enter a username(or 'b' to go back): ").replace(" ","")
        if username in userInfo:
          print("That username already exists")
        elif username == "b":
          break
        else:
          file = open("availableKeys.txt")
          availableKeys = file.read().split(",")
          file.close()
          length = len(availableKeys)
          userKey = int(availableKeys[random.randint(0,length)-1])
          password = encrypt(privateKey, userKey, False)
          
          for i in [username, str(userKey), password]:
            userInfo.append(i)
          infoUpdate(userInfo)
          userInput = username
          break
      break
    if userInput in userInfo:
      userPos = userInfo.index(userInput)
      userKey = int(userInfo[userPos+1])
      userPassword = userInfo[userPos+2]
      password = encrypt(privateKey, userKey, mas)
      if userPassword == password:
        break
      else:
        print("Incorrect password")
        if mas == False:
          while True:
            reset = input("Reset password? [Y/N] ").upper()
            if reset == "Y":
              login(privateKey, True, "")
              userInfo[userPos+2] = encrypt(privateKey, userKey, False)
              infoUpdate("userInfo.txt", userInfo)
              print("Password reset")
            break
            
    else:
      print("User doesn't exist")
  if userInput != "MasterLogin":
    print("Welcome", userInput)
  return userInput

privateKey = 9121199

file = open("userInfo.txt")
userInfo = file.read().split(",")
file.close()
if userInfo == [""]:
  userInfo = []

while True:
  player = ["",""]
  player[0] = login(privateKey, False, "1")
  player[1] = player[0]
  while player[0] == player[1]:
    player[1] = login(privateKey, False, "2")
    if player[0] == player[1]:
      print("\n" + player[0] + " is already logged in")

  score = [0,0]
  for i in range(5):
    print("\n\nRound", str(i+1) + ":")
    score = turn(player, score)
    while score[0] == score[1]:
      score = turn(player, score)
      
  winnerScore = max(score)
  winnerPos = score.index(winnerScore)
  winner = player[winnerPos]
  print(winner, "wins!")

  file = open("leaderboard.txt")
  leaderboard = file.read().split(",")
  file.close()

  for i in range(2):
    leaderboard.append(player[i])
    leaderboard.append(score[i])

  names = []
  scores = []
  newLeaderboard = []

  for i in range(1, len(leaderboard),2):
    scores.append(int(leaderboard[i]))
    names.append(leaderboard[i-1])

  for i in range(10):
    biggest = max(scores)
    bigPos = scores.index(biggest)
    scores.remove(biggest)
    biggestName = leaderboard[bigPos]
    names.remove(biggestName)
    newLeaderboard.append(biggestName)
    newLeaderboard.append(biggest)
    print(i+1, ")", biggestName, "\t", biggest, flush = "")

    infoUpdate("leaderboard.txt", newLeaderboard)

    while True:
      again = input("Play again? [Y/N] ").upper()
      if again == "N":
        exit()
      break
