#Glass Zimny
#20/9/2022
nums=[]
w = {
  1 : "first",
  2 : "second",
  3 : "third",
  4 : "fourth"}

print("This program will ask for 4 numbers and add them together")
for i in range(4):
  while True:
    n = input("Please enter your " +w[i+1]+ " number: ").replace(" ","")
    if n.isnumeric():
      break
    else:
      print("This is not an integer")
  nums.append(int(n))

print("Total: "+ str(sum(nums)))
