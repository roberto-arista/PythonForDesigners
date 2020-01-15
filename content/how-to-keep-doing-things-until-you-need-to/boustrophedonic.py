# Constants
MARGIN = 100

# Variables
step = 50
baseRadius = 5
radiusIncrement = 2

# Instructions
colors = [.2, .8]

newPage(500, 500)

xx = MARGIN
yy = MARGIN
direction = 1
ii = 0
radius = baseRadius

while (MARGIN <= xx <= width()-MARGIN) and (MARGIN <= yy <= height()-MARGIN):
    fill(colors[ii % 2])

    radius += radiusIncrement
    oval(xx-radius, yy-radius, radius*2, radius*2)
    xx += step * direction

    if xx < MARGIN or xx > width()-MARGIN:
        radius = baseRadius
        direction *= -1
        xx += step * direction
        yy += step

    ii += 1
