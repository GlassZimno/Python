#Glass Zimny
#20/9/2022

w = {
  1 : "first",
  2 : "second",
  3 : "third"}
  
nums=[]
print("This program will ask for 3 numbers, multiply the first two"+
      "and divide the answer by the third")
for i in range(3):
  while True:
    n = input("Input your " +w[i+1]+ " number: ").replace(" ","")
    if n.isnumeric():
      nums.append(int(n))
      break
    else:
      print("That is not an integer")
print("Your answer is: "+str((nums[0]*nums[1])/nums[2]))
