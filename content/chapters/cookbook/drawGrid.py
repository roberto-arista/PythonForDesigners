def drawGrid(hElems, vElems, cellSize):
    """
    hElems = horizontal elements
    vElems = vertical elements
    """
    for jj in range(vElems):
        with savedState():
            for ii in range(hElems):
                rect(0, 0, cellSize, cellSize)
                translate(cellSize, 0)
        translate(0, cellSize)


if __name__ == '__main__':
    newPage(400, 400)
    stroke(0)
    strokeWidth(10)
    fill(None)
    translate(60, 60)
    drawGrid(8, 8, 30)
