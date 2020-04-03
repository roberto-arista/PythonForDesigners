kerning = {
    ('A', 'V'): -80,
    ('V', 'A'): -80,
    ('L', 'A'): -20,
    ('A', 'W'): -60
}

corrections = list(kerning.values())
corrections.sort()
# >>> [-80, -80, -60, -20]

minCorrection, maxCorrection = abs(corrections[0]), abs(corrections[-1])
# >>> 80 20

reference = maxCorrection if minCorrection < maxCorrection else minCorrection
# >>> 80