size(200, 200)

stripeHgt = 40
gradStep = 2

yy = 0
while yy <= height():

    indexStripe = yy/stripeHgt

    xx = 0
    while xx <= width():

        if indexStripe % 2 == 0:
            fill(xx/width())
        else:
            fill(1-xx/width())

        rect(xx, yy, gradStep, stripeHgt)
        xx += gradStep

    yy += stripeHgt
