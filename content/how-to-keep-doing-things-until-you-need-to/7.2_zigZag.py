newPage(200, 200)
density = 10

xx = 0
yy = height()
stroke(0)

while xx < width():
    iX = xx/density
    if iX % 2 == 0:
        nextYY = yy-height()
    else:
        nextYY = yy+height()
    nextXX = xx+density
    line((xx, yy), (nextXX, nextYY))
    yy = nextYY
    xx = nextXX