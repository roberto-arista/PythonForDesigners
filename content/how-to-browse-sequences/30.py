stripes = 10
newPage(100, 100)

stripeWidth = width()/stripes
for stripeIndex in range(stripes):
    if stripeIndex % 2 == 0:
            fill(0)
    else:
            fill(1)
    rect(stripeIndex*stripeWidth, 0, stripeWidth, height())