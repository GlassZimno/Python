#Dominik Zimny
#20/1/2020
performance = [
    38, 36, 34, 32, 30, 28, 25, 22, 20, 18, 17, 16, 15, 14,
    13, 12, 12, 11, 11, 10, 10, 10, 9, 9, 9, 8, 8, 7, 7, 7, 6, 6, 6, 6, 5,
    5, 5, 4, 4, 4, 3, 3, 2, 2, 1, 1
]
sharesLeft = 100
shares = []
for i in range(46):
    share = round(sharesLeft * 0.1, 2)
    shares.append(share)
    sharesLeft *= 0.9
    print(share)

import turtle
turtle.penup()
turtle.hideturtle()
for i in range(1, 46):
    turtle.setposition( i * 3 , shares[i] * 3 )
    turtle.pendown()

sharesLeft = 100
shares2 = []
for i in range(-23, 23):
    share = (0.1 * performance[i + 23]) ** 3
    shares2.append(share)
    sharesLeft -= share
    print(share)

turtle.penup()
for i in range(1, 46):
    turtle.setposition( (i -23) * 3 , shares2[i] * 3 )
    turtle.pendown()
