#!/usr/bin/env python3
# coding: utf-8

##############################
# From custom tags to blocks #
##############################

### Modules
import re
from os.path import join as joinPth
from os.path import dirname
import codecs
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

### Constants
FIELD_SEPARATOR = '-'*4
TAGS = ['large_image',
        'small_image',
        'pre_code',
        'section_title',
        'workbook',
        'exercise_wrapper',
        'code_image_wrapper',
        'table',
        'ul',
        'figcaption',
        'p']


### Functions & Procedures
def convertImage(tag, kind):
    block = ['#### image ####']
    block.append(f"name: {tag['src']}")
    block.append(FIELD_SEPARATOR)
    if kind == 'large':
        block.append('class: large_image')
    else:
        block.append('class: small_image')
    block.append(FIELD_SEPARATOR)
    return block

def convertCodeExampleWithoutImage(tag, chapterFolder, counter):
    block = ['#### code-example ####']
    snippetName = f'{counter:0>2d}.py'
    with codecs.open(joinPth(chapterFolder, snippetName), 'w', 'utf-8') as snippetFile:
        snippetFile.write(tag.text)
        block.append(f'snippet: {snippetName}')
        block.append(FIELD_SEPARATOR)
    return block

def convertCodeImageWrapper(tag, chapterFolder, counter):
    block = ['#### code-example ####']

    # snippet
    snippetName = f'{counter:0>2d}.py'
    with codecs.open(joinPth(chapterFolder, snippetName), 'w', 'utf-8') as snippetFile:
        snippetFile.write(tag.pre_code.text)
        block.append(f'snippet: {snippetName}')
        block.append(FIELD_SEPARATOR)

    # images
    if tag.code_diagram:
        block.append(f'diagram: {tag.code_diagram["src"]}')

    if tag.code_image:
        block.append(f'image: {tag.code_image["src"]}')

    block.append(FIELD_SEPARATOR)

    return block

def convertLink2Mark(tag):
    return f'[{tag.string}]({tag["href"]})'

def convertEm2Mark(tag):
    return f'*{tag.string}*'

def convertInlineCode2Mark(tag):
    return f'<code>{tag.string}</code>'

def convertText(tag):
    paragraph = []
    for eachCon in tag.contents:
        if isinstance(eachCon, NavigableString):
            paragraph.append(eachCon)

        elif isinstance(eachCon, Tag):    # tag
            if eachCon.name == 'em':
                paragraph.append(convertEm2Mark(eachCon))

            elif eachCon.name == 'inline_code':
                paragraph.append(convertInlineCode2Mark(eachCon))

            elif eachCon.name == 'a':
                paragraph.append(convertLink2Mark(eachCon))

            else:
                print('[ERROR] missing a tag conversion!')
                raise Exception
        else:
            print('[ERROR] missing an element conversion!')
            raise Exception

    return '#### text-block ####', ''.join(paragraph)

def convertSectionTitle(tag, kind):
    block = ['#### section-title ####']
    if kind == 'section_title':
        block.append(f'content: {tag.text}')
        block.append(FIELD_SEPARATOR)
        block.append('class: default')
    else:
        block.append('content: Workbook')
        block.append(FIELD_SEPARATOR)
        block.append('class: workbook')
    block.append(FIELD_SEPARATOR)
    return block

def convertFigCaption(tag):
    block = ['#### text-block ####']
    block.append('content: ' + f'<figcaption>{tag.string}</figcaption>')
    block.append(FIELD_SEPARATOR)
    return block

def convertExercise(tag):
    block = ['#### exercise ####']
    if tag.exercise_content:

        tagContent = []
        for eachElem in tag.exercise_content.contents:

            if isinstance(eachElem, Tag):
                if eachElem.name == 'p':
                    header, miniBlock = convertText(eachElem)
                    tagContent.append(miniBlock)

                elif eachElem.name == 'ul':
                    miniBlock = convertList(eachElem, noHeader=True)
                    tagContent.append(miniBlock[0].replace('content: ', '\n'))

                else:
                    print('-'*20)
                    print(eachElem)
                    print(eachElem.name)
                    print(tag.exercise_content)
                    print('[ERROR] missing something here')
                    raise Exception

        block.append(f'content: {"".join(tagContent)}')
        block.append(FIELD_SEPARATOR)

    if tag.exercise_image:
        block.append(f"image: {tag.exercise_image['src']}")
        block.append(FIELD_SEPARATOR)
    return block

def convertList(tag, noHeader=False):
    if noHeader is True:
        block = []
    else:
        block = ['#### text-block ####']

    listContent = []
    for eachCon in tag.contents:
        if eachCon.name == 'li':
            singleElement = ['+ ']
            for eachElem in eachCon.contents:

                if isinstance(eachElem, Tag):
                    if eachElem.name == 'em':
                        singleElement.append(convertEm2Mark(eachElem))

                    elif eachElem.name == 'inline_code':
                        singleElement.append(convertInlineCode2Mark(eachElem))

                    elif eachElem.name == 'a':
                        singleElement.append(convertLink2Mark(eachElem))
                    else:
                        print(eachElem.name)
                        print('[ERROR] missing a tag')
                        raise Exception

                elif isinstance(eachElem, NavigableString):
                    singleElement.append(eachElem)

                else:
                    print('[ERROR] missing something here')
                    raise Exception

            listContent.append(''.join(singleElement))

    block.append('content: ' + '\n'.join(listContent))
    block.append(FIELD_SEPARATOR)
    return block

