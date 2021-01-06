#!/usr/bin/env python3

# -- Modules -- #
import drawBot as dB
from cover import background

# -- Constants -- #
WHITE = 1, 1, 1

# -- Functions -- #
def lerp(aa, bb, factor):
    return aa + (bb-aa) * factor

def getFactor(aa, bb, innerValue):
    return (innerValue-aa)/(bb-aa)

def lineStyle(thickness):
    dB.stroke(0)
    dB.fill(None)
    dB.strokeWidth(thickness)

def captionText():
    dB.fill(0)
    dB.stroke(None)
    dB.fontVariations(resetVariations=True)
    dB.font('.SFNS-Regular', 90)

def drawLetter(xFactor, yFactor, instanceParams, pointSize, isNeutral=False):
    xx = xFactor * (horStep * (grid-1))
    yy = yFactor * (verStep * (grid-1))
    dB.font('Skia', pointSize)
    dB.fontVariations(**instanceParams)
    dB.text('A', (xx, yy+100), align='center')
    dB.oval(xx-ovalRad, yy-ovalRad, ovalRad*2, ovalRad*2)

    captionText()
    lines = [f'weight {instanceParams["wght"]:.2f}',
             f'width {instanceParams["wdth"]:.2f}']
    neut = '' if isNeutral is False else '\n[neutral]'
    dB.text('; '.join(lines) + neut, (xx, yy-160), align='center')

def toFactor(axisName, value, fontName='Skia'):
    dB.font(fontName)
    fontVariations = dB.listFontVariations()
    return getFactor(fontVariations[axisName]['minValue'],
                     fontVariations[axisName]['maxValue'],
                     value)

def toValue(axisName, factor, fontName='Skia'):
    dB.font(fontName)
    fontVariations = dB.listFontVariations()
    return lerp(fontVariations[axisName]['minValue'],
                fontVariations[axisName]['maxValue'], factor)

def drawSkiaScheme():
    dB.fill(0)
    dB.font('Skia')
    fontVars = dB.listFontVariations()

    # extremes
    for jj in range(grid):
        yFactor = jj / (grid-1)
        for ii in range(grid):
            xFactor = ii / (grid-1)
            wgtVal = toValue(xAxis, xFactor)
            wdtVal = toValue(yAxis, yFactor)
            instanceParams = {xAxis: wgtVal,
                              yAxis: wdtVal}
            drawLetter(xFactor, yFactor, instanceParams, pointSize)

    # neutral state
    xFactor = toFactor(xAxis, fontVars[xAxis]['defaultValue'])
    yFactor = toFactor(yAxis, fontVars[yAxis]['defaultValue'])
    instanceParams = {xAxis: fontVars[xAxis]['defaultValue'],
                      yAxis: fontVars[yAxis]['defaultValue']}
    drawLetter(xFactor, yFactor, instanceParams, pointSize, isNeutral=True)


# -- Variables -- #
pointSize = 900
verStep = 2200
horStep = 1800
grid = 2
ovalRad = 36
tickLen = 100

wdtSteps = 6
wgtSteps = 4

xAxis = 'wght'
yAxis = 'wdth'

# -- Instructions -- #
if __name__ == '__main__':

    dB.newPage(7200, 3600)
    background(WHITE)

    # width steps
    dB.translate(800, 390)
    drawSkiaScheme()

    wgtValue = 1.6
    lftXX = xx = toFactor(xAxis, wgtValue) * (verStep * (grid-1))
    captionText()
    dB.text(f'weight: {wgtValue}', (xx, -180), align='center')

    lineStyle(thickness=20)
    dB.line((xx, 0), (xx, verStep * (grid-1)))
    with dB.savedState():
        dB.translate(xx, 0)
        for ii in range(wdtSteps):
            yy = (ii/(wdtSteps-1)) * (verStep * (grid-1))
            lineStyle(thickness=20)
            dB.line((-tickLen/2, yy), (tickLen/2, yy))

            wdtValue = toValue('wdth', ii/(wdtSteps-1))
            captionText()
            dB.text(f'width {wdtValue:.2f}', (85, yy-20), align='left')

    # weight steps
    dB.save()
    dB.translate(horStep*(grid-1) + horStep + 80, 0)
    drawSkiaScheme()

    wdtValue = .9
    yy = toFactor(yAxis, wdtValue) * (verStep * (grid-1))
    captionText()
    dB.text(f'width {wdtValue}', (-70, yy-32), align='right')

    lineStyle(thickness=20)
    dB.line((0, yy), (horStep * (grid-1), yy))
    with dB.savedState():
        dB.translate(0, yy)
        for jj in range(wgtSteps):
            xx = (jj/(wgtSteps-1)) * (horStep * (grid-1))
            lineStyle(thickness=20)
            dB.line((xx, -tickLen/2), (xx, tickLen/2))

            wgtValue = toValue('wght', jj/(wgtSteps-1))
            captionText()
            dB.text(f'weight: {wgtValue:.2f}', (xx, -140), align='center')

    dB.saveImage('equidistantSteps.png')

    # dot on the right
    wgtValue = 2.75
    xx = toFactor(xAxis, wgtValue) * (horStep * (grid-1))
    dB.fill(*WHITE)
    thisRad = ovalRad*1.25
    dB.oval(xx-thisRad, yy-thisRad, thisRad*2, thisRad*2)

    captionText()
    dB.text('desired\nvalue!', (xx, yy+200), align='center')

    # dot on the left
    dB.restore()
    wdtValue = .69
    yy = toFactor(yAxis, wdtValue) * (verStep * (grid-1))
    dB.fill(*WHITE)
    dB.oval(lftXX-thisRad, yy-thisRad, thisRad*2, thisRad*2)

    captionText()
    dB.text('desired\nvalue!', (lftXX-80, yy+24), align='right')

    dB.saveImage('equidistantSteps_extraVal.png')
