# Functions
def typeQualities(bodySize, leading):
    font('.SFNS-Regular', bodySize)
    lineHeight(leading)
    fill(0)
    stroke(None)
    
def lineQualities():
    stroke(0)
    fill(None)

# Variables
cellSize = 30
value = 10

# Instructions
canvasSize = (value+2)*cellSize
newPage(canvasSize*2, canvasSize)
for jj in range(1, value+1):
    for ii in range(1, value+1):
        with savedState():
            translate(ii*cellSize, jj*cellSize)

            lineQualities()
            rect(0, 0, cellSize, cellSize)

            typeQualities(8, 9)
            result = f'{ii}x{jj}\n={ii*jj}'
            textW, textH = textSize(result)
            text(result, (cellSize/2, cellSize/2+2), align='center')

translate(canvasSize, 0)
for jj in range(1, value+1):
    typeQualities(8, 9)
    text(f'{jj}', (cellSize*.75, jj*cellSize + cellSize/2-fontAscender()/2.5), align='right')

    for ii in range(1, value+1):        
        if jj == 1:
            typeQualities(8, 9)
            text(f'{ii}', ((ii+.5)*cellSize, cellSize/2), align='center')

        with savedState():
            translate(ii*cellSize, jj*cellSize)

            lineQualities()
            rect(0, 0, cellSize, cellSize)

            typeQualities(15, 15)
            result = f'{ii*jj}'
            textW, textH = textSize(result)
            text(result, (cellSize/2, cellSize/2-fontAscender()/2.5), align='center')

saveImage('multiplicationMatrix.pdf')