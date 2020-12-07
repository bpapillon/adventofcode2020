def binary_split(items, char):
    if char in set(['F', 'L']):
        return items[:len(items) / 2]
    if char in set(['B', 'R']):
        return items[len(items) / 2:]


def highest_seat_id(filename):
    boarding_passes = open(filename, 'rb').read().strip().split("\n")
    seat_ids = map(parse_boarding_pass, boarding_passes)
    return max(seat_ids)


def parse_boarding_pass(boarding_pass):
    rows = range(0, 128)
    columns = range(0, 8)
    row_input = list(boarding_pass[:7])
    column_input = list(boarding_pass[7:])
    row = reduce(binary_split, row_input, rows)[0]
    column = reduce(binary_split, column_input, columns)[0]
    seat_id = row * 8 + column
    return seat_id


def find_missing_number(ls):
    if len(ls) == 1:
        return ls[0] + 1
    midpoint = len(ls) / 2
    expected = ls[0] + midpoint
    if ls[midpoint] == expected:
        return find_missing_number(ls[midpoint:])
    else:
        return find_missing_number(ls[:midpoint])


def find_missing_seat(filename):
    boarding_passes = open(filename, 'rb').read().strip().split("\n")
    seat_ids = map(parse_boarding_pass, boarding_passes)
    return find_missing_number(sorted(seat_ids))


filename = 'input.txt'
print 'part 1 - max seat ID: ' + str(highest_seat_id(filename))
print 'part 2 - my seat ID: ' + str(find_missing_seat(filename))
