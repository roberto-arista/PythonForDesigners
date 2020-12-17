#!/usr/bin/env python3
# coding: utf-8

# --- Modules --- #
import json
from time import time
from pathlib import Path

# --- Constants --- #

# --- Objects & Methods --- #
DICT_FOLDER = Path('dictionaries')

# --- Variables --- #
fontName = 'Skia'
language = 'italian'

# --- Instructions --- #
if __name__ == '__main__':
    from loadWords_v4 import loadWords
    from calcWordsLength import calcWordsLength

    for language in ['italian', 'english']:
        dictPath = DICT_FOLDER / f'{language}.txt'

        before = time()
        words = loadWords(dictPath)
        length_2_words = calcWordsLength(words, fontName)
        after = time()
        print(f'calc {language}: {after-before:.3f}s')

        before = time()
        length_2_wordsPath = DICT_FOLDER / f'lang={dictPath.stem}_font={fontName}.json'
        dictPath = DICT_FOLDER / f'{language}.txt'
        with open(length_2_wordsPath, mode='r', encoding='utf-8') as jsonFile:
            length_2_words = {float(kk): set(vv) for (kk, vv) in json.load(jsonFile).items()}
        after = time()
        print(f'loaded {language}: {after-before:.3f}s')

        print('-----------')
