def interpolateValue(a, b, factor):
    value = a + (b-a)*factor

myValue = interpolateValue(10, 20, .5)
print(myValue)