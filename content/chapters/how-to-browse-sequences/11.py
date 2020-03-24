myRandomNumbers = [8, 6, 5, 5, 0, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4, 7]
aNumber = myRandomNumbers.pop()
# aNumber: 7
# myRandomNumbers: [8, 6, 5, 5, 0, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4]
aNumber = myRandomNumbers.pop(0)
# aNumber: 8
# myRandomNumbers: [6, 5, 5, 0, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4]
aNumber = myRandomNumbers.pop(5)
# aNumber: 7
# myRandomNumbers: [6, 5, 5, 0, 1, 7, 6, 7, 2, 5, 8, 6, 4]
aNumber = myRandomNumbers.pop(24)
# result: IndexError: pop index out of range
# check the len of the list before using pop
# with built-in function len()