newPage(100, 100)
thickness = 5
isHorizontal = True

if isHorizontal is True:
    limit = height()
else:
    limit = width()

isBlack = True
jumpinValue = 0
while jumpinValue < limit:
    if isBlack is True:
        fill(0)
    else:
        fill(1)

    if isHorizontal is True:
        rect(0, jumpinValue, width(), thickness)
    else:
        rect(jumpinValue, 0, thickness, height())

    isBlack = not isBlack
    jumpinValue += thickness
