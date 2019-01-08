rows = 4
newPage(200, 200)

cellSize = height()/rows

stroke(0)
fill(None)
for rowIndex in range(rows):
    rect(0*cellSize, rowIndex*cellSize, cellSize, cellSize)