#Dominik Zimny
#19/11/2019
def newint(inp):
    try:
        inp = int(inp)
    except ValueError:
        inp = ""
    return inp

again = "y"
while again == "y":
    digits = ""
    aim = ""
    count = 0
    while digits == "":
        digits = newint(input("How many digits are there? "))
    while aim == "":
        aim = newint(input("What is the target sum? "))
    length = 10**digits
    for i in range(0, length):
        total = 0
        length=str(length)
        i = str(i)
        extra = len(length) - len(i) - 1
        extra = extra * "0"
        num = extra + i
        for x in range(0, len(num)):
            total = total + int(num[x])
        if aim == total:
            count = count + 1
            print(count ,")\t", num)
    again = ""
    while again != "y" and again != "n":
        again = input("Go again? [y/n] ")
        again = again.lower()
        if again != "":
            again = again[0]
exit()
      
