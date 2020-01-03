# Constants
FROM_MM_TO_PT = 0.0393701*72
MARGIN = 20*FROM_MM_TO_PT

THICK_LINE = 1
THIN_LINE = .5

# Functions & Procedures
def typeQualities():
    font('InputMono-Regular')
    fontSize(8)
    lineHeight(10)
    fill(0)
    stroke(None)

def lineQuality(thickness):
    fill(None)
    stroke(0)
    strokeWidth(thickness)

def drawRuler(xx, converter, stepOne, stepTwo, stepThree):
    quota = height()-MARGIN
    index = 0
    while quota >= MARGIN:
        if index % stepOne == 0:
            length = 12*FROM_MM_TO_PT
            typeQualities()
            text(f'{index}', (xx+length+4, quota))
            lineQuality(THICK_LINE)
        elif index % stepTwo == 0:
            length = 8*FROM_MM_TO_PT
            lineQuality(THIN_LINE)
        elif index % stepThree == 0:
            length = 5*FROM_MM_TO_PT
            lineQuality(THIN_LINE)
        else:
            length = 0
            lineQuality(0)

        line((xx, quota), (xx+length, quota))
        quota -= 1*converter
        index += 1


if __name__ == '__main__':
    ### Instructions
    size('A4')

    stroke(0)
    strokeWidth(.5)
    offsetRuler = MARGIN
    drawRuler(xx=offsetRuler,
              converter=FROM_MM_TO_PT,
              stepOne=10,
              stepTwo=5,
              stepThree=1)

    offsetRuler += 40*FROM_MM_TO_PT
    drawRuler(xx=offsetRuler,
              converter=1,
              stepOne=12,
              stepTwo=6,
              stepThree=2)
