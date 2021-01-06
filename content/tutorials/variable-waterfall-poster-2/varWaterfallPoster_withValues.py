#!/usr/bin/env python3

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
def lineAttributes(thickness=1):
    dB.stroke(0)
    dB.strokeWidth(thickness)
    dB.fill(None)

def typeAttributes(fontName, bodySize):
    dB.fill(0)
    dB.stroke(None)
    dB.font(fontName, bodySize)

def lerp(aa, bb, factor):
    return aa + (bb-aa) * factor

def getFactor(aa, bb, innerValue):
    return (innerValue-aa)/(bb-aa)

def identity(ss):
    return ss

def uppercase(ss):
    return ss.upper()

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

def loadWords(filePath, minLength=5, txtFunc=identity):
    with open(filePath, mode='r', encoding='utf-8') as txtFile:
        lines = [ll.rstrip() for ll in txtFile.readlines()]
    words = []
    include = False
    for eachLine in lines:
        if include is True and len(eachLine) >= minLength:
            words.append(txtFunc(eachLine))
        if eachLine == '*****':
            include = not include
    return words

def calcWordsWidthIntervals(words, fontName, axisName, axisSteps, fixedAxes={}):
    """the result of this function will be cached"""
    typeAttributes(fontName, 1)
    varFontAxes = dB.listFontVariations()
    word_2_widthIntervals = defaultdict(dict)
    for eachStep in range(axisSteps):
        factor = eachStep / (axisSteps-1)
        axisValue = lerp(varFontAxes[axisName]['minValue'],
                         varFontAxes[axisName]['maxValue'], factor)
        fontParams = dict(fixedAxes)
        fontParams[axisName] = axisValue
        dB.fontVariations(**fontParams)
        for eachWord in words:
            txtWdt, txtHgt = dB.textSize(eachWord)
            word_2_widthIntervals[eachWord][axisValue] = txtWdt
    return word_2_widthIntervals

def calcWordsWidthFromIntervals(word_2_widthIntervals, waterfallAxisValue):
    """the result of this function is used on the fly"""
    width_2_words = defaultdict(list)
    for eachWord, widthIntervals in word_2_widthIntervals.items():
        btm, top = findInterval(widthIntervals.keys(), waterfallAxisValue)
        factor = getFactor(btm, top, waterfallAxisValue)
        wordLen = lerp(widthIntervals[btm], widthIntervals[top], factor)
        width_2_words[round(wordLen, PRECISION)].append(eachWord)
    return width_2_words

def findNearestWord(width_2_words, wdt, bodySize):
    smallestDiff = min(width_2_words.keys(), key=lambda x: abs(x-wdt/bodySize))
    return choice(width_2_words[smallestDiff])

def captionText():
    dB.fontVariations(resetVariations=True)
    dB.font('.SFNS-Regular', 32)

def drawWaterfallPoster(fontName='Skia', dictName='italian.txt', bodySize=120, leading=120,
                        axisSteps=5, waterfallAxisName='wght', fixedAxes={'wdth': 1.2}):
    dictPath = DICT_LOCATION / dictName

    # words width calc is influenced by: dictName, fontName, axisSteps, waterfallAxis, fixedAxes
    fixedAxesRepr = "-".join([f'{kk}{vv}' for (kk, vv) in fixedAxes.items()])
    widthIntervalsPath = DICT_LOCATION / f'lang={dictPath.stem}_font={fontName}_steps={axisSteps}_waterfallAxis={waterfallAxisName}_fixedAxes={fixedAxesRepr}.json'

    if widthIntervalsPath.exists() and REBUILD is False:
        with open(widthIntervalsPath, mode='r', encoding='utf-8') as wordsJson:
            word_2_widthIntervals = defaultdict(dict)
            for eachWord, intervals in json.load(wordsJson).items():
                word_2_widthIntervals[eachWord] = {float(kk): vv for (kk, vv) in intervals.items()}
    else:
        words = loadWords(dictPath, txtFunc=uppercase)
        word_2_widthIntervals = calcWordsWidthIntervals(words, fontName, waterfallAxisName,
                                                          axisSteps, fixedAxes)
        with open(widthIntervalsPath, mode='w', encoding='utf-8') as wordsJson:
            json.dump(word_2_widthIntervals, wordsJson, indent=4)

    netWdt = dB.width()-MARGIN*2
    netHgt = dB.height()-MARGIN*2

    if DRAFT_MODE is True:
        lineAttributes()
        dB.rect(MARGIN, MARGIN, netWdt, netHgt)

    typeAttributes(fontName, bodySize)
    varFontAxes = dB.listFontVariations()
    lines = netHgt // leading
    dB.translate(MARGIN, MARGIN+netHgt-leading)
    for ii in range(lines):
        factor = ii / (lines-1)
        waterfallAxisValue = lerp(varFontAxes[waterfallAxisName]['minValue'],
                                  varFontAxes[waterfallAxisName]['maxValue'], factor)
        width_2_words = calcWordsWidthFromIntervals(word_2_widthIntervals, waterfallAxisValue)
        aWord = findNearestWord(width_2_words, netWdt, bodySize)

        fontParams = dict(fixedAxes)
        fontParams[waterfallAxisName] = waterfallAxisValue
        typeAttributes(fontName, bodySize)
        dB.fontVariations(**fontParams)
        dB.text(aWord, (0, 0))

        captionText()
        dB.text(f'{waterfallAxisName}: {waterfallAxisValue:.2f}', (60, -40))
        dB.translate(0, -leading)

    captionText()
    dB.text(f"wdth: {fixedAxes['wdth']:.2f}", (dB.width()/2-MARGIN, 70), align='center')


# --- Variables --- #
fontName = 'Skia'
dictName = 'italian.txt'
axisSteps = 5
waterfallAxisName = 'wght'

bodySize = 140
leading = 160

# --- Instructions --- #
if __name__ == '__main__':
    dB.newDrawing()
    parameters = [
        {
            'posterWdt': 0.9,
        },
        {
            'posterWdt': 1.2,
        },
        {
            'posterWdt': 1.5,
        },
    ]
    for posterParam in parameters:
        dB.newPage('A3')
        drawWaterfallPoster(fontName, dictName, bodySize, leading, axisSteps,
                            waterfallAxisName, {'wdth': posterParam['posterWdt']})

    dB.saveImage('postersWithValues.pdf')
    dB.endDrawing()

    from cover import generateCover
    generateCover(horElems=3,
                  verElems=1,
                  scalingFactor=2.5,
                  inputPath='postersWithValues.pdf',
                  outputPath='postersWithValues.png',
                  margin=250)
