linesAmount = 8
radius = 3
size(100, 100)
for eachLineIndex in range(linesAmount):
    quota = width()/(linesAmount+1)*(eachLineIndex+1)
    fill(None)
    stroke(0)
    line((20, quota), (80, quota))

    stroke(None)
    fill(0)
    oval(20-radius, quota-radius, radius*2, radius*2)
    oval(80-radius, quota-radius, radius*2, radius*2)
