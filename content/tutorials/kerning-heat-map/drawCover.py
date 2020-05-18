from flatKerningDefault import flatKerning
from kerningHeatMap import kerningHeatMap, CELL_SIZE
from fontParts.world import OpenFont
from string import ascii_uppercase, ascii_lowercase

if __name__ == '__main__':
    ### Variables
    fontName = 'Source Serif Pro Regular.ufo'

    ### Instructions
    thisFont = OpenFont(fontName)
    flat = flatKerning(thisFont)

    canvasSize = (len(ascii_lowercase)+4)*CELL_SIZE
    newPage(canvasSize*2, canvasSize)
    fill(.8)
    rect(0, 0, width(), height())

    translate(CELL_SIZE*2, CELL_SIZE*2)
    kerningHeatMap(flat, ascii_uppercase, isFirstVertical=True)
    
    translate((len(ascii_lowercase)+4)*CELL_SIZE, 0)
    kerningHeatMap(flat, ascii_lowercase, isFirstVertical=True)
    
    saveImage('visual-abstract.pdf')