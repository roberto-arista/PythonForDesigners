import drawBot as dB
import itertools
from collections import defaultdict

def typeAttributes(fontName, pointSize):
    dB.fill(0)
    dB.stroke(None)
    dB.font(fontName, pointSize)

def lerp(aa, bb, factor):
    return aa + (bb-aa) * factor

def getFactor(aa, bb, innerValue):
    return (innerValue-aa)/(bb-aa)

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


if __name__ == '__main__':
    from varWaterfallPoster import loadWords
    words = loadWords('../variable-waterfall-poster-1/dictionaries/italian.txt')
    word_2_intervals = calcWordsWidthIntervals(words,
                                                fontName='Skia',
                                                axisName='wght',
                                                axisSteps=5,
                                                fixedAxes={'wdth': 1.2})
    # defaultdict(<class 'dict'>,
    #     {'coprifuoco': {0.4799: 5.13232421875,
    #                     1.1599: 5.544921875,
    #                     1.8398999999999999: 5.75390625,
    #                     2.5199: 5.9619140625,
    #                     3.1998999999999995: 6.16943359375},
    #      'procura': {0.4799: 3.6806640625,
    #                  1.1599: 3.9833984375,
    #                  1.8398999999999999: 4.1494140625,
    #                  2.5199: 4.31396484375,
    #                  3.1998999999999995: 4.47900390625},
    #      'concorrenza': {0.4799: 5.92919921875,
    #                      1.1599: 6.412109375,
    #                      1.8398999999999999: 6.6572265625,
    #                      2.5199: 6.90087890625,
    #                      3.1998999999999995: 7.14453125},
    #      'appassionato': {0.4799: 6.283203125,
    #                       1.1599: 6.85400390625,
    #                       1.8398999999999999: 7.1630859375,
    #                       2.5199: 7.46923828125,
    #                       3.1998999999999995: 7.77587890625}
