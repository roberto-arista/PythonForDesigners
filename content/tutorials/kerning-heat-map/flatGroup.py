groups = {'public.kern1.A': ('A', 'Agrave', 'Aacute')}
kerning = {('public.kern1.A', 'V'): -80}

flat = {}
for pair, correction in kerning.items():
    first, second = pair

    for glyphName in groups[first]:
        flat[(glyphName, second)] = correction

# result
# >>> flat = {
# >>>     ('A', 'V'): -80,
# >>>     ('Agrave', 'V'): -80,
# >>>     ('Aacute', 'V'): -80
# >>> }
