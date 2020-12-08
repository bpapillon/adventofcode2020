def group_count_any(group):
    return len(set(list(group.replace('\n', ''))))


def group_count_all(group):
    member_count = len(group.split('\n'))
    chars = group.replace('\n', '')
    char_counts = dict(map(lambda x: [x, chars.count(x)], chars))
    return len([char for char, count in char_counts.items() if count == member_count])


filename = 'input.txt'
groups = open(filename, 'rb').read().strip().split('\n\n')
counts_any = map(group_count_any, groups)
total_any = reduce(lambda x, y: x + y, counts_any)
print 'part 1: ' + str(total_any)

counts_all = map(group_count_all, groups)
total_all = reduce(lambda x, y: x + y, counts_all)
print 'part 2: ' + str(total_all)
