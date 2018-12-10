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

    # exercise
    # code-example
    # list
    # section-title
    # table
    # text-block

    # safety copy
    if oldCopy is True:
        shutil.copy(path, path.replace('.lr', '.old.lr'))

    with codecs.open(path, 'r', 'utf-8') as lrFile:
        lrDoc = lrFile.read()

    soup = BeautifulSoup(lrDoc, 'html.parser')

    # images
    print(soup)
    for eachTag in soup.find_all('small_image'):
        print(eachTag)
    raise Exception

### Variables


### Instructions
for root, folders, fileNames in os.walk('../content'):

    for eachFileName in fileNames:
        if eachFileName == 'contents.lr':
            convertLR(os.path.join(root, eachFileName))
