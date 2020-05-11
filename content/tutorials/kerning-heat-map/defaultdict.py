from collections import defaultdict

kerning = defaultdict(int)
kerning.setdefault(0)

# let's create a fake pair
kerning[('A', 'V')] = -80

# If key is in the dictionary, return its value
print(kerning[('A', 'V')])
# >>> -80

# If not, 0 is returned
print(kerning[('H', 'H')])
# >>> 0
