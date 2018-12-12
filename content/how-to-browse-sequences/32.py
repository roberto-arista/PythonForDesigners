cols = 4
size(200, 200)

cellSize = height()/cols

stroke(0)
fill(None)
for colIndex in range(cols):
    rect(colIndex*cellSize, 0*cellSize, cellSize, cellSize)