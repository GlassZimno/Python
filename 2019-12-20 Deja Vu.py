#Dominik Zimny
#20/12/2019
#Program that takes a random string and outputs
#"Deja Vu" if any character is repeated, or
#"Unique" if none repeat
s = input()
r = False
for i in range(len(s)):
    if s.count(s[i]) > 1:
        r = True
if r == True:
    print("Deja Vu")
else:
    print("Unique")
