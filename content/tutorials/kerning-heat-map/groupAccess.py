from fontParts.world import OpenFont
myFont = OpenFont('Source Serif Pro Regular.ufo')

glyphSet = myFont.groups['public.kern1.zero.lf']
print(glyphSet)
# >>> ('zero.lf', 'zero.lfslash', 'zero.cap')
