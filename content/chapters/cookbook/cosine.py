from math import cos, radians

def cosineCurve(wdt, radius):
    points = []
    for xx in range(0, wdt):
        yy = cos(radians(xx*(360/wdt))) * radius
        points.append((xx, yy))
    return points


if __name__ == '__main__':
    points = cosineCurve(450, 200)
    newPage(500, 500)
    translate(25, height()*.5)
    stroke(0)
    fill(None)
    strokeWidth(10)
    polygon(*points, close=False)
