import itertools

def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ...
    straight from itertools docs page"""
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def findInterval(sequence, value):
    for thisValue, nextValue in pairwise(sequence):
        if thisValue <= value <= nextValue:
            return thisValue, nextValue
    raise ValueError('no interval found')


if __name__ == '__main__':
    seq = [.1, .2, .3, .4, .5]
    interval = findInterval(seq, .12)
    print(interval)
    # (0.1, 0.2)

    interval = findInterval(seq, .38)
    print(interval)
    # (0.3, 0.4)

    interval = findInterval(seq, .6)
    print(interval)
    # ValueError: no interval found