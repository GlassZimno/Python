#Dominik Zimny
#20/12/2019
import math
import webbrowser as web
from mathPlus import mode

count = 0
nums = []
counter = []
save = []
userInput = ""

def mean(total, count):
    average = total/count
    return average

def help():
    print(
        "\nEnter a series of numbers,or pick an option:"+
        "\nc to clear the current numbers"+
        "\na to find average"+
        "\nme to find median"+
        "\nmo to find the smallest mode"+
        "\ns to save numbers"+
        "\nr to recover saved numbers"+
        "\ncm to clear memory"+
        "\nsh to show current numbers"+
        "\nrm to read memory"
        "\nq to quit"+
        "\nhelp to repeat this message")

help()
while userInput != "q":
    userInput = input("Enter: ")
    try:
        userInput = float(userInput)
        num = True
    except:
        num = False
    if num == True:
        nums.append(userInput)
        count += 1
        
    elif userInput == "help":
        help()
        
    elif userInput == "r":
        new = input("Would you like to start a new number set instead of adding onto existing? [y/n] ")
        if new == "y":
            nums = []
            count = 0
        file = open("averages")
        cont = file.read()
        file.close()
        b1 = cont.find("[")
        b2 = cont.find("]")
        saved = cont[b1+1:b2]
        for i in range(saved.count(",")+1):
            com = saved.find(",")
            num = saved[:com]
            saved = saved[com + 2:]
            try:
                num = float(num)
                count += int(cont[b2+1])
                nums.append(num)
            except ValueError:
                print("Memory is empty")
                userInput = ""

    elif userInput == "sh":
        if len(nums) == 0:
            print("Please enter a number first")
        else:
            print(nums)
            
    elif userInput == "cm":
        file = open("averages","w")
        file.close
        print("Memory cleared")

    elif userInput == "rm":
        file = open("averages")
        cont = file.read()
        file.close()
        b1 = cont.find("[")
        b2 = cont.find("]")
        saved = cont[b1+1:b2]
        for i in range(saved.count(",")+1):
            com = saved.find(",")
            num = saved[:com]
            saved = saved[com + 2:]
            try:
                num = float(num)
                save.append(num)
                p = True
            except ValueError:
                print("Memory is empty")
                userInput = ""
                p = False
        if p == True:
            print(save)
            
    elif len(nums) > 1:
        if userInput == "a":
            total = sum(nums)
            print(round(mean(total, count),2))
        elif userInput == "me":
            length = len(nums)
            nums.sort()
            mid = math.floor(length/2)
            if length % 2 == 0:
                mid2 = mid
                mid1 = mid - 1
                mid2 = nums[mid2]
                mid1 = nums[mid1]
                mid = mean(mid1 + mid2, 2)
            else:
                mid = nums[mid]
            print(mid)
        elif userInput == "c":
            nums = []
            count = 0
            print("cleared")
        elif userInput == "mo":
            modes = mode(nums, 3)
        elif userInput == "s":
            sure = input("Are you sure you want to overwrite the current saved numbers? [y/n] ")
            if sure == "y":
                file = open("averages","w")
                save = str(nums) + str(count)
                file.write(save)
                file.close()
                print("Saved to memory")
            else:
                userInput == ""
    
import time

print("Closing", end = "")
for i in range(3):
    x = "."
    print(x, end = "")
    time.sleep(1)
