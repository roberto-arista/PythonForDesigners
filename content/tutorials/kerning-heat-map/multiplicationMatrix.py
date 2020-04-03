# Variables
cellSize = 30
value = 10

# Instructions
canvasSize = (value+2)*cellSize
newPage(canvasSize, canvasSize)
for jj in range(1, value+1):
    for ii in range(1, value+1):
        with savedState():
            translate(ii*cellSize, jj*cellSize)
            text(f'{ii*jj}', (0, 0))
