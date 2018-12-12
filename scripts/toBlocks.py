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
        'table',
        'ul',
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

def convertCodeExample(tag, chapterFolder, counter):
    block = ['#### code-example ####']
    if tag.previous_sibling == 'code_image':
        block.append(f"image: {tag['src']}")
        block.append(FIELD_SEPARATOR)
    snippetName = f'{counter:0>2d}.py'
    with codecs.open(joinPth(chapterFolder, snippetName), 'w', 'utf-8') as snippetFile:
        snippetFile.write(tag.text)
        block.append(f'path: {snippetName}')
        block.append(FIELD_SEPARATOR)
    return block

def convertText(tag):
    paragraph = []
    for eachCon in tag.contents:
        if isinstance(eachCon, NavigableString):
            paragraph.append(eachCon)

        elif isinstance(eachCon, Tag):    # tag
            if eachCon.name == 'em':
                paragraph.append(f'*{eachCon.string}*')

            elif eachCon.name == 'inline_code':
                paragraph.append(f'`{eachCon.string}`')

            elif eachCon.name == 'a':
                paragraph.append(f'[{eachCon.string}]({eachCon["href"]})')

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

def convertExercise(tag):
    block = ['#### exercise ####']
    if tag.exercise_content:
        block.append(f'content: {tag.exercise_content.text}')
        block.append(FIELD_SEPARATOR)
    if tag.exercise_image:
        block.append(f"image: {tag.exercise_image['src']}")
        block.append(FIELD_SEPARATOR)
    return block

def convertList(tag):
    block = ['#### text-block ####']
    listContent = []
    for eachCon in tag.contents:
        if eachCon.name == 'li':
            singleElement = ['+ ']
            for eachElem in eachCon.contents:
                if isinstance(eachElem, Tag):
                    singleElement.append(f'<code>{eachElem.text}</code>')
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
                        tagText = f'<code>{content.text}</code>'
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
                        tagText = f'<code>{content.text}</code>'
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

    # list

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

            if eachTag.name == 'small_image':
                block = convertImage(eachTag, 'small')

            # code-example
            if eachTag.name == 'pre_code':
                block = convertCodeExample(eachTag,
                                           dirname(lrPath),
                                           snippetCounter)
                snippetCounter += 1

            # text-block
            if eachTag.name == 'p':
                header, block = convertText(eachTag)

            # section-title
            if eachTag.name in ['section_title', 'workbook']:
                block = convertSectionTitle(eachTag, eachTag.name)

            # exercise
            if eachTag.name == 'exercise_wrapper':
                block = convertExercise(eachTag)

            # table
            if eachTag.name == 'table':
                block = convertTable(eachTag, dirname(lrPath), tableCounter)
                tableCounter += 1

            # list
            if eachTag.name == 'ul':
                block = convertList(eachTag)

            if eachTag.name == 'p':
                textBlocks.append(block)
            else:
                if len(textBlocks) > 0:
                    paragraphs = "\n\n".join(textBlocks)
                    textBlocks = []
                    paragraphsBlock = [f'{header}', f'content: {paragraphs}', FIELD_SEPARATOR]
                    flow.append('\n'.join(paragraphsBlock))
                flow.append('\n'.join(block))

        # substitution
        newHeader = re.sub(pattern, '', lrDoc)
        newBody = '\n'.join(flow)

        with codecs.open(lrPath, 'w', 'utf-8') as newDocFile:
            newDocFile.write(newHeader)
            newDocFile.write(f'---\nbody: {newBody}')


### Variables
tableText = """<table>
    <thead>
        <tr>
            <th>Expression</th>
            <th>Output</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>not True</code></td>
            <td><code>False</code></td>
        </tr>

        <tr>
            <td><code>not False</code></td>
            <td><code>True</code></td>
        </tr>

        <tr>
            <td><code>True and True</code></td>
            <td><code>True</code></td>
        </tr>

        <tr>
            <td><code>False and True</code></td>
            <td><code>False</code></td>
        </tr>

        <tr>
            <td><code>False and False</code></td>
            <td><code>False</code></td>
        </tr>

        <tr>
            <td><code>True or True</code></td>
            <td><code>True</code></td>
        </tr>

        <tr>
            <td><code>True or False</code></td>
            <td><code>True</code></td>
        </tr>

        <tr>
            <td><code>False or False</code></td>
            <td><code>False</code></td>
        </tr>

    </tbody>
</table>"""

### Instructions
if __name__ == '__main__':
    folders = ['a-few-words-about',
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
               'why-this-manual']

    for eachFolder in folders:
        lrFileName = joinPth('../content', eachFolder, 'contents.lr')
        convertLR(lrFileName)
