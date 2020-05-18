newPage(200, 200)
stroke(0)

gutter = 8
cols = 3
rows = 3

xx = width()/cols*1
line((xx-gutter/2, 0), (xx-gutter/2, height()))
line((xx+gutter/2, 0), (xx+gutter/2, height()))

xx = width()/cols*2
line((xx-gutter/2, 0), (xx-gutter/2, height()))
line((xx+gutter/2, 0), (xx+gutter/2, height()))

yy = height()/rows*1
line((0, yy-gutter/2), (width(), yy-gutter/2))
line((0, yy+gutter/2), (width(), yy+gutter/2))

yy = height()/rows*2
line((0, yy-gutter/2), (width(), yy-gutter/2))
line((0, yy+gutter/2), (width(), yy+gutter/2))
