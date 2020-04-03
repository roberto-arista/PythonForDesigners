kerning = {
    ('A', 'V'): -80,
    ('V', 'A'): -80,
    ('L', 'A'): -20,
    ('A', 'W'): -60
}

corrections = list(kerning.values())
corrections.sort()
# >>> [-80, -80, -60, -20]

minCorrection, maxCorrection = corrections[0], corrections[-1]
# >>> 80 20

reference = abs(maxCorrection) if abs(minCorrection) < abs(maxCorrection) else abs(minCorrection)
# >>> 80
