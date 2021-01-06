#!/usr/bin/env python3

# --- Modules --- #
import json
from pathlib import Path

# --- Constants --- #
DICT_FOLDER = Path('dictionaries')

# --- Variables --- #
fontName = 'Skia'
language = 'italian'

# --- Instructions --- #
if __name__ == '__main__':
    from loadWords_v4 import loadWords
    from calcWordsWidth import calcWordsWidth

    dictPath = DICT_FOLDER / f'{language}.txt'

    # words width calc is influenced by: dictName, fontName
    width_2_wordsPath = DICT_FOLDER / f'lang={dictPath.stem}_font={fontName}.json'

    if width_2_wordsPath.exists():
        with open(width_2_wordsPath, mode='r', encoding='utf-8') as jsonFile:
            width_2_words = json.load(jsonFile)
    else:
        words = loadWords(dictPath)
        width_2_words = calcWordsWidth(words, fontName)
        with open(width_2_wordsPath, mode='w', encoding='utf-8') as jsonFile:
            json.dump({kk: list(vv) for (kk, vv) in width_2_words.items()},
                      jsonFile, indent=4)
