### Modules
from flatKerning import flatKerning
from fontParts.world import OpenFont

### Constants
CELL_SIZE = 30

### Functions
def typeQualities():
    font('Obviously-NarwSemi', 18)
    fill(0)
    stroke(None)

def drawLettersMatrix(glyphNames, kerning, isFirstVertical):
    for jj, glyphY in enumerate(glyphNames):
        for ii, glyphX in enumerate(glyphNames):
            pair = (glyphY, glyphX) if isFirstVertical else (glyphX, glyphY)

            with savedState():
                typeQualities()
                translate((ii+.5)*CELL_SIZE, jj*CELL_SIZE)
                text(f'{kerning[pair]}', (0, 0), align='center')


if __name__ == '__main__':

    ### Variables
    glyphNames = 'ABCDE'

    ### Instructions
    myFont = OpenFont('Source Serif Pro Regular.ufo')
    flatK = flatKerning(myFont)

    newPage(400, 250)
    translate(CELL_SIZE*1, CELL_SIZE*2)
    drawLettersMatrix(glyphNames, flatK, isFirstVertical=True)

    translate(CELL_SIZE*6, 0)
    drawLettersMatrix(glyphNames, flatK, isFirstVertical=False)
