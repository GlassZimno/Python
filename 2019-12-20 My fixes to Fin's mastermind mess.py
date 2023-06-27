#Dominik Zimny
#20/12/2019
import random

r = 1
answer = []
userInput = ""
numOfTries = 1

def ran():
    for i in range(4):
        answer.append(random.randint(0,9))

ran()
while userInput != "quit":
    if r == 1:
        test  = input("Testing? [yes/no] ")
        if test == "yes":
            print(answer)
    r = 0
    userInput = input("Enter your guess of a 4 digit integer to play or 'quit' to end: ")
    if userInput.isnumeric() and len(userInput) == 4:
        numCorrect = 0
        for i in range(4):
            if answer[i] == int(userInput[i]):
                numCorrect += 1
        if numCorrect == 4:
            if numOfTries != 1:
                s = "s"
            else:
                s = ""
            print("Correct... it took you... ", numOfTries,"attempt"+s+"!")
            r = 1
            answer = []
            ran()
        else:
            print("Incorrect")
            print("You got,", numCorrect,"correct")
            numOfTries += 1
    elif userInput == "quit":
        break
    else:
        print("Not valid guess, needs to be 4 integers")
