#Dominik Zimny
#18/1/2020
import turtle
import time
def findSquare(square):
    x = (square - 1) % 10
    y = (square - 1) // 10
    x *= 50
    y *= 50
    if y % 20 == 0 and y != 0:
        x -= 215
        y -= 235
        look = "left"
    else:
        x = 235 - x
        y = y - 235
        look = "right"
    return [x, y, look]


    
def slide(player, end):
    time.sleep(0.5)
    player.speed(8)
    end = findSquare(end)
    endX = end[0]
    endY = end[1]
    look = end[2]
    player.goto(endX, endY)
    return look

look = slide(turtle, 7)