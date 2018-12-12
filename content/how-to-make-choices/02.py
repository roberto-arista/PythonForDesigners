myFirstList = [1, ‘a’, False]
mySecondList = myFirstList
myThirdList = [1, ‘a’, False]

# two aliases referring to the same object in memory
myFirstList is mySecondList
# True

# extra check
id(myFirstList) == id(mySecondList)
# True

# two aliases referring to two different objects with the same content
myFirstList is myThirdList
# False

# indeed they have the same content
myFirstList == myThirdList
# True

# but different identity
id(myFirstList) == id(myThirdList)
# False