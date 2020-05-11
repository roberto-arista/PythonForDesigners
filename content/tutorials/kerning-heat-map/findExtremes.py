from itertools import product
from collections import defaultdict

kerning = defaultdict(int)
kerning.setdefault(0)

kerning[('A', 'V')] = -80
kerning[('V', 'A')] = -80
kerning[('L', 'A')] =  20
kerning[('A', 'W')] = -60
kerning[('P', 'a')] = -120

glyphNames = 'ALVPW'

corrections = [kerning[nn] for nn in product(glyphNames, repeat=2)]
corrections.sort()
print(corrections)
# >>> [-80, -80, -60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20]
# 120 was discarded, glyphNames does not contain 'a'

minCorr, maxCorr = corrections[0], corrections[-1]
# >>> -80 20

reference = abs(maxCorr) if abs(minCorr) < abs(maxCorr) else abs(minCorr)
# >>> 80
