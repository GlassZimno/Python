#Nick Zimny
#29/9/2020
import random
import getpass
def encrypt(s, privateKey, userKey):
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

privateKey = 9121199
def login(privateKey):
  userInput = input("To login, enter your username.\nTo create a new account, press [enter] ").replace(" ","")
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
        password = encrypt(getpass.getpass("Please enter a password: "), privateKey, userKey)
        userInfo.append([username, userKey, password])
        file = open("userInfo.txt","w")
        file.write(",".join(userInfo))
        file.close()
        break
  if userInput in userInfo:
    password = input 

login(privateKey)
