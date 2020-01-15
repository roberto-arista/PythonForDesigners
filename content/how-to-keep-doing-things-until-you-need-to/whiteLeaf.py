# Variables
step = 8
thickness = 1.25

# Instructions
newPage(200, 200)

stroke(0)
strokeWidth(thickness)

offset = 0
while offset <= width():
    line((offset, 0), (width(), offset))
    line((0, offset), (offset, height()))
    offset += step