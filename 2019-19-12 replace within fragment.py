#Dominik Zimny
#19/12/2019
s = input()
start = s[0]
end = s[-1]
change = s[1:-2]
change = change.replace("h","H")
print(start+change+end)
