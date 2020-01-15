newPage(100, 100)
myVar = 10

# chained comparison expressions!
# it is helpful when looking for
# a value included between values
if 20 < myVar:
    fill(0)
elif 20 >= myVar > 12:
    fill(.3)
elif 12 >= myVar > 8:
    fill(.6)
else:
    fill(.9)
rect(10, 10, 50, 50)