#!/usr/bin/env python3
# coding: utf-8

# ------------- #
# Article Cover #
# ------------- #

# --- Modules --- #
import drawBot as dB
from varWaterfallPoster import drawWaterFallPoster, pointSize, leading

# --- Constants --- #
WHITE = 1, 1, 1
GRAY = .7, .7, .7

# --- Functions --- #
def background(clr):
    dB.fill(*clr)
    dB.rect(0, 0, dB.width(), dB.height())

def generateSourcePosters(fontName, imagePath, language, axisSteps,
                          waterFallAxisName, fixedAxes, iterations=1):
    dictName = f'{language}.txt'

    dB.newDrawing()
    for ii in range(iterations):
        dB.newPage('A3')
        drawWaterFallPoster(fontName, dictName, pointSize, leading,
                            axisSteps, waterFallAxisName, fixedAxes)
    dB.saveImage(imagePath)
    dB.endDrawing()

def generateCover(horElems, verElems, scalingFactor, inputPath, outputPath, margin=250):
    dB.newDrawing()
    dB.newPage(7200, 3600)
    background(GRAY)

    horStep = (dB.width() - margin*2) / horElems
    verStep = (dB.height() - margin*2) / verElems
    dB.translate(margin+horStep/2, margin+verStep/2)

    for jj in range(verElems):
        dB.save()
        for ii in range(horElems):
            with dB.savedState():
                imgWdt, imgHgt = dB.imageSize(inputPath)
                dB.scale(scalingFactor)
                dB.fill(*WHITE)
                dB.rect(-imgWdt/2, -imgHgt/2, imgWdt, imgHgt)
                dB.image(inputPath, (-imgWdt/2, -imgHgt/2), pageNumber=horElems*jj+ii+1)
            dB.translate(horStep, 0)
        dB.restore()
        dB.translate(0, verStep)

    dB.saveImage(outputPath)
    dB.endDrawing()

def combinePDF(inputs, outputPath):
    dB.newDrawing()
    for eachInputFile in inputs:
        imgWdt, imgHgt = dB.imageSize(eachInputFile)
        dB.newPage(imgWdt, imgHgt)
        dB.image(eachInputFile, (0, 0), pageNumber=1)
    dB.saveImage(outputPath)
    dB.endDrawing()


# --- Instructions --- #
if __name__ == '__main__':
    # front cover
    generateSourcePosters(fontName='Skia',
                          imagePath='coverPosters.pdf',
                          language='italian',
                          axisSteps=7,
                          waterFallAxisName='wght',
                          fixedAxes={'wdth': 1.5},
                          iterations=28)
    generateCover(horElems=8,
                  verElems=3,
                  scalingFactor=.75,
                  inputPath='coverPosters.pdf',
                  outputPath='visual-abstract.png')

    # back cover
    generateSourcePosters(fontName='ObviouslyVariable-None',
                          imagePath='backCover.pdf',
                          language='english',
                          axisSteps=7,
                          waterFallAxisName='wght',
                          fixedAxes={'wdth': 480, 'slnt': 11},
                          iterations=28)
    generateCover(horElems=6,
                  verElems=2,
                  scalingFactor=1.15,
                  inputPath='backCover.pdf',
                  outputPath='back-cover.png')

    combinePDF(inputs=['../variable-waterfall-poster-1/coverPosters.pdf',
                       'coverPosters.pdf'],
               outputPath='leftToRight.pdf')
    generateCover(horElems=2,
                  verElems=1,
                  scalingFactor=2.5,
                  inputPath='leftToRight.pdf',
                  outputPath='fromLeftToRight.png')
