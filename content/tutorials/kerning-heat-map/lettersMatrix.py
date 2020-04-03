### Constants
CELL_SIZE = 30

### Variables
glyphNames = 'ABCDE'

### Instructions
canvasSize = (len(glyphNames)+2) * CELL_SIZE
newPage(canvasSize, canvasSize)
translate(CELL_SIZE, CELL_SIZE)
for jj, glyphY in enumerate(glyphNames):
    for ii, glyphX in enumerate(glyphNames):
        with savedState():
            translate(ii*CELL_SIZE, jj*CELL_SIZE)
            font('.SFNS-Regular', 18)
            fill(0)
            stroke(None)
            text(f'{glyphX}{glyphY}', (0, CELL_SIZE*.3))
