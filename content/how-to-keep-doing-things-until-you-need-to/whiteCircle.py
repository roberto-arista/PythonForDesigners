newPage(200, 200)
step = 5
stroke(0)

jumpin = 0
while jumpin <= width()/2:

    # btm rgt
    line((width()/2+jumpin, 0), (width(), jumpin))

    # top rgt
    line((width(), height()/2+jumpin), (width()-jumpin, height()))

    # top lft
    line((width()/2-jumpin, height()), (0, height()-jumpin))

    # btm lft
    line((0, height()/2-jumpin), (jumpin, 0))

    jumpin += step
