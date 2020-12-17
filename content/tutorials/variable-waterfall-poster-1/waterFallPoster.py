#!/usr/bin/env python3
# coding: utf-8

# -------------------------------------- #
# VARIABLE FONT WATERFALL POSTER part #1 #
# -------------------------------------- #

# --- Modules --- #
# std library
from pathlib import Path
import json
from random import shuffle
from collections import defaultdict

# external dependencies
import drawBot as dB

# --- Constants --- #
PRECISION = 2
MARGIN = 100
DRAFT_MODE = False
REBUILD = False

DICT_FOLDER = Path('dictionaries')

# --- Objects & Methods --- #
def lineQualities(thickness=1):
    dB.stroke(0)
    dB.strokeWidth(thickness)
    dB.fill(None)

def typeQualities(fontName, pointSize):
    dB.fill(0)
    dB.stroke(None)
    dB.font(fontName, pointSize)

def identity(ss):
    return ss

def uppercase(ss):
    return ss.upper()

def loadWords(filePath, minChars=5, txtFunc=identity):
    include = False
    words = set()

    with open(filePath, mode='r', encoding='utf-8') as txtFile:
        for eachLine in (ll.strip() for ll in txtFile.readlines()):

            if include is True and len(eachLine) >= minChars:
                words.add(txtFunc(eachLine))

            if eachLine == '*****':
                include = True

    return words

def calcWordsLength(words, fontName):
    dB.font(fontName, 1)
    length_2_words = defaultdict(list)
    for eachWord in words:
        txtWdt, txtHgt = dB.textSize(eachWord)
        length_2_words[round(txtWdt, PRECISION)].append(eachWord)
    return length_2_words

def findNearestGroupOfWords(length_2_words, netWdt, pointSize):
    smallestDiff = min(length_2_words.keys(), key=lambda length: abs(length-netWdt/pointSize))
    nearestWords = list(length_2_words[smallestDiff])
    shuffle(nearestWords)
    return nearestWords

def drawWaterFallPoster(fontName='Skia', dictName='italian.txt', pointSize=120, leading=120):
    dictPath = DICT_FOLDER / dictName

    # words length calc is influenced by: dictName, fontName
    length_2_wordsPath = DICT_FOLDER / f'lang={dictPath.stem}_font={fontName}.json'

    if length_2_wordsPath.exists() and REBUILD is False:
        with open(length_2_wordsPath, mode='r', encoding='utf-8') as jsonFile:
            length_2_words = {float(kk): vv for (kk, vv) in json.load(jsonFile).items()}
    else:
        words = loadWords(dictPath, txtFunc=uppercase)
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

    nearestWords = findNearestGroupOfWords(length_2_words, netWdt, pointSize)
    for ii in range(lines):
        if len(nearestWords) > 0:
            nearestWords = findNearestGroupOfWords(length_2_words, netWdt, pointSize)
        chosenWord = nearestWords.pop()
        dB.text(chosenWord, (0, 0))
        dB.translate(0, -leading)


# --- Variables --- #
fontName = 'Skia'
dictName = 'english.txt'
pointSize = 120
leading = 120

# --- Instructions --- #
if __name__ == '__main__':
    dB.newDrawing()
    for ii in range(3):
        dB.newPage('A3')
        drawWaterFallPoster(fontName, dictName, pointSize, leading)
    dB.saveImage('poster.pdf')
    dB.endDrawing()
