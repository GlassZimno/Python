import random
guess = [0,0,0,0]
answer = [0,0,0,0]
numOfTries = 0
numCorrect = 0

for i in range(0,4):
    answer[i] = random.randint(0,9)
    
print(answer)

def getGuess():
    for i in range(0,4):
        guess[i] = input("Enter a digit from your 4 integers to play or 'quit' to end: ")
        while guess[i] != "quit":
            try:
                guess[i] = int(guess[i])
            except ValueError:
                print("Not valid guess, needs to be 4 integers")
    return guess()

numCorrect = getGuess()
while guess != answer:
    numOfTries = numOfTries + 1
    guess = getGuess()
    for i in range(0,4):
        if guess[i] == answer[i]:
            numCorrect = numCorrect + 1
            
    print("Incorrect")
    print("You got,", numCorrect,"correct")
while guess == answer:
    print("Correct... it took you... ", numOfTries,"attempt!")
