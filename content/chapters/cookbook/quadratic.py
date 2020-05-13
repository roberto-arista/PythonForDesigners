def quadraticCurve(wdt, aa, bb):
    points = []
    for xx in range(-wdt//2, wdt//2):
        yy = (aa*xx)**2 + bb*xx
        points.append((xx, yy))
    return points


if __name__ == '__main__':
    points = quadraticCurve(wdt=300, aa=.13, bb=0)
    newPage(500, 500)
    translate(width()/2, 50)
    stroke(0)
    fill(None)
    strokeWidth(10)
    polygon(*points, close=False)
