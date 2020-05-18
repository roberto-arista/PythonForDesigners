def bartlettCurve(aa, wdt):
    points = []
    for xx in range(-wdt//2, wdt//2):
        yy = 1-(abs(xx))/aa
        points.append((xx, yy))
    return points


if __name__ == '__main__':
    points = bartlettCurve(.5, 400)
    newPage(500, 500)
    translate(width()*.5, height()*.9)
    stroke(0)
    fill(None)
    strokeWidth(10)
    polygon(*points, close=False)