linesAmount = 100
newPage(100, 100)
stroke(0)

factor = 1
for eachLineIndex in range(linesAmount):
    x = width()/(linesAmount+1)*(eachLineIndex+1) * factor
    line((x, 20), (x, 80))
    factor += .1