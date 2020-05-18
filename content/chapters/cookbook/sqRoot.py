from math import sqrt

def sqRootCurve(wdt, yScale):
    points = []
    for xx in range(0, wdt):
        yy = sqrt(xx)
        points.append((xx, yy*yScale))
    return points


if __name__ == '__main__':
    points = sqRootCurve(wdt=450, yScale=12)
    newPage(500, 500)
    translate(25, 100)
    stroke(0)
    fill(None)
    strokeWidth(10)
    polygon(*points, close=False)
