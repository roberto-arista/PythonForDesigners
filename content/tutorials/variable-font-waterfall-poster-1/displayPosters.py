#!/usr/bin/env python3
# coding: utf-8

# --- Modules --- #
from cover import generateCover, generateSourcePosters


# --- Variables --- #
fontName = 'Skia'
imagePath = 'posters.pdf'


# --- Instructions --- #
if __name__ == '__main__':
    generateSourcePosters(fontName, imagePath, language='italian', iterations=6)
    generateCover(horElems=3, verElems=1, scalingFactor=2.5,
                  inputPath=imagePath, outputPath='3posters.png')
