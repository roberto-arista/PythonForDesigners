def lerp(aa, bb, factor):
    return aa + (bb-aa) * factor


if __name__ == '__main__':
    intervalWidths = 10, 20
    value = lerp(*intervalWidths, .5)
    print(value)
    # 15
