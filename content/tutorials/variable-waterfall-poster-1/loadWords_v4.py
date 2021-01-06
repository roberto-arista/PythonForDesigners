#!/usr/bin/env python3

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


if __name__ == '__main__':
    words = loadWords('dictionaries/italian.txt')
    print(len(words))
    # >>> 16458
