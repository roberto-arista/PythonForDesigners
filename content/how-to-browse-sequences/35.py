cols = 4
rows = 4
newPage(200, 200)
cellWidth = width()/cols
cellHeight = height()/rows
for rowIndex in range(rows):
    for colIndex in range(cols):
        grayscale = (rowIndex+colIndex)/(rows+cols-2)
        fill(grayscale)
        rect(colIndex*cellWidth, rowIndex*cellHeight, cellWidth, cellHeight)
