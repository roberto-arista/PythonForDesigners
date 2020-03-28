def lerp(aa, bb, factor):
    return aa + (bb - aa) * factor

def getFactor(aa, bb, innerValue):
    return (innerValue-aa)/(bb-aa)

def remapValue(val, pMin, pMax, nMin, nMax):
    factor = getFactor(pMin, pMax, val)
    nVal = lerp(nMin, nMax, factor)
    return nVal


if __name__ == '__main__':
    newVal = remapValue(2, 0, 10, -1, +1)
    # -0.6