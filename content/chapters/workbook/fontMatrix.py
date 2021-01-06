#!/usr/bin/env python3

# --------------- #
# UFO Font Matrix #
# --------------- #

# --- Modules --- #
import drawBot as dB
import fontParts.world as fp
from collections import namedtuple

# --- Constants --- #
BoxSize = namedtuple('Box', ['width', 'height'])

# --- Functions & Classes --- #
def lineAttributes(thickness=1):
    dB.stroke(0)
    dB.fill(None)
    dB.strokeWidth(thickness)

def shapeAttributes():
    dB.fill(0)
    dB.stroke(None)

def captionAttributes():
    shapeAttributes()
    dB.font('.SFNS-Regular', 7)

def initPage(pageFormat, pageMargin, cellSize):
    dB.newPage(pageFormat)
    dB.translate(pageMargin, dB.height()-pageMargin-cellSize.height)
    dB.save()

def drawGlyph(glyph):
    """from https://pythonfordesigners.com/chapters/cookbook/"""
    glyphPath = dB.BezierPath(glyphSet=glyph.layer)
    glyph.draw(glyphPath)
    dB.drawPath(glyphPath)

def drawGlyphCell(aGlyph, pointSize, cellSize):
    wdt, hgt = cellSize
    fontInfo = aGlyph.font.info

    lineAttributes()
    # box + captions
    dB.rect(0, 0, cellSize.width, cellSize.height)
    dB.line((0, cellSize.height-dB.fontLineHeight()),
            (cellSize.width, cellSize.height-dB.fontLineHeight()))
    dB.line((0, dB.fontLineHeight()), (cellSize.width, dB.fontLineHeight()))

    captionAttributes()
    glyphName = f'{aGlyph.name}'
    if dB.textSize(glyphName)[0] >= cellSize.width:
        glyphName = f'{glyphName[:len(glyphName)//2]}...'

    dB.text(glyphName, (cellSize.width/2, cellSize.height-dB.fontLineHeight() -.5), align='center')
    if aGlyph.unicode:
        dB.text(f'{aGlyph.unicode:0>4X}', (cellSize.width/2, -dB.fontDescender() +2), align='center')

    with dB.savedState():
        dB.translate(cellSize.width/2, cellSize.height/2 + dB.fontLineHeight())
        scalingFactor = pointSize/1000
        dB.scale(scalingFactor)
        dB.translate(-aGlyph.width/2, -fontInfo.unitsPerEm/2)
        shapeAttributes()
        drawGlyph(aGlyph)

        lineAttributes()
        lineOffset = 150      # upms
        dB.line((0, fontInfo.descender-lineOffset), (0, fontInfo.ascender+lineOffset))
        dB.line((aGlyph.width, fontInfo.descender-lineOffset), (aGlyph.width, fontInfo.ascender+lineOffset))
        for eachVerticalMetric in [0, fontInfo.capHeight, fontInfo.descender, fontInfo.ascender]:
            dB.line((-lineOffset, eachVerticalMetric), (aGlyph.width+lineOffset, eachVerticalMetric))

def drawFontMatrix(ufoFont, pageFormat, pageMargin, pointSize, cellSize):
    initPage(pageFormat, pageMargin, cellSize)

    netWdt = (dB.width() - pageMargin*2)
    netHgt = (dB.height() - pageMargin*2)
    columns = netWdt // cellSize.width
    rows =    netHgt // cellSize.height
    horStep = netWdt / columns
    verStep = netHgt / rows

    for index, eachGlyphName in enumerate(ufoFont.glyphOrder):
        eachGlyph = thisFont[eachGlyphName]
        with dB.savedState():
            dB.translate(horStep/2 - cellSize.width/2, 0)
            drawGlyphCell(eachGlyph, pointSize, cellSize)

        # handle content distribution
        if index % columns == columns-1 and (index+1) % (columns*rows) == 0:
            initPage(pageFormat, pageMargin, cellSize)
        elif index % columns == columns-1:
            dB.restore()
            dB.translate(0, -verStep)
            dB.save()
        else:
            dB.translate(horStep, 0)


if __name__ == '__main__':
    # --- Variables --- #
    fontName = 'SourceSerifPro-Regular.ufo'

    cellSize = BoxSize(75, 100)
    pageMargin = 50
    pointSize = 48
    pageFormat = 'A4'

    # --- Instructions --- #
    thisFont = fp.OpenFont(fontName)
    drawFontMatrix(thisFont, pageFormat, pageMargin, pointSize, cellSize)
