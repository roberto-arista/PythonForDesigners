canvas = 200
factor = .75

newPage(canvas, canvas)

fill(.2)
polygon((0, 0),
        (0, canvas),
        (canvas/2*factor, canvas/2))

fill(.4)
polygon((0, 0),
        (canvas, 0),
        (canvas/2, canvas/2*factor))

fill(.6)
polygon((canvas, 0),
        (canvas, canvas),
        (width()-canvas/2*factor, canvas/2))

fill(.8)
polygon((canvas, canvas),
        (0, canvas),
        (canvas/2, height()-canvas/2*factor))