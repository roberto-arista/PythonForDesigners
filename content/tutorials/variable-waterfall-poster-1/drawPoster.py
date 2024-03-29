#!/usr/bin/env python3

# --- Modules --- #
import drawBot as dB
from pathlib import Path
import json
from collections import defaultdict
from random import shuffle

# --- Constants --- #
DICT_FOLDER = Path('dictionaries')
MARGIN = 100
DRAFT_MODE = False
PRECISION = 2

# --- Objects & Methods --- #
def lineQualities(thickness=1):
    dB.stroke(0)
    dB.strokeWidth(thickness)
    dB.fill(None)

def typeQualities(fontName, pointSize):
    dB.fill(0)
    dB.stroke(None)
    dB.font(fontName, pointSize)

def uppercase(txt):
    return txt.upper()

def identity(txt):
    return txt

def loadWords(filePath, minChars=5, txtFilter=identity):
    include = False
    words = set()

    with open(filePath, mode='r', encoding='utf-8') as txtFile:
        for eachLine in (ll.strip() for ll in txtFile.readlines()):

            if include is True and len(eachLine) >= minChars:
                words.add(eachLine)

            if eachLine == '*****':
                include = True

    return words

def calcWordsWidth(words, fontName):
    dB.font(fontName, 1)
    width_2_words = defaultdict(set)
    for eachWord in words:
        txtWdt, txtHgt = dB.textSize(eachWord)
        width_2_words[round(txtWdt, PRECISION)].add(eachWord)
    return width_2_words

def findNearestGroupOfWords(width_2_words, netWdt, pointSize):
    smallestDiff = min(width_2_words.keys(),
                       key=lambda width: abs(width-netWdt/pointSize))
    nearestWords = list(width_2_words[smallestDiff])
    shuffle(nearestWords)
    return nearestWords

def drawPoster(fontName='Skia', dictName='italian.txt',
               pointSize=120, leading=120):
    dictPath = DICT_FOLDER / dictName

    # words width calc is influenced by: dictName, fontName
    width_2_wordsPath = DICT_FOLDER / f'lang={dictPath.stem}_font={fontName}.json'

    if width_2_wordsPath.exists():
        with open(width_2_wordsPath, mode='r', encoding='utf-8') as jsonFile:
            width_2_words = {float(kk): set(vv)
                              for (kk, vv)
                              in json.load(jsonFile).items()}
    else:
        words = loadWords(dictPath)
        width_2_words = calcWordsWidth(words, fontName)
        with open(width_2_wordsPath, mode='w', encoding='utf-8') as jsonFile:
            json.dump({kk: list(vv) for (kk, vv) in width_2_words.items()},
                      jsonFile, indent=4)

    netWdt = dB.width()-MARGIN*2
    netHgt = dB.height()-MARGIN*2

    if DRAFT_MODE is True:
        lineQualities()
        dB.rect(MARGIN, MARGIN, netWdt, netHgt)

    typeQualities(fontName, pointSize)
    lines = netHgt // leading
    dB.translate(MARGIN, MARGIN+netHgt-leading)
    nearestWords = findNearestGroupOfWords(width_2_words,
                                           netWdt, pointSize)
    for ii in range(lines):
        if len(nearestWords) > 0:
            nearestWords = findNearestGroupOfWords(width_2_words,
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
    dB.endDrawing()
