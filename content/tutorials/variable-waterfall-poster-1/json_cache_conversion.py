#!/usr/bin/env python3
# coding: utf-8

# --- Modules --- #
import json
from pathlib import Path

# --- Constants --- #
DICT_FOLDER = Path('dictionaries')

# --- Objects & Methods --- #

# --- Variables --- #
fontName = 'Skia'
language = 'italian'

# --- Instructions --- #
if __name__ == '__main__':
    from loadWords_v4 import loadWords
    from calcWordsLength import calcWordsLength

    dictPath = DICT_FOLDER / f'{language}.txt'

    # words length calc is influenced by: dictName, fontName
    length_2_wordsPath = DICT_FOLDER / f'lang={dictPath.stem}_font={fontName}.json'

    if length_2_wordsPath.exists():
        with open(length_2_wordsPath, mode='r', encoding='utf-8') as jsonFile:
            length_2_words = {float(kk): set(vv) for (kk, vv) in json.load(jsonFile).items()}
    else:
        words = loadWords(dictPath)
        length_2_words = calcWordsLength(words, fontName)
        with open(length_2_wordsPath, mode='w', encoding='utf-8') as jsonFile:
            json.dump(length_2_words, jsonFile, indent=4)
