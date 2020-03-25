FULL_CIRCLE = 360

for angle in range(FULL_CIRCLE):
    hue = angle / FULL_CIRCLE
    print(f'{angle} / {FULL_CIRCLE} = {hue:.3f}')