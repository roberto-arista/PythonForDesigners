def HEX2RGB(hexColor):
    offset = 1 if hexColor.startswith('#') else 0
    rr = int(hexColor[offset:offset+2], 16)
    gg = int(hexColor[offset+2:offset+4], 16)
    bb = int(hexColor[offset+4:], 16)
    return rr, gg, bb


if __name__ == '__main__':
    rgbColor = HEX2RGB('#DC7814')
    print(rgbColor)
