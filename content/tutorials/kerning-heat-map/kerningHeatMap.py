### Modules
# from project folder
from flatKerningDefault import flatKerning

# dependencies
from drawBot import font, fill, stroke
from drawBot import savedState, translate
from drawBot import text, rect, textSize, newPage
from fontParts.world import OpenFont

# from std library
from itertools import product
from string import ascii_uppercase

### Constants
CELL_SIZE = 30

WHITE = 1, 1, 1
BLACK = 0, 0, 0

RED = 1, 0, 0
GREEN = 0, 1, 0

### Functions
def lerp(aa, bb, factor):
    return aa + (bb-aa) * factor

def lerpRGB(colorOne, colorTwo, factor):
    rr = lerp(colorOne[0], colorTwo[0], factor)
    gg = lerp(colorOne[1], colorTwo[1], factor)
    bb = lerp(colorOne[2], colorTwo[2], factor)
    return rr, gg, bb

def typeQualities(clr=BLACK):
    font('Obviously-NarwSemi', 18)
    shapeQualities(clr)

def shapeQualities(clr=BLACK):
    fill(*clr)
    stroke(None)

def kerningHeatMap(kerning, glyphNames, isFirstVertical):
    corrections = [kerning[pair]
                   for pair in product(glyphNames, repeat=2)]
    corrections.sort()
    minCorrection, maxCorrection = abs(corrections[0]), abs(corrections[-1])
    if minCorrection < maxCorrection:
        reference = maxCorrection
    else:
        reference = minCorrection

    for jj, glyphY in enumerate(glyphNames):

        # vertical captions
        with savedState():
            translate(-CELL_SIZE, jj*CELL_SIZE)
            typeQualities()
            text(f'{glyphY}', (CELL_SIZE*.5, CELL_SIZE*.2),
                 align='center')

        # drawing the row
        for ii, glyphX in enumerate(glyphNames):
            pair = (glyphY, glyphX) if isFirstVertical else (glyphX, glyphY)
            correction = kerning[pair]

            with savedState():
                translate(ii*CELL_SIZE, jj*CELL_SIZE)

                # horizontal captions
                if jj == 0:
                    typeQualities()
                    text(f'{glyphX}', (CELL_SIZE*.5, -CELL_SIZE*.8),
                         align='center')

                # draw the cells
                factor = .5 + .5 * abs(correction)/reference
                if correction == 0:
                    rectClr = BLACK
                    typeClr = WHITE
                elif correction < 0:
                    rectClr = lerpRGB(WHITE, RED, factor)
                    typeClr = WHITE
                else:
                    rectClr = lerpRGB(WHITE, GREEN, factor)
                    typeClr = BLACK
                shapeQualities(rectClr)
                rect(0, 0, CELL_SIZE, CELL_SIZE)

                if correction != 0:
                    corrStr = f'{abs(correction)}'

                    # just a check for body size
                    if textSize(corrStr)[0] > CELL_SIZE:
                        print(f'[WARNING] {pair} text is too big!')

                    typeQualities(clr=typeClr)
                    text(corrStr, (CELL_SIZE*.5, CELL_SIZE*.2), align='center')


if __name__ == '__main__':
    ### Variables
    fontName = 'Source Serif Pro Regular.ufo'
    glyphNames = ascii_uppercase

    ### Instructions
    thisFont = OpenFont(fontName)
    flat = flatKerning(thisFont)

    canvasSize = (len(glyphNames)+4)*CELL_SIZE
    newPage(canvasSize, canvasSize)
    translate(CELL_SIZE*2, CELL_SIZE*2)
    kerningHeatMap(flat, glyphNames, isFirstVertical=True)
