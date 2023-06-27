#Nick Zimny
#29/9/2020
file = open("availableKeys.txt")
cont = file.read()
file.close()
print(cont)
cont = cont.replace("\t",",").replace("\n", ",")
print(cont)
file = open("availableKeys.txt", "w")
file.write(cont)
file.close()
