#Dominik Zimny
#11/11/2019
total=0
coins = [1,1,1,1,1,1,1,1,1,1]
for i in range (0,10):
    coins[i] = 0
print("Enter values in pence, enter 'stop' when you're done")
for i in range (0,10):
    while coins[i] == 0:
        coins[i] = input("Enter value "+str(i+1)  + " ")
        coins[i] = coins[i].lower()
        if coins[i] == "stop":
            break
        try:
            coins[i] = float(coins[i])
            total = total + coins[i]
            break
        except ValueError:
            coins[i] = 0
print(f'£{total:.2f}')
