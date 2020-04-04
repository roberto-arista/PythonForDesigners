kerning = {
    ('A', 'V'): -80,
    ('V', 'A'): -80,
    ('L', 'A'): -20,
    ('A', 'W'): -60,
    ('P', 'a'): -120,
}
glyphNames = 'ALVPW'

corrections = [corr for (pair, corr) in kerning.items()
               if pair[0] in glyphNames and pair[1] in glyphNames]
corrections.sort()
# >>> [-80, -80, -60, -20]
# 120 was discarded, glyphNames does not contain 'a'

minCorr, maxCorr = corrections[0], corrections[-1]
# >>> 80 20

reference = abs(maxCorr) if abs(minCorr) < abs(maxCorr) else abs(minCorr)
# >>> 80
