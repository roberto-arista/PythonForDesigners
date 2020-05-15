from math import sqrt

RADIUS = 5

def calcDistance(pt1, pt2):
    return sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

def closestPoint(refPt, points):
    return min(points, key=lambda x: calcDistance(refPt, x))

def drawPt(point):
    oval(point[0]-RADIUS, point[1]-RADIUS, RADIUS*2, RADIUS*2)


if __name__ == '__main__':
    points = [(311, 168), (204, 320), (134, 339), (185, 23), (0, 171), (227, 139), (172, 372), (388, 231), (142, 169), (167, 102), (368, 0), (40, 97), (166, 206), (263, 27), (157, 53), (5, 168), (285, 249), (34, 228), (174, 86), (55, 271), (350, 240), (238, 71), (56, 154), (116, 297), (165, 122), (297, 296), (392, 386), (124, 50), (193, 58), (389, 117), (387, 67), (353, 260), (245, 332), (133, 155), (73, 165), (231, 192), (89, 238), (300, 356), (31, 158), (100, 375), (12, 54), (358, 136), (179, 123), (293, 207), (59, 331), (377, 309), (50, 47), (277, 243), (117, 2), (18, 189)]
    refPt = 95, 180
    closest = closestPoint(refPt, points)

    newPage(400, 400)
    fill(0)
    for eachPt in points:
        if eachPt != closest:
            drawPt(eachPt)

    fill(1, 0, 0)
    drawPt(closest)

    fill(0, 1, 0)
    drawPt(refPt)
