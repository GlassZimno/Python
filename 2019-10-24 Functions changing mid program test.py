#Dominik Zimny
#24/10/2019
#Test to see if functions can change mid-program
def sev(num):
    num=num*7
    return num

number=sev(10)
print(number)

def sev(num):
    num=num-7
    return num

number=sev(10)
print(number)

#Conclusion: Yes, you can
