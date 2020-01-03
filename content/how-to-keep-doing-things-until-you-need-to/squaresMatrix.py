# Variables
side = 20

# Instructions
newPage(200, 200)

yy = 0
while yy < height():
    xx = 0
    while xx < width():
        fill((xx/side + yy/side) % 2)
        rect(xx, yy, side, side)
        xx += side
    yy += side
