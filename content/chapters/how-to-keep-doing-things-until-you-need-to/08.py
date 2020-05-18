index = 0

while index <= 20:
    index += 1

    if index % 2 == 0:
        print('found even number')
        continue
    print('found odd number')

print('outside the while loop')