import random
guess = [0,0,0,0]
answer = [0,0,0,0]
#Should be 1, if you get it in one try, it'll say
#you got it in 0 attempt
numOfTries = 0
#numCorrect being here makes it so that it stacks
#with every game played
numCorrect = 0

for i in range(0,4):
    answer[i] = random.randint(0,9)

print(answer)

def getGuess():
    #This means the user has to input one by one,
    #it's inconvenient 
    for i in range(0,4):
        guess[i] = input("Enter a digit from your 4 integers to play or 'quit' to end: ")
        while guess[i] != "quit":
            try:
                guess[i] = int(guess[i])
            except ValueError:
                #It doesn't check the length of the guess
                print("Not valid guess, needs to be 4 integers")
    #No need to return guess, it already alters the list
    return guess()

#getGuess doesn't give you the numCorrect
numCorrect = getGuess()
while guess != answer:
    #Can use shortcut, numOfTries += 1
    numOfTries = numOfTries + 1
    guess = getGuess()
    for i in range(0,4):
        if guess[i] == answer[i]:
            numCorrect = numCorrect + 1
    #Looks like a chunk of code is just not here
    #I'm assuming this checks if the user
    #entered correctly
            
    print("Incorrect")
    print("You got,", numCorrect,"correct")
#Not using numCorrect like you told me
#i.e. if numCorrect == 4:
#This while will just repeat this for eternity
while guess == answer:
    #Could include a check for if numOfTries is 1
    #to add an s on the end of attempt if it isn't
    print("Correct... it took you... ", numOfTries,"attempt!")
