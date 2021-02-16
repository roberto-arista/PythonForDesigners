# Modules
import unicodedata

# Constants
FROM_MM_TO_PT = 0.0393701*72

BIN_X = 25 * FROM_MM_TO_PT
INT_X = 45 * FROM_MM_TO_PT
HEX_X = 60 * FROM_MM_TO_PT
CHR_X = 90 * FROM_MM_TO_PT
DES_X = 120 * FROM_MM_TO_PT

CELL_HEIGHT = 16
MARGIN = 18 * FROM_MM_TO_PT

BLACK = 0, 0, 0
GRAY = .6, .6, .6

# Functions
def typeQualities(isBold=False):
    openTypeFeatures(tnum=True)
    if not isBold:
        font('.SFNS-Regular', 10)
    else:
        font('.SFNS-Bold', 10)
    fill(*BLACK)
    stroke(None)

def getUniDescription(char):
    """Provide a character and I will return a description
    if available in the Unicode database"""
    try:
        return unicodedata.name(char)
    except ValueError:
        return ''

def drawHeader(yy):
    typeQualities(isBold=True)
    text('binary', (BIN_X, yy), align='right')
    text('int10', (INT_X, yy), align='right')
    text('utf-8', (HEX_X, yy), align='left')
    text('character', (CHR_X, yy), align='left')
    text('description', (DES_X, yy), align='left')

def initPage():
    newPage('A4')
    typeQualities()
    text(f'page: {pageCount()}', (width()/2, MARGIN/2), align='center')
    yy = height() - MARGIN
    drawHeader(yy)
    yy -= CELL_HEIGHT
    return yy

def drawTableRow(ii, description, yy):
    text(f'{ii:b}', (BIN_X, yy), align='right')
    text(f'{ii}', (INT_X, yy), align='right')
    text(f'U+{ii:0>4X}', (HEX_X, yy), align='left')

    fs = FormattedString(font='.SFNS-Regular', fontSize=10)
    fs.append('|', fill=GRAY)
    fs.append(f'{ii:c}', fill=BLACK)
    fs.append('|', fill=GRAY)
    text(fs, (CHR_X, yy), align='left')

    text(description, (DES_X, yy), align='left')


# Variables
start = 32
end = 256

# Instructions
if __name__ == '__main__':
    yy = initPage()
    for ii in range(start, end):
        description = getUniDescription(f'{ii:c}')

        if description:
            typeQualities()
            drawTableRow(ii, description, yy)
            yy -= CELL_HEIGHT

            if yy <= MARGIN:
                yy = initPage()
