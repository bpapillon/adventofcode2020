def position_on_map(input_map, x, y):
    row = input_map[y]
    return row[divmod(x, len(input_map[0]))[1]]


def traverse(input_map, move_width, move_height):
    x = 0
    y = 0
    chars = []
    while y < len(input_map):
        chars.append(position_on_map(input_map, x, y))
        x += move_width
        y += move_height
    return len([char for char in chars if char == '#'])


filename = 'input.txt'
map_rows = open(filename, 'rb').read().strip().split("\n")
print 'part 1: ' + str(traverse(map_rows, 3, 1))

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
trees_encountered = map(lambda slope: traverse(map_rows, slope[0], slope[1]), slopes)
product_of_trees_encountered = reduce(lambda x, y: x * y, trees_encountered)
print 'part 2: ' + str(product_of_trees_encountered)
