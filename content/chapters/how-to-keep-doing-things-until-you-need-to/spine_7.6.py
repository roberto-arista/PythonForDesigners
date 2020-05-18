
size(200, 200)

step = 20
margin = 20
maxThickness = 10

stroke(0)

halfHeight = height()/2

yy = margin
while yy <= height()-margin:

    xx = margin
    while xx <= width()-margin:

        if xx > halfHeight:
            strokeWidth(maxThickness-maxThickness*((xx-halfHeight)/halfHeight))
        else:
            strokeWidth(maxThickness*(xx/halfHeight))

        line((xx-step*.35, yy), (xx+step*.35, yy))
        xx += step

    yy += step
