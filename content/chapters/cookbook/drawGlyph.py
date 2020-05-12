import fontParts.world as fp

def drawGlyph(glyph):
    """
    from https://gist.github.com/roberto-arista/e916e3c9c0ab445b2bfb714af80dab6b#gistcomment-2828756
    thanks Frederik!
    """
    glyphPath = BezierPath(glyphSet=glyph.layer)
    glyph.draw(glyphPath)
    drawPath(glyphPath)


if __name__ == '__main__':
    myFont = fp.OpenFont('someFont.ufo')
    drawGlyph(myFont['a'])
