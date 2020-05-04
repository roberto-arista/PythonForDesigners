### Modules
from fontParts.world import OpenFont
from flatKerningDefault import flatKerning
from string import ascii_uppercase

### Constants
CELL_SIZE = 30

WHITE = 1, 1, 1
BLACK = 0, 0, 0

RED = 1, 0, 0
GREEN = 0, 1, 0

### Functions
def typeQualities(clr=BLACK, bodySize=8, leading=9, fontName=None):
    if fontName is None:
        font('Obviously-NarwSemi', bodySize)
    else:
        font(fontName, bodySize)
    lineHeight(leading)
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
    glyphNames = 'AVRT'

    ### Instructions
    thisFont = OpenFont(fontName)
    flat = flatKerning(thisFont)

    # small heat map
    canvasSize = (len(glyphNames)+2)*CELL_SIZE
    newPage(canvasSize, canvasSize)
    with savedState():
        translate(CELL_SIZE, CELL_SIZE*1.4)
        kerningHeatMap(flat, glyphNames, isFirstVertical=True)
