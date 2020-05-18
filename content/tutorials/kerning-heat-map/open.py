from fontParts.world import OpenFont
myFont = OpenFont('Source Serif Pro Regular.ufo')
print(myFont.info.familyName, myFont.info.styleName)
# >>> Source Serif Pro Regular
print(myFont.kerning)
# >>> <RKerning for font 'Source Serif Pro Regular' path='Source Serif Pro Regular.ufo' at 4412747344>
print(len(myFont.kerning))
# >>> 7970
