side = 20
newPage(200, 200)
quota = height()
while quota > 0:
    quota -= side

    if (quota/side+1) % 2 == 0:
        fill(.8)
    else:
        fill(.2)

    rect(0, quota, side, side)