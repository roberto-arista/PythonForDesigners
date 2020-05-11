# Modules
import csv
from colorsys import rgb_to_hls

from drawBot import newPage, height, fill, stroke
from drawBot import font, rect, text, openTypeFeatures

# Constants
FROM_MM_TO_PT = 0.0393701*72
CELL_HGT = 24
MARGIN = 20*FROM_MM_TO_PT
FIGURE_SPACE = '\u2007'

SWA_X = 15*FROM_MM_TO_PT
NAM_X = 48*FROM_MM_TO_PT
HLS_X = 130*FROM_MM_TO_PT
RGB_X = 165*FROM_MM_TO_PT
HEX_X = 180*FROM_MM_TO_PT

BLACK = 0, 0, 0
WHITE = 1, 1, 1

# Function
def loadTable(fileName):
    with open(fileName, mode='r', encoding='utf-8') as csvFile:
        colorReader = csv.reader(csvFile, delimiter='\t')
        return list(colorReader)

def initPage():
    newPage('A4')
    quota = height()-MARGIN
    drawHeader(quota)
    quota -= CELL_HGT
    return quota

def drawHeader(quota):
    typeQualities(isBold=True)
    text('Swatch', (SWA_X, quota))
    text('Name', (NAM_X, quota))
    text('HLS', (HLS_X, quota), align='right')
    text('RGB', (RGB_X, quota), align='right')
    text('HEX', (HEX_X, quota))

def typeQualities(isBold=False):
    fill(*BLACK)
    stroke(None)
    openTypeFeatures(tnum=True)
    if isBold is False:
        font('.SFNS-Regular', 9)
    else:
        font('.SFNS-Bold', 9)

def fromHEX2RGB(hexColor):
    assert hexColor.startswith('#'), 'hex color should start with #'
    rr = int(hexColor[1:3], 16)
    gg = int(hexColor[3:5], 16)
    bb = int(hexColor[5:], 16)
    return (rr, gg, bb)


# Variables
fileName = 'colors.csv'

# Instructions
quota = initPage()
for colorName, hexColor in loadTable(fileName):
    rgbColor = fromHEX2RGB(hexColor)
    rgbFloatColor = [ch/255 for ch in rgbColor]

    # swatch
    fill(*rgbFloatColor)
    rect(SWA_X, quota-4, 80, CELL_HGT*.7)

    # name
    typeQualities()
    text(colorName, (NAM_X, quota))

    # hls
    hh, ll, ss = rgb_to_hls(*rgbFloatColor)
    hlsStr = f'{hh*360:\u2007>3.0f}°{FIGURE_SPACE}{ll*100:\u2007>3.0f}%{FIGURE_SPACE}{ss*100:\u2007>3.0f}%'
    text(hlsStr, (HLS_X, quota), align='right')

    # rgb
    rr, gg, bb = rgbColor
    rgbStr = f'{rr:\u2007>3}{FIGURE_SPACE}{gg:\u2007>3}{FIGURE_SPACE}{bb:\u2007>3}'
    text(rgbStr, (RGB_X, quota), align='right')

    # hex
    text(hexColor, (HEX_X, quota), align='left')

    quota -= CELL_HGT
    if quota < MARGIN:
        quota = initPage()
