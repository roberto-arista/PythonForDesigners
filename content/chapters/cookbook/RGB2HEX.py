def RGB2HEX(rr, gg, bb):
    return f'#{rr:0>2X}{gg:0>2X}{bb:0>2X}'

if __name__ == '__main__':
    hexColor = RGB2HEX(220, 120, 20)
    # '#DC7814'