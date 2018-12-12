myRandomNumbers = [8, 6, 5, 5, 0, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4, 7]
myRandomNumbers.remove(5) # remember: item is not the position index!
# result: [8, 6, 5, 0, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4, 7]
myRandomNumbers.remove(5)
# result: [8, 6, 0, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4, 7]
myRandomNumbers.remove(0)
# result: [8, 6, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4, 7]
myRandomNumbers.remove(0)
# result: ValueError: list.remove(x): x not in list
# check if the list contains the element you want to remove
# with in keyword
if 0 in myRandomNumbers:
    myRandomNumbers.remove(0)
# result: [8, 6, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4, 7]
