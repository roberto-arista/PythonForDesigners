#!/usr/bin/env python3
# coding: utf-8

# ----------------------- #
# Plot some random points #
# ----------------------- #

# --- Modules --- #
from statistics import mean
from random import uniform
from drawBot import oval, newPage, width
from drawBot import stroke, line, height, text
from drawBot import strokeWidth, fill, font

# --- Constants --- #
BLACK = 0, 0, 0
RED = 1, 0, 0
BLUE = 0, 0, 1

# --- Objects & Methods --- #
def lineQualities(clr=BLACK, thickness=1):
    stroke(*clr)
    strokeWidth(thickness)
    fill(None)

def shapeQualities(clr=BLACK):
    stroke(None)
    fill(*clr)

def typeQualities(fontName='SFMono-Regular', pointSize=12, clr=BLACK):
    shapeQualities(clr)
    font(fontName, pointSize)

def createRandomPoints(amount, minVal=0, maxVal=1000):
    points = []
    for ii in range(amount):
        xx = uniform(minVal, maxVal)
        yy = uniform(minVal, maxVal)
        points.append((xx, yy))
    return points

def plotPoints(points, radius=1):
    for xx, yy in points:
        oval(xx-radius, yy-radius, radius*2, radius*2)

def calcAxisMean(points, axisIndex):
    return mean([pt[axisIndex] for pt in points])


# --- Variables --- #
amount = 400

# --- Instructions --- #
if __name__ == '__main__':
    newPage(400, 400)
    randomPts = createRandomPoints(amount, 0, width())

    lineQualities(RED)
    xMean = calcAxisMean(randomPts, 0)
    line((xMean, 0), (xMean, height()))
    typeQualities(clr=RED)
    text(f'{xMean:.2f}', (xMean+4, 20))

    lineQualities(BLUE)
    yMean = calcAxisMean(randomPts, 1)
    line((0, yMean), (width(), yMean))
    typeQualities(clr=BLUE)
    text(f'{yMean:.2f}', (20, yMean+5))

    shapeQualities()
    plotPoints(randomPts)
