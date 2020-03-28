def lerp(aa, bb, factor):
    return aa + (bb - aa) * factor


if __name__ == '__main__':
    mid = lerp(10, 20, .5)
    # 15.0
