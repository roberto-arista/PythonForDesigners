canvasSide = 200

newPage(canvasSide, canvasSide)
factor = .75

fill(.6)
polygon((0, 0),
        (0, canvasSide),
        (canvasSide/2*factor, canvasSide/2))

fill(.4)
polygon((0, 0),
        (canvasSide, 0),
        (canvasSide/2, canvasSide/2*factor))

fill(.2)
polygon((canvasSide, 0),
        (canvasSide, canvasSide),
        (canvasSide-canvasSide/2*factor, canvasSide/2))

fill(.0)
polygon((canvasSide, canvasSide),
         (0, canvasSide),
         (canvasSide/2, canvasSide-canvasSide/2*factor))