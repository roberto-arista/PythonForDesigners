#!/usr/bin/env python3

# ------------ #
# Show Beziers #
# ------------ #

# --- Modules --- #
import drawBot as dB
import fontParts.world as fp
from fontTools.pens.basePen import BasePen

# --- Constants --- #
ANCHOR_SIDE = 10
HND_RAD = 4

# --- Functions & Classes --- #
class ShowBeziersPen(BasePen):

    def __init__(self, glyphSet):
        super().__init__(glyphSet)
        self.prevPt = None

    def _moveTo(self, pt):
        xx, yy = pt
        shapeAttributes()
        dB.rect(xx-ANCHOR_SIDE/2, yy-ANCHOR_SIDE/2, ANCHOR_SIDE, ANCHOR_SIDE)
        self.prevPt = pt

    def _lineTo(self, pt):
        xx, yy = pt
        dB.rect(xx-ANCHOR_SIDE/2, yy-ANCHOR_SIDE/2, ANCHOR_SIDE, ANCHOR_SIDE)
        self.prevPt = pt

    def _curveToOne(self, pt1, pt2, pt3):
        lineAttributes()
        dB.line(pt1, self.prevPt)
        dB.line(pt2, pt3)

        shapeAttributes()
        dB.oval(pt1[0]-HND_RAD, pt1[1]-HND_RAD, HND_RAD*2, HND_RAD*2)
        dB.oval(pt2[0]-HND_RAD, pt2[1]-HND_RAD, HND_RAD*2, HND_RAD*2)
        dB.rect(pt3[0]-ANCHOR_SIDE/2, pt3[1]-ANCHOR_SIDE/2, ANCHOR_SIDE, ANCHOR_SIDE)
        self.prevPt = pt3

def lineAttributes(thickness=1):
    dB.stroke(0)
    dB.fill(None)
    dB.strokeWidth(thickness)

def shapeAttributes(alpha=1):
    dB.fill(0, alpha)
    dB.stroke(None)

def drawGlyph(glyph):
    """from https://pythonfordesigners.com/chapters/cookbook/"""
    glyphPath = dB.BezierPath(glyphSet=glyph.layer)
    glyph.draw(glyphPath)
    dB.drawPath(glyphPath)


if __name__ == '__main__':
    # --- Variables --- #
    fontName = 'SourceSerifPro-Regular.ufo'
    scalingFactor = .6

    # --- Instructions --- #
    myFont = fp.OpenFont(fontName)
    myGlyph = myFont['a']
    glyphPen = ShowBeziersPen(myFont)
    xMin, yMin, xMax, yMax = myGlyph.bounds
    glyphHgt = yMax-yMin

    dB.newDrawing()
    dB.newPage(400, 400)
    dB.translate(dB.width()/2, dB.height()/2)

    lineAttributes()
    with dB.savedState():
        dB.scale(scalingFactor)
        dB.translate(-myGlyph.width/2, -glyphHgt/2)

        shapeAttributes(alpha=.25)
        drawGlyph(myGlyph)

        lineAttributes()
        drawGlyph(myGlyph)

        myGlyph.draw(glyphPen)

    dB.saveImage('showBeziers.pdf')
    dB.endDrawing()
