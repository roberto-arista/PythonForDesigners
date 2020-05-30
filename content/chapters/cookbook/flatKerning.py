### Modules
from fontParts.world import OpenFont

### Functions
if __name__ == '__main__':
    ff = OpenFont('someFont.ufo')
    flatKerning = ff.getFlatKerning()
    print(flatKerning)
    # {('A', 'V'): -80, ('Agrave', 'V'): -80, ('Aacute', 'V'): -80}
