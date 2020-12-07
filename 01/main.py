import itertools


def combo_product(combo):
    return reduce(lambda x, y: x * y, combo)


def combo_sum(combo):
    return reduce(lambda x, y: x + y, combo)


def product_of_entry_combination(entries, combination_size):
    combinations = itertools.combinations(entries, combination_size)
    combination = [combination for combination in combinations if combo_sum(combination) == 2020][0]
    return combo_product(combination)


integers = map(int, open('input.txt', 'rb').read().strip().split("\n"))
print 'part 1: ' + str(product_of_entry_combination(integers, 2))
print 'part 2: ' + str(product_of_entry_combination(integers, 3))
