#!/usr/bin/env python3
# coding: utf-8

# ----------------- #
# Locations diagram #
# ----------------- #

# --- Modules --- #
from drawBot import stroke, strokeWidth, newPage
from drawBot import translate, width, height, line
from drawBot import text, font, fill, oval, saveImage
from drawBot import newPath, arc, drawPath, lineHeight

from getFactor import getFactor
from lerp import lerp
from findInterval import findInterval

# --- Constants --- #
POINT_SIZE = 125
WHITE = 1, 1, 1
BLACK = 0, 0, 0
RED = 1, 0, 0

# --- Objects & Methods --- #
def lineStyle(clr=BLACK, transparent=False):
    stroke(*clr)
    fill(*WHITE) if transparent is False else fill(None)
    strokeWidth(20)

def typeStyle(clr=BLACK):
    lineHeight(POINT_SIZE*1.5)
    fill(*clr)
    stroke(None)
    font('.SFNS-Regular', POINT_SIZE)


if __name__ == '__main__':
    # --- Variables --- #
    scalingFactor = 800
    steps = [1, 3, 4, 6, 8, 12]

    tickLen = 100

    rad = 40
    factor = .35

    # --- Instructions --- #
    newPage(7200, 2200)
    graphWdt = ((len(steps)-1)*scalingFactor)
    translate(width()/2 - graphWdt/2,
              height()/2 + 200)

    lineStyle()
    line((0, 0), (graphWdt, 0))

    stepsFactors = {}
    for ii, eachValue in enumerate(steps):
        xx = ii * scalingFactor

        lineStyle()
        line((xx, -tickLen/2), (xx, +tickLen/2))

        typeStyle()
        text(f'{ii/10}', (xx, -tickLen/2 - POINT_SIZE), align='center')
        stepsFactors[ii/10] = eachValue
        text(f'{eachValue}', (xx, +tickLen/2 + POINT_SIZE*.35), align='center')

    stepsInterval = findInterval(sorted(stepsFactors.keys()), factor)
    location = getFactor(*stepsInterval, factor)
    value = lerp(stepsFactors[stepsInterval[0]], stepsFactors[stepsInterval[1]], location)

    xx = factor*10 * scalingFactor
    lineStyle(clr=RED)
    oval(xx-rad, -rad, rad*2, rad*2)

    typeStyle(clr=RED)
    text(f'{factor:.2f}', (xx, -tickLen/2 - POINT_SIZE), align='center')
    text(f'{value:.0f}', (xx, +tickLen/2 + POINT_SIZE*.35), align='center')

    # arc
    lineStyle(transparent=True)
    newPath()
    xx = int(factor*10) * scalingFactor
    arc((xx + .5*scalingFactor, 150),
        scalingFactor/2, 15, 165, clockwise=False)
    drawPath()

    intervalRepr = ', '.join([f'{ff}' for ff in stepsInterval])
    expressions = [
        f'interval (bottom, top)= {intervalRepr}',
        f'location (relative to interval) = (factor − bottom) ÷  top − bottom) = ({factor:.2f} − {stepsInterval[0]}) ÷ ({stepsInterval[1]} − {stepsInterval[0]}) = {location:.2f}',
        f'value = value bottom + (value top − value bottom) × location = {stepsFactors[stepsInterval[0]]} + ({stepsFactors[stepsInterval[1]]} − {stepsFactors[stepsInterval[0]]}) × {location:.2f} = {value:.0f}',
    ]

    typeStyle()
    text('\n'.join(expressions), (-300, -500))

    saveImage('locationsDiagram.png')
