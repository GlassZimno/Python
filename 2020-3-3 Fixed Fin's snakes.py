import random
again = "yes"
def player(player, playerPosition):
        
    while input("Click enter to roll: ") != "":
        pass
    
    #Rolling dice
    diceOne = random.randint(1,6)
    diceTwo = random.randint(1,6)
    playerScore = diceOne + diceTwo
    print(player,"rolled", diceOne,"&",diceTwo)

    #I find this a kinda odd way of dealing with doubles
    #But I left it in because I tried to keep it as close to your original code as possible
    if diceOne == diceTwo:
        print(doubleMessage)
        if playerPosition < playerScore:
                playerPosition = 0
        else:
            playerScore = -playerScore
    playerPosition += playerScore
    #+=, -=, /=, *= are all very nice and easy shorthand
    if playerPosition > 49:
        playerPosition = 49
    print(player,"is on square",playerPosition)
    return playerPosition

#Set up the messages
doubleMessage = "You rolled a double, unlucky"
winMessage = ", congratulations, you won!"
welcomeMessage = "Welcome to snakes and ladders!!!!"
while again == "yes":
    print(welcomeMessage)
    #Find player amount and name
    #don't need to ask twice
    numOfPlayers = ""
    while not numOfPlayers in ["1", "2"]:
        numOfPlayers = input("How many players (1 or 2): ")
    playerOne = input("What is player 1's name: ")
    if numOfPlayers == "2":
        playerTwo = input("What is player 2's name: ")
    
    playerOnePosition = 0
    playerTwoPosition = 0
    
    while True:
        #Go through playerOne's turn and check if they've won
        playerOnePosition = player(playerOne, playerOnePosition)
        if playerOnePosition == 49:
            winner = playerOne
            break
        #Then check if there are 2 players, and do the same for playerTwo if there are
        if numOfPlayers == "2":
            playerTwoPosition = player(playerTwo, playerTwoPosition)
            if playerOnePosition == 49:
                winner = playerTwo
                break
    
    print(winner + winMessage)
    again = ""
    while not again in ["yes", "no"]:
        again = input("Do you want to play again (yes/no): ")
