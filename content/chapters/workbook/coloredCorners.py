#!/usr/bin/env python3
# coding: utf-8

# --------------- #
# Colored Corners #
# --------------- #

# --- Modules --- #
from drawBot import newDrawing, newPage, saveImage, endDrawing
from drawBot import width, height, fill, oval, stroke
from drawBot import BezierPath, drawPath, strokeWidth

from math import radians, cos, sin

# --- Constants --- #
EXTREMES_LOCATIONS = {
    'lftTop': (0, 1),
    'rgtTop': (1, 1),
    'rgtBtm': (1, 0),
    'lftBtm': (0, 0)
}

# --- Objects & Methods --- #
def lerp(aa, bb, factor):
    return aa + (bb - aa) * factor

def lerpRGB(clrOne, clrTwo, factor):
    rr = lerp(clrOne[0], clrTwo[0], factor)
    gg = lerp(clrOne[1], clrTwo[1], factor)
    bb = lerp(clrOne[2], clrTwo[2], factor)
    return rr, gg, bb

def plotCorners(extremes, cornerRadius=20):
    for label, clr in extremes.items():
        loc = EXTREMES_LOCATIONS[label]
        xx, yy = width()*loc[0], height()*loc[1]
        fill(*clr)
        oval(xx-cornerRadius, yy-cornerRadius, cornerRadius*2, cornerRadius*2)

def calcColor(extremes, pt):
    xx, yy = pt
    xFactor = xx / width()
    yFactor = yy / height()
    lftClr = lerpRGB(extremes['lftBtm'], extremes['lftTop'], yFactor)
    rgtClr = lerpRGB(extremes['rgtBtm'], extremes['rgtTop'], yFactor)
    return lerpRGB(lftClr, rgtClr, xFactor)

def plotColoredCircle(center, radius, thickness, extremes, arcAngle=1):
    centerX, centerY = center
    strokeWidth(thickness)
    fill(None)

    for angle in range(0, 360, arcAngle):
        colorAngle = radians(angle+arcAngle/2)
        colorPt = centerX + cos(colorAngle)*radius, centerY + sin(colorAngle)*radius
        clr = calcColor(extremes, colorPt)

        stroke(*clr)
        bz = BezierPath()
        bz.arc(center, radius, angle, angle+arcAngle, clockwise=False)
        bz.endPath()
        drawPath(bz)


# --- Variables --- #
extremes = {
    # label : color
    'lftTop': (1, 0, 1),
    'rgtTop': (1, 1, 0),
    'rgtBtm': (1, .5, 0),
    'lftBtm': (0, 1, 1)
}

# --- Instructions --- #
if __name__ == '__main__':
    newDrawing()
    newPage(400, 400)
    plotCorners(extremes)

    for eachRadius in [60, 120, 180]:
        plotColoredCircle(center=(width()/2, height()/2), radius=eachRadius,
                          thickness=15, extremes=extremes)

    saveImage('coloredCorners.pdf')
    endDrawing()
