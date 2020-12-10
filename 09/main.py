import itertools


def find_encryption_weakness(numbers, invalid_number):
    slice_length = 2
    while True:
        try:
            match = next(x for x in slices(numbers, slice_length) if sum(x) == invalid_number)
            return min(match) + max(match)
        except StopIteration:
            pass
        slice_length += 1


def find_invalid_number(numbers, preamble_length):
    for idx, number in enumerate(numbers):
        if idx < preamble_length:
            continue
        valid = set(map(sum, itertools.combinations(numbers[idx - preamble_length:idx], 2)))
        if number not in valid:
            return number


def slices(enum, length):
    for i in xrange(len(enum) - length + 1):
        yield enum[i:i + length]


filename = 'input.txt'
preamble_length = 25
numbers = map(int, open(filename, 'rb').read().strip().split('\n'))
invalid_number = find_invalid_number(numbers, preamble_length)
print "part 1: " + str(invalid_number)
print "part 2: " + str(find_encryption_weakness(numbers, invalid_number))
