#Dominik Zimny
#2019/10/24
#number to currency
def pnd(price):
        pounds=price//1
        pence=price-pounds
        pence=round(pence,2)
        pence=str(pence)
        pence=float(pence)
        pence=pence*100
        pence=int(pence)
        if pence==0:
                pence="00"
        pence=str(pence)
        pounds=int(pounds)
        pounds=str(pounds)
        price="£"+pounds+"."+pence
        return price
loop=True
while loop==True:
        loop2=True
        price=0
        while price<1:
                price=input()
                try:
                        price=float(price)
                except ValueError:
                        price=0
        totalCost=pnd(price)
        print(totalCost)
        while loop2==True:
                answer=input("Again? [Y/N] ")
                if answer != "":
                        answer=answer[0]
                answer=answer.upper()
                if answer=="Y":
                        loop2=False
                elif answer=="N":
                        loop=False
                        loop2=False
