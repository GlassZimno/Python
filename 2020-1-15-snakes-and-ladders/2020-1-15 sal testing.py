#Dominik Zimny
#15/1/2020
import math
def square(x, y):
    x = abs(x / 50)
    y = abs(y / 50)
    if math.floor(y) % 2  != 0:
        x = math.ceil(x)
        y = math.ceil(y)
    else:
        x = math.floor(x)
        y = math.floor(y)
    return x * y

print(square(-215, -135))