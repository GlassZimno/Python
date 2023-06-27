#Dominik Zimny
#17/1/2020
square = 19
if (square / 10) % 1 == 0:
    y = square - 10
    x = 1
    y = (10 * y) - 285
    x = (50 * x) - 265
elif ((square * 100) + 285) % 1 ==0:
    y = (square // 10) * 10
    x = square - y
    print(x, y)
    y = (square * 5) - 265
    x = (square * 100) - 285

print(x, y)
