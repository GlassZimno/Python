#Dominik Zimny
#30/11/2019
import random

#Define a function to give a certain number of cards to the player or computer
def giveCard(player, amount):
    for i in range(0, amount):
        player.append(randCard())
    return player

def randCard():
    card = cards[random.randint(0, len(cards) - 1)]
    return card

def findColour(card):
    #Go through the word until a space appears to find the colour of the card
    for i in range(0, len(card)):
        if card[i] == " ":
            space = i
            colour = card[0:space]
            break
    return colour

def cardPlace(topCard, player, cardChosen, opponent):
    if opponent == "computer":
        opponent = computerCards
    else:
        opponent = playerCards
    if cardChosen == "new":
        player = giveCard(player, 1)
    else:
        print(cardChosen)
        cardChosen = player[int(cardChosen) - 1]
        #Test if card chosen can be placed
        if findColour(topCard) == findColour(cardChosen) or topCard[-1] == cardChosen[-1]:
            if "plus" in cardChosen:
                add = cardChosen[-1]
                opponent = giveCard(opponent, int(add))
            elif cardChosen[-4:len(cardChosen)] == "skip":
                print("skip")
            topCard = cardChosen
            player.remove(cardChosen)
    return topCard
    
#Define arrays
cards = ["switch"]
colours = ["green ", "red ", "blue ", "yellow "]
playerCards = []
computerCards = []

#Generate possible cards to save time and space in the program
for i in range(0,4):
    for j in range(2, 10):
        card = colours[i] + str(j)
        cards.append(card)
    for k in range(2, 6, 2):
        card = colours[i] + "plus " + str(k)
        cards.append(card)
    card = colours[i] + "skip"
    cards.append(card)

#Generate 5 cards for the player and computer
playerCards = giveCard(playerCards, 5)
computerCards = giveCard(computerCards, 5)

#Pick a random card to begin the game with
topCard = randCard()
topCard = "blue 3"

playerCards.append("blue skip")

loop = True
while loop == True:
    print(topCard)
    #Let the player pick a card
    for i in range(0, len(playerCards)):
        print(i + 1,"\t", playerCards[i])
    cardChosen = input("Pick the number of the card you want to place, or \"new\" to get a card from the deck: ")

    topCard = cardPlace(topCard, playerCards, cardChosen, computerCards)
    print(topCard)

    cardChosen = random.randint(0, len(computerCards) -1)

    topCard = cardPlace(topCard, computerCards, cardChosen, playerCards)

