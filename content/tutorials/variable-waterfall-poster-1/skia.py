#!/usr/bin/env python3
# coding: utf-8

# -------------------------- #
# Display Skia Variable Font #
# -------------------------- #

# --- Modules --- #
from tools import lerp
import drawBot as dB

# --- Variables --- #
fontName = 'Skia'
bodySize = 100
text = 'ABC'

horElems = 6
verElems = 4

# --- Instructions --- #
if __name__ == '__main__':
    dB.newDrawing()
    dB.newPage(1800, 500)

    dB.font(fontName, bodySize)
    dB.translate(135, 60)

    fontVars = dB.listFontVariations()
    print(fontVars)

    xAxis = fontVars['wght']
    yAxis = fontVars['wdth']

    horStep = dB.width()/horElems
    verStep = dB.height()/verElems - 24

    for jj in range(verElems):
        yy = verStep * jj
        yFactor = jj/verElems
        yAxisValue = lerp(yAxis['minValue'], yAxis['maxValue'], yFactor)

        for ii in range(horElems):
            xx = horStep * ii
            xFactor = ii/(horElems-1)
            xAxisValue = lerp(xAxis['minValue'], xAxis['maxValue'], xFactor)

            dB.fontVariations(**{'wdth': yAxisValue, 'wght': xAxisValue})
            dB.text(text, (xx, yy), align='center')

    dB.saveImage('skia.pdf')
    dB.saveImage('skia.png')
    dB.endDrawing()
