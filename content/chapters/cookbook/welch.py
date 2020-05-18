def welchCurve(aa, wdt):
    points = []
    for xx in range(-wdt//2, wdt//2+1):
        yy = 1 - (xx**2 / aa**2)
        points.append((xx, yy))
    return points


if __name__ == '__main__':
    points = welchCurve(5, 200)
    newPage(500, 500)
    translate(width()*.5, height()*.9)
    stroke(0)
    fill(None)
    strokeWidth(10)
    polygon(*points, close=False)