#Dominik Zimny
#17/1/2020
cell = 7
x = (cell - 1) % 10
y = (cell - 1) // 10
x *= 50
y *= 50
if y % 20 == 0:
    x -= 215
    y -= 235
    look = "right"
else:
    x = 235 - x
    y = y - 235
    look = "left"
print(x, y, look)
