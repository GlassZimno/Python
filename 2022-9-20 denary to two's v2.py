#Glass Zimny
#20/9/2022

while True:
  print("Would you like to:\n1: Convert two's compliment to denary"+
        "\n2: Convert signed denary to two's compliment")
  c = input()
  while c == "1":
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
    break
  
  while c == "2":
    while True:
      num = input("Input a signed integer x, where -129 < x < 128: ").replace(" ","")
      if num == "0":
        num = "+0"
      if num != "":
        if num[0] == "-" or num[0] == "+":
          if num[1:].isnumeric():
            rem=int(num[1:])
            num=int(num)
            if num <= 127 and num >= -128:
              break
            else:
              print("Number not within the correct range")
          else:
            print("This is not an integer")
        else:
          print("Entry is missing a sign at the beginning i.e. + or -")
      else:
        print("Please enter your integer")
        
    if num<0:
      dif=num+128
      total="1"
      for i in range(7):
        i = 6-i
        if dif >= 2**i:
          dif = dif % 2**i
          total += "1"
        else:
          total += "0"
    else:
      total = ""
      for i in range(8):
        i = 7-i
        if rem >= 2**i:
          rem = rem % 2**i
          total += "1"
        else:
          total += "0"
        
    print(total)
    break
  if not c in ["1","2"]:
    print("this is not a valid option")






        
