cols = 4
rows = 4
size(200, 200)
cellWidth = width()/cols
cellHeight = height()/rows
for rowIndex in range(rows):
    for colIndex in range(cols):
        if (rowIndex+colIndex) % 2 == 0:
            fill(0)
        else:
            fill(1)
        rect(colIndex*cellWidth, rowIndex*cellHeight, cellWidth, cellHeight)