#Dominik Zimny
#11/4/2020

p1 = input("Player one name: ")
p2 = input("Player two name: ")

pos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
possibleWins = ([0,1,2], ["3","4","5"], ["6","7","8"], ["0","3","6"],["1","4","7"], ["2","5","8"], ["0","4","8"], ["2","4","6"])
p1Owned = []
p2Owned = []
def board(pos):
    print("    "+pos[0]+"    |    "+pos[1]+"    |    "+pos[2]+"    ")
    print("-------------------")
    print("    "+pos[3]+"    |    "+pos[4]+"    |    "+pos[5]+"    ")
    print("-------------------")
    print("    "+pos[6]+"    |    "+pos[7]+"    |    "+pos[8]+"    ")

def checkWin(pos, owned):
    for i in possibleWins:
        print(i)
        print(owned)
        if i in owned:
            print("kinky bastard")
            return True
        else:
            return False

board(pos)
spacesLeft = 9
loop = True
while loop == True:
    p1loop = True
    while p1loop == True:
        move = int(input(p1+", choose a number to place your nought ")) - 1
        if move >= 0 and move < 9:
            if not pos[move] in ["O", "X"]:
                p1loop = False
            else:
                print("That space is already filled")
        else:
            print("That isn't an option")
    pos[move] = "O"
    p1Owned.append(move)
    spacesLeft -= 1
    board(pos)
    if checkWin(pos, p1Owned):
        pass
    if spacesLeft == 0:
        break
    p2loop = True
    while p2loop == True:
        move = int(input(p2+", choose a number to place your cross ")) - 1
        if move >= 0 and move < 9:
            if not pos[move] in ["O", "X"]:
                p2loop = False
            else:
                print("That space is already filled")
        else:
            print("That isn't an option")
    pos[move] = "X"
    p2Owned.append(move)
    spacesLeft -= 1
    board(pos)


