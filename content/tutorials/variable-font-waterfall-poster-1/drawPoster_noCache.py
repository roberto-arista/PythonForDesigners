#!/usr/bin/env python3
# coding: utf-8

# --- Modules --- #
import drawBot as dB
from pathlib import Path

from loadWords_v4 import loadWords
from calcWordsLength import calcWordsLength
from findNearestGroupOfWords import findNearestGroupOfWords

# --- Constants --- #
DICT_FOLDER = Path('dictionaries')
MARGIN = 100
DRAFT_MODE = True

# --- Objects & Methods --- #
def lineQualities(thickness=1):
    dB.stroke(0)
    dB.strokeWidth(thickness)
    dB.fill(None)

def typeQualities(fontName, pointSize):
    dB.fill(0)
    dB.stroke(None)
    dB.font(fontName, pointSize)

def drawPoster(fontName='Skia', dictName='italian.txt',
               pointSize=120, leading=120):
    dictPath = DICT_FOLDER / dictName

    words = loadWords(dictPath)
    length_2_words = calcWordsLength(words, fontName)

    netWdt = dB.width()-MARGIN*2
    netHgt = dB.height()-MARGIN*2

    if DRAFT_MODE is True:
        lineQualities()
        dB.rect(MARGIN, MARGIN, netWdt, netHgt)

    typeQualities(fontName, pointSize)
    lines = netHgt // leading
    dB.translate(MARGIN, MARGIN+netHgt-leading)
    nearestWords = findNearestGroupOfWords(length_2_words,
                                           netWdt, pointSize)
    for ii in range(lines):
        if len(nearestWords) > 0:
            nearestWords = findNearestGroupOfWords(length_2_words,
                                                   netWdt, pointSize)
        chosenWord = nearestWords.pop()
        dB.text(chosenWord, (0, 0))
        dB.translate(0, -leading)


# --- Variables --- #
fontName = 'Skia'
language = 'italian'

netWdt = 400
pointSize = 68

# --- Instructions --- #
if __name__ == '__main__':
    dB.newDrawing()
    for eachPoster in range(5):
        dB.newPage('A3')
        drawPoster()
    dB.saveImage('posters.pdf')
    dB.endDrawing()
