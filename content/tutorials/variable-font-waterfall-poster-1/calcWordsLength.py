#!/usr/bin/env python3
# coding: utf-8

# --- Modules --- #
import drawBot as dB
from pathlib import Path
from collections import defaultdict

# --- Constants --- #
DICT_FOLDER = Path('dictionaries')
PRECISION = 2

# --- Objects & Methods --- #
def calcWordsLength(words, fontName):
    dB.font(fontName, 1)
    length_2_words = defaultdict(set)
    for eachWord in words:
        txtWdt, txtHgt = dB.textSize(eachWord)
        length_2_words[round(txtWdt, PRECISION)].add(eachWord)
    return length_2_words


# --- Variables --- #
fontName = 'Skia'
language = 'italian'

# --- Instructions --- #
if __name__ == '__main__':
    from loadWords_v4 import loadWords
    words = loadWords(DICT_FOLDER / f'{language}.txt')
    length_2_words = calcWordsLength(words, fontName)
    print(f'words: {len(words)}')
    # words: 16458
    print(f'groups: {len(length_2_words)}')
    # groups: 573
    print(f'words/groups ratio: {len(words)/len(length_2_words):.3f}')
    # words/groups ratio: 28.723
