canvasSide = 100
gap = 10

size(canvasSide, canvasSide)
stroke(0)

currentPos = gap
while currentPos < canvasSide:
    line((0, currentPos), (canvasSide, currentPos))
    line((currentPos, 0), (currentPos, canvasSide))
    currentPos += gap
