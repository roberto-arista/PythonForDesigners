size(200, 200)

assert width() == height(), 'the canvas should be squared'


step = 10

stroke(0)
strokeWidth(2)

shiftin = 0
while shiftin <= width():

    ptBtm = shiftin, 0
    ptRgt = width(), shiftin
    ptTop = width()-shiftin, height()
    ptLft = 0, height()-shiftin

    line(ptBtm, ptRgt)
    line(ptTop, ptLft)

    shiftin += step