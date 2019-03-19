newPage(200, 200)

switch = 3
factor = .5
minTck = 2
maxTck = 30

# is even
if switch % 2 == 0:
    multiplyColor = .8
    plusColor = .2
# is odd
else:
    multiplyColor = .2
    plusColor = .8

actualTck = minTck + (maxTck-minTck)*factor
strokeWidth(actualTck)
print(actualTck)

# plus
stroke(plusColor)
line((width()/2, 0), (width()/2, height()))
line((0, height()/2), (width(), height()/2))

# multiply
stroke(multiplyColor)
line((0, 0), (width(), height()))
line((0, height()), (width(), 0))
