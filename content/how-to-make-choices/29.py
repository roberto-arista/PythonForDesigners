newPage(200, 200)
factor = .5
blackOnWhite = False

if blackOnWhite is True:
    backgroundColor = 1
    circleColor = 0
else:
    backgroundColor = 0
    circleColor = 1

fill(backgroundColor)
rect(0, 0, width(), height())

fill(circleColor)
radius = (width()/4 + width()/2*factor)/2
oval(width()/2-radius, height()/2-radius, radius*2, radius*2)