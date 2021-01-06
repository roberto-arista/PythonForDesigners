#!/usr/bin/env python3

##############
# Protractor #
##############

### Modules
from math import degrees
from drawBot import font, fontSize, fill, strokeWidth, stroke
from drawBot import newPage, translate, width, height
from drawBot import oval, savedState, text, line, drawPath
from drawBot import rotate, blendMode, newPath, arc, openTypeFeatures
from fractions import Fraction

### Constants
FULL_CIRCLE = 360
BLACK = (0, 0, 0)
RED = (1, 0, 0)

MARGIN = 10

TICKS = {
    'large': {
        'width': 20,
        'thickness': 1,
    },
    'medium': {
        'width': 10,
        'thickness': .5,
    },
    'small': {
        'width': 5,
        'thickness': .5,
    }
}

### Functions & Procedures
def textAttributes():
    fill(*BLACK)
    stroke(None)
    font('.SFNS-Regular')
    fontSize(10)

def shapeAttributes(fillColor=None, strokeColor=None, thickness=1):
    if fillColor is None:
        fill(None)
    else:
        fill(*fillColor)

    if strokeColor is None:
        stroke(None)
    else:
        strokeWidth(thickness)
        stroke(*strokeColor)


### Variables
protractorRadius = 200

### Instructions
if __name__ == '__main__':
    newPage(600, 600)
    translate(width()/2, height()/2)

    # field
    shapeAttributes(strokeColor=BLACK, thickness=4)
    oval(-protractorRadius, -protractorRadius,
         protractorRadius*2, protractorRadius*2)

    # degrees
    with savedState():
        for eachAngle in range(FULL_CIRCLE):
            for eachPolarity in [-1, +1]:
                # long tick, degrees
                if (eachAngle % 10 == 0 and eachPolarity == -1) or \
                   (eachAngle % 15 == 0 and eachPolarity == 1):
                    key = 'large'
                    # caption
                    textAttributes()
                    alignment = 'right' if eachPolarity == -1 else 'left'
                    txt = f'{eachAngle}°' if eachPolarity == -1 else f'{Fraction(eachAngle*2, FULL_CIRCLE)} π'
                    openTypeFeatures(frac=True) if '/' in txt else openTypeFeatures(frac=False)
                    text(txt, (protractorRadius+(MARGIN*1.5+TICKS[key]['width'])*eachPolarity, 0),
                         align=alignment)

                # medium tick
                elif eachAngle % 5 == 0:
                    key = 'medium'

                # short tick
                else:
                    key = 'small'

                shapeAttributes(strokeColor=BLACK, thickness=TICKS[key]['thickness'])
                line((protractorRadius+MARGIN*eachPolarity, 0),
                     (protractorRadius+(MARGIN+TICKS[key]['width'])*eachPolarity, 0))
            rotate(1)

    # drawing 1 red radian
    blendMode('multiply')
    shapeAttributes(strokeColor=RED, thickness=8)
    line((0, 0), (protractorRadius, 0))

    newPath()
    arc((0, 0), protractorRadius, 0, degrees(1), clockwise=False)
    drawPath()
