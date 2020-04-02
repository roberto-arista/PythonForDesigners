### Constants
FIRST_PREFIX = 'public.kern1.'
SECOND_PREFIX = 'public.kern2.'

### Functions
def flatKerning(aFont):
    flatKerning = {}

    for pair, correction in aFont.kerning.items():
        first, second = pair

        # both groups
        if first.startswith(FIRST_PREFIX) and second.startswith(SECOND_PREFIX):
            for firstGlyph in aFont.groups[first]:
                for secondGlyph in aFont.groups[second]:
                    flatKerning[(firstGlyph, secondGlyph)] = correction

        # first group, second glyph
        elif first.startswith(FIRST_PREFIX):
            for firstGlyph in aFont.groups[first]:
                flatKerning[(firstGlyph, second)] = correction

        # first glyph, second group
        elif second.startswith(SECOND_PREFIX):
            for secondGlyph in aFont.groups[second]:
                flatKerning[(first, secondGlyph)] = correction

        # first glyph, second glyph
        else:
            flatKerning[(first, second)] = correction

    return flatKerning


### Instructions
if __name__ == '__main__':
    from fontParts.world import OpenFont
    fontName = 'Source Serif Pro Regular.ufo'

    thisFont = OpenFont(fontName)
    print(len(thisFont.kerning))
    # 7970

    flat = flatKerning(thisFont)
    print(len(flat))
    # 237806 😅
