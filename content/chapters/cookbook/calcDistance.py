from math import sqrt

def calcDistance(pt1, pt2):
    return sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

if __name__ == '__main__':
    dist = calcDistance((20, 30), (100, 80))
    # 94.33981132056604