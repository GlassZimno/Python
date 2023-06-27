#Dominik Zimny
#2019/10/24
#number to currency
def pnd(price):
        while price < 1:
                price=input("\n")
                try:
                        price=float(price)
                except ValueError:
                        price=0
        if price!=0:
                price=f'£{price:.2f}'
        return price

while True:
        price=0
        totalCost = pnd(price)
        print(totalCost)
        answer=""
        while True:
                answer=input("\nAgain? [Y/N] ").upper()
                if answer == "Y":
                        break
                elif answer == "N":
                        exit()
                                
