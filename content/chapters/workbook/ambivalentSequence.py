#!/usr/bin/env python3
# coding: utf-8

# ----------------------------------- #
# Séquences progressives ambivalentes #
# ----------------------------------- #

### Modules
from math import pi, cos, sin
from drawBot import newDrawing, endDrawing, newPage, rect
from drawBot import translate, oval, save, restore, fill, savedState
from drawBot import saveImage, width, height, frameDuration

### Constants
TWO_PI = pi*2

### Functions
def background(clr):
    fill(*clr)
    rect(0, 0, width(), height())

def projectPt(angle, radius, offset=(0, 0)):
    """angle expressed in radians"""
    xx = offset[0] + cos(angle)*radius
    yy = offset[1] + sin(angle)*radius
    return xx, yy


### Variables
rectFactor = .8
circleFactor = .4
rectRadius = 12
circleRadius = 0

distanceInFrames = 44  # frames
rectPeriod = 60        # frames
circlePeriod = 40      # frames

canvas = 1080, 1080
elements = 5, 5
margin = 40, 40

bgClr = (.9, .9, .9)
shapeClr = (0, 0, 0)

frames = 120
fps = 30

### Instructions
if __name__ == '__main__':
    newDrawing()

    netWdt = canvas[0] - margin[0]*2
    netHgt = canvas[1] - margin[1]*2
    horStep = netWdt/elements[0]
    verStep = netHgt/elements[1]
    maxIndexesSum = sum(elements)-2
    duration = 1/fps

    for eachFrame in range(frames):
        newPage(canvas[0], canvas[1])
        frameDuration(duration)

        background(bgClr)
        translate(margin[0], margin[1])

        for jj in range(elements[1]):
            for ii in range(elements[0]):

                with savedState():
                    translate((ii+.5)*horStep, (jj+.5)*verStep)
                    shiftedFrameCount = eachFrame + ((ii+jj)/maxIndexesSum)*distanceInFrames

                    save()   # 3
                    with savedState():
                        fill(*shapeClr)
                        rectX, rectY = projectPt(shiftedFrameCount/rectPeriod*TWO_PI, rectRadius)
                        rectSide = horStep*rectFactor
                        rect(rectX-rectSide/2, rectY-rectSide/2, rectSide, rectSide)
                    restore()   # 3

                    with savedState():
                        fill(*bgClr)
                        circleX, circleY = projectPt(-shiftedFrameCount/circlePeriod*TWO_PI, circleRadius)
                        circleDiameter = horStep*circleFactor
                        oval(circleX - circleDiameter/2, circleY - circleDiameter/2, circleDiameter, circleDiameter)

    saveImage('Séquences progressives ambivalentes.mp4')
    saveImage('Séquences progressives ambivalentes.gif')
    saveImage('Séquences progressives ambivalentes.pdf')
    endDrawing()
