# Variables
thickness = 4
coverage = .5

canvas = 200
xx = 20
yy = 20
wdt = 160
hgt = 160

# Instructions
newPage(canvas, canvas)

stroke(0)
strokeWidth(thickness)
stripes = round(wdt*coverage/thickness)-1
if stripes > 0:
    step = (wdt-thickness)/stripes
    movingX = xx + thickness/2
    while movingX <= xx+wdt:
        line((movingX, yy), (movingX, yy+hgt))
        movingX += step
