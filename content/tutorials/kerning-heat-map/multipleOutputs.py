#!/usr/bin/env python3
# coding: utf-8

# ------------------------------- #
# Make multiple Kerning Heat Maps #
# ------------------------------- #

### Modules
# from the project folder
from flatKerningDefault import flatKerning
from withCaptions import kerningHeatMap, CELL_SIZE

# dependency
from fontParts.world import OpenFont
from drawBot import newDrawing, endDrawing, newPage, saveImage, translate

# std library
from string import ascii_uppercase, ascii_lowercase
from os import listdir, mkdir
from os.path import join, exists
from shutil import rmtree

### Objects, Functions, Procedures
def catchFiles(folder, extension):
    return [join(folder, nn) for nn in listdir(folder)
            if nn.endswith(extension)]

def clean(folder):
    if exists(folder):
        rmtree(folder)
    mkdir(folder)


### Instructions
if __name__ == '__main__':
    outputFolder = 'output'
    clean(outputFolder)

    fontPaths = catchFiles('fonts', '.ufo')
    glyphSets = {'uppercase': ascii_uppercase,
                 'lowercase': ascii_lowercase}

    for eachPath in fontPaths:
        thisFont = OpenFont(eachPath)

        for setName, eachSet in glyphSets.items():
            flat = flatKerning(thisFont, eachSet)
            canvasSize = CELL_SIZE * (len(eachSet) + 4)
            newDrawing()
            newPage(canvasSize, canvasSize)
            translate(CELL_SIZE*2, CELL_SIZE*2)
            kerningHeatMap(flat, eachSet, isFirstVertical=True)

            fontName = f'{thisFont.info.familyName} {thisFont.info.styleName}'
            saveImage(join(outputFolder, f'{fontName} - {setName}.pdf'))
            endDrawing()
