from drawBot import newPage, fill, rect, width, height, blendMode
from drawBot import image, saveImage, translate, scale

WHITE = 1, 1, 1

def background(clr=WHITE):
    fill(*clr)
    rect(0, 0, width(), height())


if __name__ == '__main__':
    newPage(7200, 3600)
    background()
    blendMode('multiply')

    translate(1550, 130)
    scale(3.15)
    image('noordzijCubeAxon.pdf', (0, 0))
    saveImage('noordzij_cube.png')
