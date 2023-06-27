#Dominik Zimny
#2019/10/24
#number to currency
def pnd(num):
    if num % 1 != 0:
        pence=num%1
        pence=round(pence,2)
        pence=str(pence)
        pence1=pence[2]
        length=len(pence)
        if length >2:
            pence2=pence[3]
            pence=pence1+pence2
        elif length<2:
            pence1=int(pence)
            pence1=pence1*10
    pounds=price//1
    pounds=int(pounds)
    pounds=str(pounds)
    pence=str(pence)
    price="£"+pounds+"."+pence
    return price

totalPrice=float(input())
totalPrice=pnd(totalPrice)
print(totalPrice)


