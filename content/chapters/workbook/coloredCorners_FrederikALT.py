#!/usr/bin/env python3
# coding: utf-8

# -------------------------------------------------------------------------------- #
# Colored Corners, alternative solution by Frederik Berlaen https://typemytype.com #
# -------------------------------------------------------------------------------- #

# --- Modules --- #
from drawBot import newPage, fill, oval, blendMode, BezierPath, clipPath, radialGradient, rect

# --- Variables --- #
originX, originY = 0, 0
canvasWdt = canvasHgt = 200
circles = 3
offset = 20
thickness = 26

color1 = (0, 1, 1)
color2 = (1, .5, 0)
color3 = (1, 0, 1)
color4 = (1, 1, 0)

# --- Instructions --- #
if __name__ == '__main__':
    colorMap = [
        (originX, originY, color1),
        (originX + canvasWdt, originY, color2),
        (originX, originY + canvasHgt, color3),
        (originX + canvasWdt, originY + canvasHgt, color4),
    ]

    newPage(canvasWdt, canvasHgt)

    # corners
    for cx, cy, color in colorMap:
        fill(*color)
        oval(cx-thickness, cy-thickness, thickness*2, thickness*2)

    # rings
    blendMode("multiply")
    path = BezierPath()
    for i in range(circles):
        factor = i / (circles - 1)
        inset = offset + (canvasWdt / 2-offset*2) * factor
        path.oval(originX+inset, originY+inset, canvasWdt-inset*2, canvasHgt-inset*2)
    path = path.expandStroke(thickness)
    clipPath(path)

    for cx, cy, color in colorMap:
        radialGradient((cx, cy), (cx, cy), [color, (1, 1, 1, 0)], startRadius=0, endRadius=canvasWdt)
        rect(originX, originY, canvasWdt, canvasHgt)
