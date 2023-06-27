#Nick Zimny
#29/9/2020
import random
import getpass
def encrypt(privateKey, userKey):
  s = getpass.getpass("Please enter a password: ")
  seed = privateKey * userKey
  output = ""
  
  for i in s:
    num = ord(i)
    num *= seed
    output += str(hex(num))
    
    seed = str(seed)
    total = 0
    for i in seed:
      total += int(i)
    length = len(seed)
    midPoint = length//2
    mid = []
    if length % 2 != 0:
      seed = seed[:midPoint] + seed[midPoint+1:]
    seed = int(seed[midPoint-3: midPoint+3]) + total
    seed **= 2
      
  return output

file = open("userInfo.txt")
userInfo = file.read().split(",")
file.close()
if userInfo == [""]:
  userInfo = []

privateKey = 9121199
def login(privateKey):
  login = False
  while True:
    userInput = input("To login, enter your username.\nTo create a new account, press [enter]\n").replace(" ","")
    if userInput == "":
      while True:
        username = input("Please enter a username: ").replace(" ","")
        if username in userInfo:
          print("That username already exists")
        else:
          file = open("availableKeys.txt")
          availableKeys = file.read().split(",")
          file.close()
          length = len(availableKeys)
          userKey = int(availableKeys[random.randint(0,length)-1])
          password = encrypt(privateKey, userKey)
          for i in [username, str(userKey), password]:
            userInfo.append(i)
          file = open("userInfo.txt","w")
          print(userInfo)
          file.write(",".join(userInfo))
          file.close()
          login = True
          break
        
    if userInput in userInfo:
      userPos = userInfo.index(userInput)
      userKey = int(userInfo[userPos+1])
      userPassword = userInfo[userPos+2]
      password = encrypt(privateKey, userKey)
      if userPassword == password:
        login = True
        break
      else:
        print("Incorrect password")
        while True:
          x = input("Reset password? [Y/N]").upper()
          if x == "Y":
            
    else:
      print("User doesn't exist")
  return login
login(privateKey)
