#Glass Zimny
#20/9/2022

while True:
  while True:
    num = input("Input 8-bit two's compliment binary number: ").replace(" ","")
    if len(num) == 8:
      if num.replace("1","").replace("0","") == "":
        break
      else:
        print("This is not a binary number")
    else:
      print("Entry is not 8 characters long")

  num = num.replace("1","p").replace("0","1").replace("p","0")[::-1]
  total = 0

  for i in range(8):
    total += (2**i)*int(num[i])
  total += 1
  print("Denary: -"+str(total))
