# Constants
DOTS = 3

# Variables
radius = 50

switch = False
distance = .5

# Instructions
if switch is True:
    direction = 1
else:
    direction = -1

newPage(400, 400)
stroke(0)
gap = (height()-radius*2*DOTS)/(DOTS+1)

xx = width()/2 - (width()/2 * distance) * direction
yy = gap + radius
oval(xx-radius, yy-radius, radius*2, radius*2)

xx = width()/2 + (width()/2 * distance) * direction
yy += gap + radius*2
oval(xx-radius, yy-radius, radius*2, radius*2)

xx = width()/2 - (width()/2 * distance) * direction
yy += gap + radius*2
oval(xx-radius, yy-radius, radius*2, radius*2)
