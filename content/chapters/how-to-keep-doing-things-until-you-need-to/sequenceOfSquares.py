# Variables
side = 20

# Instructions
newPage(200, 200)

quota = height()
color = .2
while quota >= 0:
    fill(color)
    rect(0, quota, side, side)
    quota -= side

    if color == .2:
        color = .8
    else:
        color = .2