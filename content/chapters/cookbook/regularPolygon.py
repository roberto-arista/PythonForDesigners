from math import cos, sin, radians

def regularPolygon(sides, radius):
    vertices = []
    sliceAngle = 360/sides
    for ii in range(sides):
        xx = cos(radians(ii*sliceAngle)) * radius
        yy = sin(radians(ii*sliceAngle)) * radius
        vertices.append((xx, yy))
    polygon(*vertices)


if __name__ == '__main__':
    newPage(500, 500)
    translate(width()/2, height()/2)
    regularPolygon(sides=8, radius=200)
