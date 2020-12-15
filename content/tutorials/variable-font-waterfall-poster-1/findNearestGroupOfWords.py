#!/usr/bin/env python3
# coding: utf-8

# --- Modules --- #
from random import shuffle
from pathlib import Path

# --- Constants --- #
DICT_FOLDER = Path('dictionaries')

# --- Objects & Methods --- #
def findNearestGroupOfWords(length_2_words, netWdt, pointSize):
    smallestDiff = min(length_2_words.keys(),
                       key=lambda length: abs(length-netWdt/pointSize))
    nearestWords = list(length_2_words[smallestDiff])
    shuffle(nearestWords)
    return nearestWords


# --- Variables --- #
fontName = 'Skia'
language = 'italian'

netWdt = 400
pointSize = 68

# --- Instructions --- #
if __name__ == '__main__':
    from loadWords_v4 import loadWords
    from calcWordsLength import calcWordsLength

    words = loadWords(DICT_FOLDER / f'{language}.txt')
    length_2_words = calcWordsLength(words, fontName)

    nearestWords = findNearestGroupOfWords(length_2_words,
                                           netWdt,
                                           pointSize)
    print(f'available words: {len(nearestWords)}')
    # available words: 12

    for indexLine in range(16):
        if len(nearestWords) == 0:
            nearestWords = findNearestGroupOfWords(length_2_words,
                                                   netWdt,
                                                   pointSize)
        chosenWord = nearestWords.pop()
        print(f'\t{indexLine+1:0>2d}: {chosenWord}')
        # 01: sfruttamento
        # 02: allontanatevi
        # 03: trasmettitore
        # 04: cristianesimo
        # 05: professionale
        # 06: maggiorenne
        # 07: spiegherebbe
        # 08: terribilmente
        # 09: affermazione
        # 10: collaboratore
        # 11: combattendo
        # 12: suggerimenti
        # 13: spiegherebbe
        # 14: combattendo
        # 15: maggiorenne
        # 16: professionale
