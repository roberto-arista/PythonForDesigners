canvasSide = 200

newPage(canvasSide, canvasSide)
center = (canvasSide/2, canvasSide/2)

fill(.2)
polygon((0, 0),
        (0, canvasSide),
        center)

fill(.4)
polygon((0, 0),
        (canvasSide, 0),
        center)

fill(.6)
polygon((canvasSide, 0),
        (canvasSide, canvasSide),
        center)

fill(.8)
polygon((canvasSide, canvasSide),
        (0, canvasSide),
        center)