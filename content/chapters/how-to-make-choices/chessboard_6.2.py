newPage(200, 200)
side = 20

yy = 0
while yy < height():
    iY = yy / side
    xx = 0
    while xx < width():
        iX = xx / side
        if (iX+iY) % 2 == 0:
            fill(1)
        else:
            fill(0)
        rect(xx, yy, side, side)

        xx += side        
    yy += side