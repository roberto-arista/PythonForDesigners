from fontParts.world import OpenFont
myFont = OpenFont('Source Serif Pro Regular.ufo')

for pair, correction in myFont.kerning.items():
    first, second = pair
    print(f'{first} vs {second} = {correction}')

    # here a selection of the different kinds of kerning pairs (with example)
    # group vs group
    # >>> public.kern1.periodcentered vs public.kern2.LAT_T = -40

    # group vs glyph
    # >>> public.kern1.zero.lf vs AE = -21

    # glyph vs group
    # >>> zeta vs public.kern2.GRK_alpha = -20

    # glyph vs glyps
    # >>> B vs AE = -50
