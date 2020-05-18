#!/usr/bin/env python3
# coding: utf-8

# --------- #
# HSL DONUT #
# --------- #

### Modules
# std library
from colorsys import hls_to_rgb

# dependency
from drawBot import font, fill, stroke, strokeWidth, newPath, arc, drawPath
from drawBot import savedState, rotate, line, text, newPage, translate
from drawBot import width, height, newDrawing, endDrawing, saveImage, rect

### Constants
FULL_CIRCLE = 360
BLACK = 0, 0, 0

### Functions
def typeQualities(fontName='Arnold_v0.3-Regular', bodySize=9):
    # shout out to Rüdiger 👋
    font(fontName, bodySize)
    fill(*BLACK)
    stroke(None)

def lineQualities(clr=BLACK, thickness=1):
    stroke(*clr)
    strokeWidth(thickness)
    fill(None)

def hslDonut(rings, ringThickness, holeRadius, fixedValue, isLuminosityConst, captions=True):
    for angle in range(FULL_CIRCLE):
        for eachRing in range(rings):
            ringFactor = eachRing / (rings-1)
            radius = holeRadius + eachRing*ringThickness

            if isLuminosityConst:
                rgbClr = hls_to_rgb(angle/FULL_CIRCLE, fixedValue, ringFactor)
            else:
                rgbClr = hls_to_rgb(angle/FULL_CIRCLE, ringFactor, fixedValue)
            lineQualities(rgbClr, ringThickness)

            newPath()
            arc((0, 0), radius, angle-.5, angle+.5, clockwise=False)
            drawPath()

        with savedState():
            if angle % 10 == 0 and captions:
                captionRadius = radius + ringThickness
                rotate(angle)

                lineQualities(thickness=.5)
                line((captionRadius -2, 0), (captionRadius +2, 0))

                typeQualities()
                text(f'{angle}', (radius + ringThickness + 6, 0))


### Instructions
if __name__ == '__main__':
    newDrawing()
    newPage(400, 400)

    fill(.8)
    rect(0, 0, width(), height())

    translate(width()/2, height()/2)
    hslDonut(rings=8,
             ringThickness=15,
             holeRadius=45,
             fixedValue=.75,
             isLuminosityConst=False)
    saveImage('HSL Donut L.pdf')
    endDrawing()
