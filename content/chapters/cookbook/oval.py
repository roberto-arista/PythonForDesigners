from math import sin, cos, radians

def ovalCurve(wdt, hgt):
    points = []
    for angle in range(360):
        xx = sin(radians(angle)) * wdt/2
        yy = cos(radians(angle)) * hgt/2
        points.append((xx, yy))
    return points


if __name__ == '__main__':
    points = ovalCurve(400, 150)
    newPage(500, 500)
    translate(width()*.5, height()*.5)
    stroke(0)
    fill(None)
    strokeWidth(10)
    polygon(*points, close=True)
