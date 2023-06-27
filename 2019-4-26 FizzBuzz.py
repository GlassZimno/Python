#26/4/2019
#identify variables a and import time function
a=0
import time
#set up loop
loop = True
while loop == True:
    #slow the program
    time.sleep(0.1)
    #add 1 every loop
    a = a + 1
    #check if divisible by both 3 and 5
    if a % 3 == 0 and a % 5 == 0:
        print ("FizzBuzz")
    #check if only divisible by 3
    elif a % 3 == 0:
        print("Fizz")
    #check if only divisible by 5
    elif a % 5 == 0:
        print("Buzz")
    else:
        print(a)
        
        
    
