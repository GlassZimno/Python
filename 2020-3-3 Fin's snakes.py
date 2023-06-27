import random
again = "yes"

#Set up the messages
doubleMessage = "You rolled a double, unlucky"
winMessage = ", congratulations, you won!"
welcomeMessage = "Welcome to snakes and ladders!!!!"
while again == "yes":
    print(welcomeMessage)
    #Find player amount and name
    #don't need to ask twice
    numOfPlayers = input("How many players (1 or 2): ")
    while numOfPlayers != "1" and numOfPlayers != "2":
        numOfPlayers = input("How many players (1 or 2): ")
    numOfPlayers = int(numOfPlayers)
    if numOfPlayers == 2:
        playerOne = input("What is player 1's name: ")
        playerTwo = input("What is player 2's name: ")
    else:
        #Also don't need to ask twice
        playerOne = input("What is player 1's name: ")
    #You never use gameOver again, it can just be cut completely
    gameOver = False
    playerOnePosition = 0
    playerTwoPosition = 0
    #This could just be moved out, you're doing two checks when you could be doing one
    while gameOver == False:
        if playerOnePosition >= 49:
            playerOneWon = True
            break
        elif playerTwoPosition >= 49:
            playerTwoWon = True
            break
        #Else isn't needed, break will skip this if either check just before is True
        else:
            if numOfPlayers == 2:
                #Player 1's turn
                #The first player's turn is repeated when it doesn't need to be at all
                #The difference between playerOne's turn and playerTwo's is just variable names, so this could be a function
                #This just wasn't necassary in any way lolol
                
                #You repeat this single line 6 times
                roll = input("Click enter to roll: ")
                #It's possible and very easy to do what you're doing here with just two lines of code and no repeats
                
                if roll == "":
                    #Rolling dice
                    diceOne = random.randint(1,6)
                    diceTwo = random.randint(1,6)
                    playerScore = diceOne + diceTwo
                    print(playerOne,"rolled", diceOne,"&",diceTwo)

                    #To me, this is an odd way of dealing with doubles but it does work with almost no repetition
                    if diceOne == diceTwo:
                        print(doubleMessage)
                        if playerOnePosition < playerScore:
                                playerOnePosition = 0
                        else:
                            playerOnePosition = playerOnePosition - playerScore
                    else:
                        playerOnePosition = playerOnePosition + playerScore
                    #You repeat this again, you really don't need to
                    if playerOnePosition >= 49:
                        print(playerOne,"is on square 49")
                        playerOneWon = True
                        break
                    else:
                        print(playerOne,"is on square",playerOnePosition)
                else:
                    roll = input("Click enter to roll: ")

                #Player 2's turn
                roll = input("Click enter to roll: ")
                if roll == "":
                    diceOne = random.randint(1,6)
                    diceTwo = random.randint(1,6)
                    playerScore = diceOne + diceTwo
                    print(playerTwo,"rolled", diceOne,"&",diceTwo)
                    if diceOne == diceTwo:
                        print(doubleMessage)
                        if playerTwoPosition < playerScore:
                                playerTwoPosition = 0
                        else:
                            playerTwoPosition = playerTwoPosition - playerScore
                    else:
                        playerTwoPosition = playerTwoPosition + playerScore
                    if playerTwoPosition >= 49:
                        print(playerTwo,"is on square 49")
                        playerTwoWon = True
                        break
                    else:
                        print(playerTwo,"is on square",playerTwoPosition)
                else:
                    roll = input("Click enter to roll: ")


            #Player 1's turn
            else:
                roll = input("Click enter to roll: ")
                if roll == "":
                    diceOne = random.randint(1,6)
                    diceTwo = random.randint(1,6)
                    playerScore = diceOne + diceTwo
                    print(playerOne,"rolled", diceOne,"&",diceTwo)
                    if diceOne == diceTwo:
                        print(doubleMessage)
                        if playerOnePosition < playerScore:
                                playerOnePosition = 0
                        else:
                            playerOnePosition = playerOnePosition - playerScore
                    else:
                        playerOnePosition = playerOnePosition + playerScore
                    if playerOnePosition >= 49:
                        print(playerOne,"is on square 49")
                        playerOneWon = True
                        break
                    else:
                        print(playerOne,"is on square",playerOnePosition)
                else:
                    roll = input("Click enter to roll: ")

    #Works but the check could have been done differently to only happen once
    if playerOneWon == True:
        print(playerOne + winMessage)
    else:
        print(playerTwo + winMessage)
    again = input("Do you want to play again (yes/no): ")
    while again != "yes" and again != "no":
        again = input("Do you want to play again (yes/no): ")

#I see no holes :)
