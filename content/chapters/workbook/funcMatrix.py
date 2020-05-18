# Modules
from drawBot import font, lineHeight, fill, stroke, newPage, savedState, openTypeFeatures
from drawBot import translate, rect, textSize, text, fontAscender, width, height, saveImage

from fractions import Fraction
from operator import add, mul, pow, truediv, sub

# Constants
WHITE = 1, 1, 1

# Functions
def background(clr):
    fill(*clr)
    rect(0, 0, width(), height())

def typeQualities(bodySize, leading):
    font('.SFNS-Regular', bodySize)
    lineHeight(leading)
    fill(0)
    stroke(None)

def lineQualities():
    stroke(0)
    fill(None)

def caption(name):
    typeQualities(12, 12)
    text(name, (width()/2, height()-20), align='center')


# Variables
cellSize = margin = 30
startValue = 3
endValue = 12    # included

operations = {
    'multiplication': mul,
    'addition': add,
    'difference': sub,
    'division': truediv,
    'power of': pow,
}

# Instructions
assert endValue > startValue
canvasSize = (endValue-startValue+1)*cellSize + margin*2

for name, func in operations.items():
    newPage(canvasSize, canvasSize)
    background(WHITE)
    caption(name)

    translate(margin, margin)
    for jj in range(startValue, endValue+1):
        indexJ = jj - startValue
        typeQualities(8, 9)
        text(f'{jj}', (-cellSize*.25, indexJ*cellSize + cellSize/2-fontAscender()/2.5), align='right')

        for ii in range(startValue, endValue+1):
            indexI = ii - startValue
            if indexJ == 1:
                typeQualities(8, 9)
                text(f'{ii}', ((indexI+.5)*cellSize, -cellSize/2), align='center')

            with savedState():
                translate(indexI*cellSize, indexJ*cellSize)

                lineQualities()
                rect(0, 0, cellSize, cellSize)

                typeQualities(14, 14)
                openTypeFeatures(frac=False, tnum=True)
                result = func(jj, ii)

                # decimal
                if result % 1 != 0:
                    resultStr = f'{Fraction(jj, ii)}'
                    openTypeFeatures(frac=True, tnum=False)

                # big values
                elif abs(result) > 99:   # 3 digits at least (and maybe a minus)
                    txtWdt, txtHgt = textSize(f'{int(result)}')
                    bodySize = 15
                    while txtWdt > (cellSize-4) and bodySize > 0:
                        bodySize -= .25
                        typeQualities(bodySize, bodySize)
                        txtWdt, txtHgt = textSize(f'{int(result)}')
                    resultStr = f'{int(result)}'

                else:
                    resultStr = f'{int(result)}'

                text(resultStr, (cellSize/2, cellSize/2-fontAscender()/2.5), align='center')
