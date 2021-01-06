#!/usr/bin/env python3

# ------------- #
# Article Cover #
# ------------- #

# --- Modules --- #
import drawBot as dB
from waterfallPoster import drawWaterfallPoster, pointSize, leading

# --- Constants --- #
WHITE = 1, 1, 1
GRAY = .7, .7, .7

# --- Functions --- #
def background(clr):
    dB.fill(*clr)
    dB.rect(0, 0, dB.width(), dB.height())

def generateSourcePosters(fontName, imagePath, language, iterations=1):
    dictName = f'{language}.txt'

    dB.newDrawing()
    for ii in range(iterations):
        dB.newPage('A3')
        drawWaterfallPoster(fontName, dictName, pointSize, leading)
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


# --- Variables --- #
fontName = 'Skia'
inputPath = 'coverPosters.pdf'

scalingFactor = .75

horElems = 8
verElems = 3

# --- Instructions --- #
if __name__ == '__main__':
    generateSourcePosters(fontName, inputPath, language='italian', iterations=28)
    generateCover(horElems, verElems, scalingFactor, inputPath, outputPath='visual-abstract.png')
