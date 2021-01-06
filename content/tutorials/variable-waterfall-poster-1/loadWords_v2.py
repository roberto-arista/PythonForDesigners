#!/usr/bin/env python3

def loadWords(filePath):
    include = False
    words = set()

    with open(filePath, mode='r', encoding='utf-8') as txtFile:
        for eachLine in (ll.strip() for ll in txtFile.readlines()):

            if include is True:
                words.add(eachLine)

            if eachLine == '*****':
                include = True

    return words


if __name__ == '__main__':
    words = loadWords('dictionaries/italian.txt')
    print(len(words))
    # >>> 17596
