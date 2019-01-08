shades = 10
newPage(100, 100)

shadeWidth = width()/shades
for shadeIndex in range(shades):
    grayscaleValue = 1 - (1/(shades-1)*shadeIndex)
    fill(grayscaleValue)
    rect(shadeIndex*shadeWidth, 0, shadeWidth, height())