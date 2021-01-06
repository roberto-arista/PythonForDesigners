#!/usr/bin/env python3

# ---------- #
# Axonometry #
# ---------- #

### Modules
# dependencies
from drawBot import newPage, width, height, translate
from drawBot import save, restore, scale, saveImage
from drawBot import newDrawing, endDrawing, savedState

# from the project folder
from HSLdonut import hslDonut

### Variables
discs = 16
rings = 22
ringThickness = 5
holeRadius = 45

### Instructions
if __name__ == '__main__':
    newDrawing()
    newPage(952, 488)

    translate(width()*.27, height()*.25)
    save()
    for eachDisc in range(discs):
        with savedState():
            scale(1, .65)
            hslDonut(rings,
                     ringThickness,
                     holeRadius,
                     fixedValue=eachDisc/(discs-1),
                     isLuminosityConst=True,
                     captions=False)
        translate(0, 16)
    restore()

    translate(width()*.44, 0)
    save()
    for eachDisc in range(discs):
        with savedState():
            scale(1, .65)
            hslDonut(rings,
                     ringThickness,
                     holeRadius,
                     fixedValue=eachDisc/(discs-1),
                     isLuminosityConst=True,
                     captions=False)
        translate(0, 16)
    restore()

    saveImage('cd-roms.pdf')
    endDrawing()
