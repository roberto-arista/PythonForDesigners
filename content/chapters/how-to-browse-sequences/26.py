
linesAmount = 8
newPage(100, 100)

stroke(0)
for eachLineIndex in range(linesAmount):
    quota = width()/(linesAmount+1)*(eachLineIndex+1)
    line((20, quota), (80, quota))