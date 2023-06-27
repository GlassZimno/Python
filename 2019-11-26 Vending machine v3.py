#Glass Zimny
#26/11/2019

def money(total):
    #Total is currently in pence form
    total = str(total)
    #If the length is 1 or 2, keep it as such, but add pence on the end
    if len(total) < 3:
        total = total + " pence"
       
    #If not, divide by 100 and add £ at the beginning
    else:
        total = int(total) / 100
        total = "£" + str(total)
       
    #E.g. 1 = "1 pence", 12 = "12 pence", 123 = "£1.23"
    return total

#The money function is used but doesn't need to print each time
#But it does get printed more than once, so this function reduces repetition
def totalprint(total):
    #Call the money function and display it
    total = money(total)
    print("\nThe total is " + total)

def clear():
    #Go through each slot in the coins array and set it to zero
    for i in range(0, 10):
        coins[i] = 0
       
    return coins

#Set arrays
coins = [0,0,0,0,0,0,0,0,0,0]
real = (1,2,5,10,20,50,100,200)

#Create main loop and tell the user their options
loop = True
print("\n\tVending machine")
while loop == True:
    print("\nWhat would you like to do?")
    print("1.  Clear,  clears memory")
    print("2.  New,   lets you enter new coins")
    print("3.  Show,  display memory")
    print("4.  End,  exit program\n")
    do = input("Enter number or command word: ")
   
    while do == "clear" or do == "1":
        #Call on the clear function
        clear()
        #Notify the user that the action is complete
        print("\nSlots cleared")
        do = ""
       
    while do == "new" or do == "2":
        i = 0
        total = 0
        #Call the clear function to reset to 0 to be able to accept new entries
        clear()
        print("\nEnter 10 coins, or \"stop\" when you're done")
        while i in range(0, 10):
            #x will be 0 until the user says to stop
            x = 0
            #Repeat until the entry is in the real array
            while not coins[i] in real:
                #Let the user enter the coin value
                coins[i] = input("Enter coin "+ str(i + 1) +"\t")
                #Lower case to match if statement
                coins[i] = coins[i].lower()
                if coins[i] == "stop":
                    x = 1
                    #Ends the loop now and moves out of it
                    break
               
                #Checks to see if what is entered is a number, if not, it will ask the user again
                try:
                    coins[i] = int(coins[i])
                   
                except ValueError:
                    coins[i] = ""
                   
            #This makes it so that if stop is entered, it does not try to add it to the total
            if x != 1:
                total += coins[i]
                i += 1
               
            else:
                i = 11
               
        #Return the total back to the user
        totalprint(total)
        do = ""
       
    while do == "show" or do == "3":
        total = 0
        #Go through each number in the array and print it on a new line
        for i in range(0, 10):
            print("Slot " + str(i + 1) +":\t" + money(coins[i]))
            total += coins[i]
           
        #Tell the user the total after showing each indicidual coin
        totalprint(total)
        do = ""
       
    while do == "end" or do == "4":
        #Kill the program
        exit()
