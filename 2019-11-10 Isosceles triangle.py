#Dominik Zimny
#10/11/2019

def newinput(n):
    n=str(n)
    side = ""
    while side == "":
        side = input("\nEnter the length of side "+n+":   ")
        try:
            side = float(side)
        except ValueError:
            side = ""
    return side

loop = True
while loop == True:
    while True:
        a = newinput(1)
        b = newinput(2)
        c = newinput(3)
        if a + b < c or a + c < b or b + c < a:
            print("\nNot a valid triangle.")
            break
        else:
            if a == b or b == c or a == c:
                print("\nIsosceles.")
                break
            else:
                print("\nNot isosceles.")
                break
    while True:
        answer = input("Again? [Y/N] ")
        if answer != "":
            answer = answer[0]
        answer = answer.upper()
        if answer == "Y":
            break
        elif answer == "N":
            exit()
