#!/usr/bin/env python3
# coding: utf-8

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

def calcWordsLength(words, fontName):
    dB.font(fontName, 1)
    length_2_words = defaultdict(set)
    for eachWord in words:
        txtWdt, txtHgt = dB.textSize(eachWord)
        length_2_words[round(txtWdt, PRECISION)].add(eachWord)
    return length_2_words

def findNearestGroupOfWords(length_2_words, netWdt, pointSize):
    smallestDiff = min(length_2_words.keys(),
                       key=lambda length: abs(length-netWdt/pointSize))
    nearestWords = list(length_2_words[smallestDiff])
    shuffle(nearestWords)
    return nearestWords

def drawPoster(fontName='Skia', dictName='italian.txt',
               pointSize=120, leading=120):
    dictPath = DICT_FOLDER / dictName

    # words length calc is influenced by: dictName, fontName
    length_2_wordsPath = DICT_FOLDER / f'lang={dictPath.stem}_font={fontName}.json'

    if length_2_wordsPath.exists():
        with open(length_2_wordsPath, mode='r', encoding='utf-8') as jsonFile:
            length_2_words = {float(kk): set(vv)
                              for (kk, vv)
                              in json.load(jsonFile).items()}
    else:
        words = loadWords(dictPath)
        length_2_words = calcWordsLength(words, fontName)
        with open(length_2_wordsPath, mode='w', encoding='utf-8') as jsonFile:
            json.dump(length_2_words, jsonFile, indent=4)

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
    dB.endDrawing()
