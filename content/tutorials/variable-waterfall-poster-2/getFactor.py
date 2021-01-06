def getFactor(aa, bb, innerValue):
    return (innerValue-aa)/(bb-aa)


if __name__ == '__main__':
    interval = 1, 2
    ff = getFactor(*interval, 1.5)
    print(ff)
    # 0.5
