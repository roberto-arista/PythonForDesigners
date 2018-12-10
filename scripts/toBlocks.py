#!/usr/bin/env python3
# coding: utf-8

##############################
# From custom tags to blocks #
##############################

### Modules
import os
import shutil
import codecs
from bs4 import BeautifulSoup

### Constants

### Functions & Procedures
def convertLR(path, oldCopy=True):

    # list
    # section-title
    # table
    # text-block

    # safety copy
    if oldCopy is True:
        shutil.copy(path, path.replace('.lr', '.old.lr'))

    # open the file and make the soup
    with codecs.open(path, 'r', 'utf-8') as lrFile:
        lrDoc = lrFile.read()
    soup = BeautifulSoup(lrDoc, 'lxml')

    # images
    # for eachTag in soup.find_all('large_image'):
        # print(eachTag['src'])

    # for eachTag in soup.find_all('small_image'):
        # print(eachTag['src'])

    # # code-example
    for eachTag in soup.find_all('pre_code'):
        print(eachTag.text)
        raise Exception

    # raise Exception

    # exercise


### Variables


### Instructions
for root, folders, fileNames in os.walk('../content'):

    for eachFileName in fileNames:
        if eachFileName == 'contents.lr':
            convertLR(os.path.join(root, eachFileName))
