cols = 4
rows = 4
size(200, 200)

cellWidth = width()/cols
cellHeight = height()/rows

stroke(0)
fill(None)
for rowIndex in range(rows):
    for colIndex in range(cols):
        rect(colIndex*cellWidth, rowIndex*cellHeight, cellWidth, cellHeight)