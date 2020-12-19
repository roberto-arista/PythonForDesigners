#!/usr/bin/env python3
# coding: utf-8

# ------------------------------ #
# VARIABLE FONT WATERFALL POSTER #
# ------------------------------ #

# --- Modules --- #
# std library
import itertools
from pathlib import Path
import json
from random import choice
from collections import defaultdict

# external dependencies
import drawBot as dB

# --- Constants --- #
PRECISION = 2
MARGIN = 100
DRAFT_MODE = False
REBUILD = False

DICT_LOCATION = Path('../variable-waterfall-poster-1/dictionaries')

# --- Objects & Methods --- #
def lineQualities(thickness=1):
    dB.stroke(0)
    dB.strokeWidth(thickness)
    dB.fill(None)

def typeQualities(fontName, pointSize):
    dB.fill(0)
    dB.stroke(None)
    dB.font(fontName, pointSize)

def lerp(aa, bb, factor):
    return aa + (bb-aa) * factor

def getFactor(aa, bb, innerValue):
    return (innerValue-aa)/(bb-aa)

def identity(ss):
    return ss

def uppercase(ss):
    return ss.upper()

TXT_FILTERS = {
    'identity': identity,
    'uppercase': uppercase,
}

def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ...
    straight from itertools docs page"""
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def findInterval(sequence, value):
    for thisValue, nextValue in pairwise(sequence):
        if thisValue <= value <= nextValue:
            return thisValue, nextValue
    raise ValueError('no interval found')

def loadWords(filePath, minChars=5, txtFilter=identity):
    include = False
    words = set()

    with open(filePath, mode='r', encoding='utf-8') as txtFile:
        for eachLine in (ll.strip() for ll in txtFile.readlines()):

            if include is True and len(eachLine) >= minChars:
                words.add(txtFilter(eachLine))

            if eachLine == '*****':
                include = True

    return words

def calcWordsLengthIntervals(words, fontName, axisName, axisSteps, fixedAxes={}):
    """the result of this function will be cached"""
    typeQualities(fontName, 1)
    varFontAxes = dB.listFontVariations()
    word_2_lengthIntervals = defaultdict(dict)
    for eachStep in range(axisSteps):
        factor = eachStep / (axisSteps-1)
        axisValue = lerp(varFontAxes[axisName]['minValue'],
                         varFontAxes[axisName]['maxValue'], factor)
        fontParams = dict(fixedAxes)
        fontParams[axisName] = axisValue
        dB.fontVariations(**fontParams)
        for eachWord in words:
            txtWdt, txtHgt = dB.textSize(eachWord)
            word_2_lengthIntervals[eachWord][axisValue] = txtWdt
    return word_2_lengthIntervals

def calcWordsLengthFromIntervals(word_2_lengthIntervals, waterFallAxisValue):
    """the result of this function is used on the fly"""
    length_2_words = defaultdict(list)
    for eachWord, lengthIntervals in word_2_lengthIntervals.items():
        btm, top = findInterval(lengthIntervals.keys(), waterFallAxisValue)
        factor = getFactor(btm, top, waterFallAxisValue)
        wordLen = lerp(lengthIntervals[btm], lengthIntervals[top], factor)
        length_2_words[round(wordLen, PRECISION)].append(eachWord)
    return length_2_words

def findNearestWord(length_2_words, wdt, pointSize):
    smallestDiff = min(length_2_words.keys(), key=lambda x: abs(x-wdt/pointSize))
    return choice(length_2_words[smallestDiff])

def drawWaterFallPoster(fontName='Skia', dictName='italian.txt', pointSize=120, leading=120,
                        axisSteps=5, waterFallAxisName='wght', fixedAxes={'wdth': 1.2}):
    dictPath = DICT_LOCATION / dictName
    txtFilterName = 'uppercase'

    # words length calc is influenced by: dictName, fontName, axisSteps, waterFallAxis, fixedAxes, txtFilter
    fixedAxesRepr = "-".join([f'{kk}{vv}' for (kk, vv) in fixedAxes.items()])
    lengthIntervalsPath = DICT_LOCATION / f'lang={dictPath.stem}_font={fontName}_steps={axisSteps}_waterFallAxis={waterFallAxisName}_fixedAxes={fixedAxesRepr}_filter={txtFilterName}.json'

    if lengthIntervalsPath.exists() and REBUILD is False:
        with open(lengthIntervalsPath, mode='r', encoding='utf-8') as wordsJson:
            word_2_lengthIntervals = defaultdict(dict)
            for eachWord, intervals in json.load(wordsJson).items():
                word_2_lengthIntervals[eachWord] = {float(kk): vv for (kk, vv) in intervals.items()}
    else:
        words = loadWords(dictPath, txtFilter=TXT_FILTERS[txtFilterName])
        word_2_lengthIntervals = calcWordsLengthIntervals(words, fontName, waterFallAxisName,
                                                          axisSteps, fixedAxes)
        with open(lengthIntervalsPath, mode='w', encoding='utf-8') as wordsJson:
            json.dump(word_2_lengthIntervals, wordsJson, indent=4)

    netWdt = dB.width()-MARGIN*2
    netHgt = dB.height()-MARGIN*2

    if DRAFT_MODE is True:
        lineQualities()
        dB.rect(MARGIN, MARGIN, netWdt, netHgt)

    typeQualities(fontName, pointSize)
    varFontAxes = dB.listFontVariations()
    lines = netHgt // leading
    dB.translate(MARGIN, MARGIN+netHgt-leading)
    for ii in range(lines):
        factor = ii / (lines-1)
        waterFallAxisValue = lerp(varFontAxes[waterFallAxisName]['minValue'],
                                  varFontAxes[waterFallAxisName]['maxValue'], factor)
        length_2_words = calcWordsLengthFromIntervals(word_2_lengthIntervals, waterFallAxisValue)
        aWord = findNearestWord(length_2_words, netWdt, pointSize)

        fontParams = dict(fixedAxes)
        fontParams[waterFallAxisName] = waterFallAxisValue
        dB.fontVariations(**fontParams)
        dB.text(aWord, (0, 0))
        dB.translate(0, -leading)


# --- Variables --- #
fontName = 'Skia'
dictName = 'italian.txt'
pointSize = 120
leading = 120
axisSteps = 5
waterFallAxisName = 'wght'
fixedAxes = {'wdth': 1.2, 'slnt': 6}

# --- Instructions --- #
if __name__ == '__main__':
    dB.newDrawing()
    for ii in range(3):
        dB.newPage('A3')
        drawWaterFallPoster(fontName, dictName, pointSize, leading, axisSteps,
                            waterFallAxisName, fixedAxes)
    dB.saveImage('poster.pdf')
    dB.endDrawing()
