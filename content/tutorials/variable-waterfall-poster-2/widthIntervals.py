from collections import defaultdict
import drawBot as dB

def typeAttributes(fontName, bodySize):
    dB.fill(0)
    dB.stroke(None)
    dB.font(fontName, bodySize)

def lerp(aa, bb, factor):
    return aa + (bb-aa) * factor

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

def calcWordsIntervals(words, fontName, axisName, axisSteps, fixedAxes={}):
    """the result of this function will be cached"""
    typeAttributes(fontName, 1)
    varFontAxes = dB.listFontVariations()
    word_2_intervals = defaultdict(dict)
    for eachStep in range(axisSteps):
        factor = eachStep / (axisSteps-1)
        axisValue = lerp(varFontAxes[axisName]['minValue'],
                         varFontAxes[axisName]['maxValue'], factor)
        fontParams = dict(fixedAxes)
        fontParams[axisName] = axisValue
        dB.fontVariations(**fontParams)
        for eachWord in words:
            txtWdt, txtHgt = dB.textSize(eachWord)
            word_2_intervals[eachWord][axisValue] = txtWdt
    return word_2_intervals


if __name__ == '__main__':
    fontName = 'Skia'
    axisName = 'wght'
    axisSteps = 5
    fixedAxes = {'wdth': 1.2}

    words = loadWords('sample.txt')
    word_2_intervals = calcWordsIntervals(words, fontName,
                                          axisName, axisSteps,
                                          fixedAxes)
