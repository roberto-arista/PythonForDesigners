cols = 4
rows = 4
size(200, 200)

cellWidth = width()/cols
cellHeight = height()/rows

for rowIndex in range(rows):
    for colIndex in range(cols):
        x = colIndex*cellWidth
        y = rowIndex*cellHeight

        stroke(None)
        fill(0)
        text('{}, {}'.format(colIndex, rowIndex), (x+5, y+5))

        fill(None)
        stroke(0)
        rect(x, y, cellWidth, cellHeight)