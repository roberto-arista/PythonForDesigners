def lerp(aa, bb, factor):
    return aa + (bb - aa) * factor

def lerpRGB(colorOne, colorTwo, factor):
    rr = lerp(colorOne[0], colorTwo[0], factor)
    gg = lerp(colorOne[1], colorTwo[1], factor)
    bb = lerp(colorOne[2], colorTwo[2], factor)
    return rr, gg, bb

if __name__ == '__main__':
    red = 255, 0, 0
    blue = 0, 0, 255
    gradient = lerpRGB(red, blue, .5)
    # (127.5, 0.0, 127.5)

    red = 1, 0, 0
    blue = 0, 0, 1
    gradient = lerpRGB(red, blue, .5)
    # (0.5, 0.0, 0.5)
