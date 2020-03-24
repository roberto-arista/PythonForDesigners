factor = .5
switch = True

newPage(100, 100)

if switch is False:
    background = 0
    figure = 1
else:
    background = 1
    figure = 0

fill(background)
rect(0, 0, width(), height())

radius = (height()/4 + height()/2 * factor)/2

fill(figure)
oval(width()/2-radius, height()/2-radius,
     radius*2, radius*2)
