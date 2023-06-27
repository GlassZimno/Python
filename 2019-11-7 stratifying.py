#Dominik Zimny
#7/11/2019
total=0
count=0
entered=""
while entered == "":
    entered=input()
    entered=entered.lower()
    if entered == "stop":
        break
    try:
        num=int(entered)
        total=total+num
        count+=1
        entered=""
    except ValueError:
        entered=""
print(total/count)


