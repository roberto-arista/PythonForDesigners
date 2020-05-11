newPage(200, 200)

factor = .5
minTck = 2
maxTck = 30

actualTck = minTck + (maxTck-minTck)*factor
strokeWidth(actualTck)

# plus
stroke(.2)
line((width()/2, 0), (width()/2, height()))
line((0, height()/2), (width(), height()/2))

# multiply
stroke(.8)
line((0, 0), (width(), height()))
line((0, height()), (width(), 0))
