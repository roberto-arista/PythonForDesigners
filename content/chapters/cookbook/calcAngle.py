from math import atan2, degrees

def calcAngle(pt1, pt2, mode='degrees'):
    assert mode == 'degrees' or mode == 'radians'
    ang = atan2((pt2[1] - pt1[1]), (pt2[0] - pt1[0]))
    if mode == 'radians':
        return ang
    else:
        return degrees(ang)


if __name__ == '__main__':
    angle = calcAngle((50, 50), (10, 80), mode='degrees')
    # 143.13010235415598

    angle = calcAngle((50, 50), (10, 80), mode='radians')
    # 2.498091544796509