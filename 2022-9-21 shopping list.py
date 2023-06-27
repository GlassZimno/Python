#Glass Zimny
#21/9/2022

l = []
print("This program will create a shopping list and read it back"+
      "until you enter an empty item")
i=0
while True:
  i += 1
  s = input("Item "+str(i)+": ")
  if s == "":
    break
  l.append(s)

print("Shopping list: "+", ".join(l))
