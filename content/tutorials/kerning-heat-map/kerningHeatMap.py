### Modules
from fontParts.world import OpenFont
from flatKerning2 import flatKerning
from string import ascii_uppercase

### Constants
CELL_SIZE = 30

WHITE = 1, 1, 1
BLACK = 0, 0, 0

RED = 1, 0, 0
GREEN = 0, 1, 0

### Functions
def typeQualities(clr=BLACK):
    font('Obviously-NarwSemi', 8)
    lineHeight(9)
    shapeQualities(clr)

def shapeQualities(clr=BLACK):
    fill(*clr)
    stroke(None)

def kerningHeatMap(kerning, glyphNames, isFirstVertical):
    for jj, glyphY in enumerate(glyphNames):
        for ii, glyphX in enumerate(glyphNames):
            pair = (glyphY, glyphX) if isFirstVertical else (glyphX, glyphY)
            correction = kerning[pair]

            with savedState():
                translate(ii*CELL_SIZE, jj*CELL_SIZE)

                if correction == 0:
                    shapeQualities(BLACK)
                elif correction < 0:
                    shapeQualities(RED)
                else:
                    shapeQualities(GREEN)
                rect(0, 0, CELL_SIZE, CELL_SIZE)

                typeQualities(clr=WHITE)
                text(f'{pair[0]}, {pair[1]}\n{correction}',
                     (CELL_SIZE*.1, CELL_SIZE*.5))


if __name__ == '__main__':
    ### Variables
    fontName = 'Source Serif Pro Regular.ufo'
    glyphNames = ascii_uppercase

    ### Instructions
    thisFont = OpenFont(fontName)
    flat = flatKerning(thisFont, glyphSet=glyphNames)

    newPage(1000, 1000)
    translate(CELL_SIZE*2, CELL_SIZE*2)
    kerningHeatMap(flat, glyphNames, isFirstVertical=True)