def convertTable(tag, chapterFolder, counter):
    table = []

    headerRows = 0
    if tag.thead:
        for tRow in tag.thead.find_all('tr', recursive=False):
            eachRow = []
            for tagCell in tRow.find_all('th', recursive=False):

                if tagCell.contents:
                    content = tagCell.contents[0]
                    if isinstance(content, Tag) and (content.name == 'code' or content.name == 'inline_code'):
                        tagText = convertInlineCode2Mark(content)
                    else:
                        tagText = tagCell.text
                else:
                    tagText = tagCell.text

                eachRow.append(tagText)
            table.append('\t'.join(eachRow))
        headerRows += 1

    if tag.tbody:
        for tRow in tag.tbody.find_all('tr', recursive=False):
            eachRow = []
            for tagCell in tRow.find_all('td', recursive=False):
                if tagCell.contents:
                    content = tagCell.contents[0]
                    if isinstance(content, Tag) and (content.name == 'code' or content.name == 'inline_code'):
                        tagText = convertInlineCode2Mark(content)
                    else:
                        tagText = tagCell.text
                else:
                    tagText = tagCell.text

                eachRow.append(tagText)
            table.append('\t'.join(eachRow))

    tableFileName = f'{counter:0>2d}.csv'
    with codecs.open(joinPth(chapterFolder, tableFileName), 'w', 'utf-8') as tableFile:
        tableFile.write('\n'.join(table))

    block = ['#### table ####']
    block.append(f'path: {tableFileName}')
    block.append(FIELD_SEPARATOR)

    block.append(f'headers: {headerRows}')
    block.append(FIELD_SEPARATOR)

    return block


def convertLR(lrPath, oldCopy=True):

    # open the file and make the soup
    with codecs.open(lrPath.replace('.lr', '.old.lr'), 'r', 'utf-8') as lrFile:
        lrDoc = lrFile.read()

    pattern = re.compile(r'---\nbody:(.*)', re.DOTALL)
    result = re.search(pattern, lrDoc)

    if result:
        lrBody = result.group(1)  # first parenthesized match group

        tableCounter = 1
        snippetCounter = 1

        flow = []
        textBlocks = []
        block = None
        header = None

        soup = BeautifulSoup(lrBody, 'lxml')
        for eachTag in soup.body.find_all(TAGS, recursive=False):

            # images
            if eachTag.name == 'large_image':
                block = convertImage(eachTag, 'large')

            elif eachTag.name == 'small_image':
                block = convertImage(eachTag, 'small')

            # code-example
            elif eachTag.name == 'pre_code':
                block = convertCodeExampleWithoutImage(eachTag,
                                                       dirname(lrPath),
                                                       snippetCounter)
                snippetCounter += 1

            # text-block
            elif eachTag.name == 'p':
                header, block = convertText(eachTag)

            # section-title
            elif eachTag.name in ['section_title', 'workbook']:
                block = convertSectionTitle(eachTag, eachTag.name)

            # exercise
            elif eachTag.name == 'exercise_wrapper':
                block = convertExercise(eachTag)

            elif eachTag.name == 'code_image_wrapper':
                block = convertCodeImageWrapper(eachTag,
                                                dirname(lrPath),
                                                snippetCounter)
                snippetCounter += 1

            # table
            elif eachTag.name == 'table':
                block = convertTable(eachTag, dirname(lrPath), tableCounter)
                tableCounter += 1

            # list
            elif eachTag.name == 'ul':
                block = convertList(eachTag)

            # figure caption
            elif eachTag.name == 'figcaption':
                block = convertFigCaption(eachTag)

            else:
                print('[ERROR] missing something here!')
                raise Exception

            if eachTag.name == 'p':
                textBlocks.append(block)
            else:
                if len(textBlocks) > 0:
                    paragraphs = "\n\n".join(textBlocks)
                    textBlocks = []
                    paragraphsBlock = [f'{header}', f'content: {paragraphs}', FIELD_SEPARATOR]
                    flow.append('\n'.join(paragraphsBlock))
                flow.append('\n'.join(block))

        # if last tag is 'p'
        if eachTag.name == 'p':
            paragraphs = "\n\n".join(textBlocks)
            textBlocks = []
            paragraphsBlock = [f'{header}', f'content: {paragraphs}', FIELD_SEPARATOR]
            flow.append('\n'.join(paragraphsBlock))

        # substitution
        newHeader = re.sub(pattern, '', lrDoc)
        newBody = '\n'.join(flow)

        with codecs.open(lrPath, 'w', 'utf-8') as newDocFile:
            newDocFile.write(newHeader)
            newDocFile.write(f'---\nbody: {newBody}')


### Instructions
if __name__ == '__main__':
    folders = [
               'a-few-words-about',
               'basic-data-types',
               'coordinates-and-primitives',
               'how-to-browse-sequences',
               'how-to-keep-doing-things-until-you-need-to',
               'how-to-make-choices',
               'should-a-designer-code',
               'strings-encoding-and-unicode',
               'impressum',
               'the-elements-of-a-python-program',
               'transform-strings',
               'typesetting-with-drawbot',
               'using-drawbot',
               'why-this-manual'
               ]

    for eachFolder in folders:
        lrFileName = joinPth('../content', eachFolder, 'contents.lr')
        convertLR(lrFileName)
