#!/usr/bin/env python3
# coding: utf-8

def loadWords(filePath):
    with open(filePath, mode='r', encoding='utf-8') as txtFile:
        return {ll.rstrip()
                for ll in txtFile.readlines()
                if ll.rstrip()}


if __name__ == '__main__':
    words = loadWords('dictionaries/italian.txt')
    print(len(words))
    # >>> 17604
