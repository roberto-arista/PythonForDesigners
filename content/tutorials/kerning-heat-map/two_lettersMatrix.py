### Constants
CELL_SIZE = 30

### Functions
def typeQualities():
    font('.SFNS-Regular', 8)
    fill(0)
    stroke(None)


if __name__ == '__main__':

    ### Variables
    glyphNames = 'ABCDE'
    isFirstVertical = True

    ### Instructions
    newPage(400, 400)
    translate(CELL_SIZE*2, CELL_SIZE*2)
    for jj, glyphY in enumerate(glyphNames):
        for ii, glyphX in enumerate(glyphNames):
            pair = (glyphY, glyphX) if isFirstVertical else (glyphX, glyphY)

            with savedState():
                translate(ii*CELL_SIZE, jj*CELL_SIZE)
                text(f'{pair[0]}{pair[1]}', (0, 0))
